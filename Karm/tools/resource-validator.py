#!/usr/bin/env python3
"""
Resource Validator for Karm Learning Platform

This tool crawls all markdown files in the curriculum and validates
external links, checks for broken URLs, and suggests alternatives.

Usage:
    python resource-validator.py --check-all
    python resource-validator.py --check-curriculum
    python resource-validator.py --report
"""

import re
import requests
import json
import time
from pathlib import Path
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Set, Tuple
import argparse


class ResourceValidator:
    """Validates external resources and links in Karm curriculum."""

    def __init__(self, karm_root: str = "."):
        self.karm_root = Path(karm_root)
        self.results = {
            "total_urls": 0,
            "valid_urls": 0,
            "invalid_urls": 0,
            "broken_urls": [],
            "warnings": [],
            "checked_files": [],
            "scan_time": 0
        }
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Karm-Resource-Validator/1.0 (Educational Platform Link Checker)'
        })

    def find_markdown_files(self) -> List[Path]:
        """Find all markdown files in the Karm directory."""
        if not self.karm_root.exists():
            print(f"Karm root directory '{self.karm_root}' not found.")
            return []

        # Look for .md files in karm curriculum and other directories
        patterns = [
            "**/*.md",
            "curriculum/**/*.md"
        ]

        files = []
        for pattern in patterns:
            try:
                files.extend(self.karm_root.glob(pattern))
            except Exception as e:
                print(f"Warning: Could not scan pattern {pattern}: {e}")

        return sorted(set(files))

    def extract_urls(self, content: str) -> Set[str]:
        """Extract all URLs from markdown content."""
        urls = set()

        # Markdown link patterns: [text](url)
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        links = re.findall(link_pattern, content)

        for _, url in links:
            # Clean up the URL (remove surrounding quotes if any)
            url = url.strip('"\'')

            # Skip local/internal links
            if not url.startswith(('http://', 'https://')):
                continue

            # Skip obvious placeholders
            if any(placeholder in url.lower() for placeholder in [
                'example.com', 'your-website.com', 'localhost', '127.0.0.1'
            ]):
                continue

            urls.add(url)

        # Also check for bare URLs (though less common in markdown)
        url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
        bare_urls = re.findall(url_pattern, content)

        for url in bare_urls:
            if not any(placeholder in url.lower() for placeholder in [
                'example.com', 'localhost', '127.0.0.1'
            ]):
                urls.add(url)

        return urls

    def check_url_status(self, url: str) -> Tuple[str, str, int]:
        """
        Check if a URL is accessible.
        Returns (url, status, response_time_ms)
        """
        try:
            start_time = time.time()
            response = self.session.head(url, timeout=10, allow_redirects=True)

            # Some sites don't allow HEAD requests, try GET
            if response.status_code >= 400:
                response = self.session.get(url, timeout=10, allow_redirects=True)

            response_time = int((time.time() - start_time) * 1000)

            if 200 <= response.status_code < 300:
                status = "valid"
            elif response.status_code == 401:
                status = "auth_required"
            elif 400 <= response.status_code < 500:
                status = "client_error"
            elif 500 <= response.status_code < 600:
                status = "server_error"
            else:
                status = f"http_{response.status_code}"

            return url, status, response_time

        except requests.exceptions.Timeout:
            return url, "timeout", 10000
        except requests.exceptions.ConnectionError:
            return url, "connection_error", 0
        except requests.exceptions.RequestException as e:
            return url, f"error_{type(e).__name__}", 0
        except Exception as e:
            return url, f"unknown_error", 0

    def validate_file_links(self, filepath: Path, check_links: bool = True) -> Dict:
        """Validate all links in a single file."""
        file_results = {
            "file": str(filepath.relative_to(self.karm_root)),
            "urls_found": 0,
            "urls_checked": 0,
            "valid_urls": 0,
            "invalid_urls": 0,
            "broken_urls": [],
            "warnings": []
        }

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            urls = self.extract_urls(content)
            file_results["urls_found"] = len(urls)

            if not check_links or not urls:
                return file_results

            # Check URLs with concurrency
            with ThreadPoolExecutor(max_workers=5) as executor:
                futures = {executor.submit(self.check_url_status, url): url for url in urls}

                for future in as_completed(futures):
                    url, status, response_time = future.result()

                    file_results["urls_checked"] += 1

                    if status == "valid":
                        file_results["valid_urls"] += 1
                    else:
                        file_results["invalid_urls"] += 1
                        file_results["broken_urls"].append({
                            "url": url,
                            "status": status,
                            "response_time_ms": response_time
                        })

                    # Update global results
                    self.results["total_urls"] += 1
                    if status == "valid":
                        self.results["valid_urls"] += 1
                    else:
                        self.results["invalid_urls"] += 1
                        self.results["broken_urls"].append({
                            "file": file_results["file"],
                            "url": url,
                            "status": status,
                            "response_time_ms": response_time
                        })

        except Exception as e:
            file_results["warnings"].append(f"Error processing file: {e}")

        return file_results

    def validate_all_resources(self, check_links: bool = True) -> Dict:
        """Validate resources across all markdown files."""
        start_time = time.time()

        files = self.find_markdown_files()
        print(f"🔍 Found {len(files)} markdown files to scan")

        all_file_results = []

        for i, filepath in enumerate(files, 1):
            print(f"📄 Processing {i}/{len(files)}: {filepath.name}")
            file_result = self.validate_file_links(filepath, check_links)
            all_file_results.append(file_result)

            # Progress indicator
            if i % 10 == 0 or i == len(files):
                checked = sum(f["urls_checked"] for f in all_file_results)
                valid = sum(f["valid_urls"] for f in all_file_results)
                print(f"  ↳ URLs checked: {checked}, Valid: {valid}")

        self.results["checked_files"] = all_file_results
        self.results["scan_time"] = time.time() - start_time

        return self.results

    def generate_report(self) -> str:
        """Generate validation report."""
        results = self.results

        report = f"""
🔗 Karm Resource Validation Report
===================================

📊 Scan Summary
---------------
Files Scanned: {len(results['checked_files'])}
Total URLs Found: {results['total_urls']}
URLs Checked: {results['total_urls']}
Valid URLs: {results['valid_urls']}
Invalid URLs: {results['invalid_urls']}
Scan Time: {results['scan_time']:.1f} seconds

"""

        if results['invalid_urls'] > 0:
            report += "🚨 Broken Links Found\n"
            report += "--------------------\n\n"

            broken_by_status = {}
            for broken in results['broken_urls'][:20]:  # Limit to first 20
                status = broken['status']
                if status not in broken_by_status:
                    broken_by_status[status] = []
                broken_by_status[status].append(broken)

            for status, links in broken_by_status.items():
                report += f"**{status.upper().replace('_', ' ')} ({len(links)} links):**\n"
                for link in links[:5]:  # Show first 5 per category
                    report += f"• {link['url']} ({link['file']})\n"
                if len(links) > 5:
                    report += f"  ... and {len(links) - 5} more\n"
                report += "\n"

        # Success rate
        if results['total_urls'] > 0:
            success_rate = (results['valid_urls'] / results['total_urls']) * 100
            report += f"{success_rate:.1f}%"
            if success_rate >= 95:
                report += " 🟢 Excellent!"
            elif success_rate >= 90:
                report += " 🟡 Good"
            elif success_rate >= 80:
                report += " 🟠 Needs attention"
            else:
                report += " 🔴 Requires immediate fixes"
        else:
            report += "No URLs found to validate."

        report += "\n\n📝 Recommendations\n"
        report += "-----------------\n"

        if results['invalid_urls'] > 0:
            report += "• Replace broken links with working alternatives\n"
            report += "• Consider using archived versions (archive.org) for historical links\n"
            report += "• Update outdated documentation links\n"

        report += "• Regularly run this validator to maintain link quality\n"
        report += "• Consider adding link checking to CI/CD pipeline\n"

        return report

    def save_report(self, filename: str = "resource_validation_report.json"):
        """Save detailed results to JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2, default=str)
        print(f"📄 Detailed report saved to: {filename}")


def main():
    parser = argparse.ArgumentParser(description="Karm Resource Validator")
    parser.add_argument("--check-all", action="store_true", help="Validate all resources")
    parser.add_argument("--check-curriculum", action="store_true", help="Validate only curriculum files")
    parser.add_argument("--report", action="store_true", help="Generate report from previous run")
    parser.add_argument("--output", default="resource_validation_report.json", help="Output file for detailed results")

    args = parser.parse_args()

    validator = ResourceValidator()

    if args.report:
        # Try to load previous results
        try:
            with open(args.output, 'r') as f:
                results = json.load(f)
            validator.results = results
            print(validator.generate_report())
        except FileNotFoundError:
            print(f"No previous report found at {args.output}")
            print("Run --check-all first to generate a report.")
        return

    check_links = True  # Can be configurable in future

    if args.check_all or args.check_curriculum:
        print("🚀 Starting Karm Resource Validation")
        print("=" * 50)

        results = validator.validate_all_resources(check_links)

        print("\n✅ Validation Complete!")
        print(report)

        validator.save_report(args.output)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
