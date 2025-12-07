#!/usr/bin/env python3
"""
Karm Progress Tracker

A CLI tool for tracking learning progress across Karm curriculum modules.
Monitors completion status, generates progress reports, and provides learning insights.

Usage: python progress-tracker.py
"""

import json
import os
import argparse
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from pathlib import Path


class KarmProgressTracker:
    """Tracks and manages learning progress across Karm curriculum."""

    def __init__(self, progress_file: str = "karm-progress.json"):
        self.progress_file = progress_file
        self.curriculum = {
            "01-foundations": {
                "programming-fundamentals": {"name": "Programming Fundamentals", "total_sections": 15, "estimated_hours": 8},
                "data-structures-algorithms": {"name": "Data Structures & Algorithms", "total_sections": 12, "estimated_hours": 10}
            },
            "02-backend-engineering": {
                "api-design": {"name": "API Design & REST", "total_sections": 14, "estimated_hours": 12},
                "databases": {"name": "Databases & Storage", "total_sections": 16, "estimated_hours": 14}
            },
            "05-devops-cloud": {
                "devops-cicd": {"name": "DevOps & CI/CD", "total_sections": 10, "estimated_hours": 8}
            }
        }

    def load_progress(self) -> Dict:
        """Load progress data from file."""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return self.initialize_progress()
        return self.initialize_progress()

    def initialize_progress(self) -> Dict:
        """Initialize empty progress structure."""
        progress = {
            "version": "1.0",
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "modules": {}
        }

        # Initialize all curriculum modules
        for module_key, topics in self.curriculum.items():
            progress["modules"][module_key] = {"topics": {}}
            for topic_key, topic_info in topics.items():
                progress["modules"][module_key]["topics"][topic_key] = {
                    "name": topic_info["name"],
                    "status": "not_started",  # not_started, in_progress, completed
                    "start_date": None,
                    "completion_date": None,
                    "completed_sections": 0,
                    "total_sections": topic_info["total_sections"],
                    "estimated_hours": topic_info["estimated_hours"],
                    "actual_hours": 0,
                    "notes": []
                }

        return progress

    def save_progress(self, progress: Dict) -> None:
        """Save progress data to file."""
        progress["last_updated"] = datetime.now().isoformat()

        try:
            os.makedirs(os.path.dirname(self.progress_file), exist_ok=True)
            with open(self.progress_file, 'w') as f:
                json.dump(progress, f, indent=2, ensure_ascii=False)
        except (IOError, OSError) as e:
            print_with_color(f"Error saving progress: {e}", "red")
            return

    def start_topic(self, progress: Dict, module: str, topic: str) -> bool:
        """Mark a topic as started."""
        if module not in progress["modules"]:
            print_with_color(f"Module '{module}' not found", "red")
            return False

        if topic not in progress["modules"][module]["topics"]:
            print_with_color(f"Topic '{topic}' not found in module '{module}'", "red")
            return False

        topic_data = progress["modules"][module]["topics"][topic]
        if topic_data["status"] == "not_started":
            topic_data["status"] = "in_progress"
            topic_data["start_date"] = datetime.now().isoformat()
            return True
        else:
            print_with_color(f"Topic '{topic}' is already {topic_data['status']}", "yellow")
            return False

    def complete_topic(self, progress: Dict, module: str, topic: str, actual_hours: Optional[int] = None) -> bool:
        """Mark a topic as completed."""
        if module not in progress["modules"]:
            print_with_color(f"Module '{module}' not found", "red")
            return False

        if topic not in progress["modules"][module]["topics"]:
            print_with_color(f"Topic '{topic}' not found in module '{module}'", "red")
            return False

        topic_data = progress["modules"][module]["topics"][topic]

        # Mark remaining sections as completed if not already
        if topic_data["completed_sections"] < topic_data["total_sections"]:
            topic_data["completed_sections"] = topic_data["total_sections"]

        topic_data["status"] = "completed"
        topic_data["completion_date"] = datetime.now().isoformat()

        if actual_hours is not None:
            topic_data["actual_hours"] = actual_hours

        return True

    def update_progress(self, progress: Dict, module: str, topic: str,
                       completed_sections: Optional[int] = None,
                       actual_hours: Optional[int] = None,
                       note: Optional[str] = None) -> bool:
        """Update progress for a specific topic."""
        if module not in progress["modules"]:
            print_with_color(f"Module '{module}' not found", "red")
            return False

        if topic not in progress["modules"][module]["topics"]:
            print_with_color(f"Topic '{topic}' not found in module '{module}'", "red")
            return False

        topic_data = progress["modules"][module]["topics"][topic]

        # Mark as in progress if not started
        if topic_data["status"] == "not_started":
            self.start_topic(progress, module, topic)
            topic_data = progress["modules"][module]["topics"][topic]  # Refresh reference

        updated = False

        if completed_sections is not None:
            if 0 <= completed_sections <= topic_data["total_sections"]:
                topic_data["completed_sections"] = completed_sections
                updated = True
            else:
                print_with_color(f"Invalid section count. Must be 0-{topic_data['total_sections']}", "red")
                return False

        if actual_hours is not None:
            topic_data["actual_hours"] = max(0, actual_hours)
            updated = True

        if note:
            note_entry = {
                "date": datetime.now().isoformat(),
                "note": note
            }
            if "notes" not in topic_data:
                topic_data["notes"] = []
            topic_data["notes"].append(note_entry)
            updated = True

        return updated

    def generate_report(self, progress: Dict) -> str:
        """Generate a comprehensive progress report."""
        report_lines = []
        report_lines.append("🧠 KARM LEARNING PROGRESS REPORT")
        report_lines.append("=" * 50)
        report_lines.append("")

        total_topics = 0
        completed_topics = 0
        total_estimated_hours = 0
        total_actual_hours = 0

        for module_key, module_data in progress["modules"].items():
            module_name = module_key.replace("-", " ").title()
            report_lines.append(f"📚 {module_name}")
            report_lines.append("-" * 30)

            module_topics = 0
            module_completed = 0
            module_hours = 0
            module_actual = 0

            for topic_key, topic_data in module_data["topics"].items():
                total_topics += 1
                module_topics += 1

                status_icon = {
                    "not_started": "⬜",
                    "in_progress": "🟡",
                    "completed": "✅"
                }.get(topic_data["status"], "⬜")

                completion_percent = (
                    topic_data["completed_sections"] / topic_data["total_sections"] * 100
                    if topic_data["total_sections"] > 0 else 0
                )

                report_lines.append(
                    f"   {status_icon} {topic_key}: {topic_data['name']} "
                    f"({topic_data['completed_sections']}/{topic_data['total_sections']} sections, "
                    f"{completion_percent:.1f}%)"
                )

                if topic_data["status"] == "completed":
                    completed_topics += 1
                    module_completed += 1

                total_estimated_hours += topic_data["estimated_hours"]
                total_actual_hours += topic_data["actual_hours"]
                module_hours += topic_data["estimated_hours"]
                module_actual += topic_data["actual_hours"]

            # Module summary
            if module_topics > 0:
                module_completion = module_completed / module_topics * 100
                report_lines.append(f"Module completion: {module_completion:.1f}% ({module_completed}/{module_topics} topics)")
                report_lines.append("")

        # Overall summary
        report_lines.append("📊 OVERALL PROGRESS")
        report_lines.append("=" * 30)

        if total_topics > 0:
            overall_completion = completed_topics / total_topics * 100
            report_lines.append(f"Overall completion: {overall_completion:.1f}% ({completed_topics}/{total_topics} topics)")
            report_lines.append(f"Estimated hours: {total_estimated_hours}")
            report_lines.append(f"Actual hours spent: {total_actual_hours}")
            if total_estimated_hours > 0:
                efficiency_ratio = total_actual_hours / total_estimated_hours * 100 if total_actual_hours > 0 else 0
                report_lines.append(f"Time efficiency: {efficiency_ratio:.1f}%")

        report_lines.append("")
        report_lines.append("Last updated: " + progress.get("last_updated", "Unknown"))

        return "\n".join(report_lines)

    def get_recommendations(self, progress: Dict) -> List[str]:
        """Generate personalized learning recommendations."""
        recommendations = []

        # Find topics to start
        not_started = []
        in_progress_but_incomplete = []

        for module_key, module_data in progress["modules"].items():
            for topic_key, topic_data in module_data["topics"].items():
                if topic_data["status"] == "not_started":
                    not_started.append(topic_data["name"])
                elif topic_data["status"] == "in_progress":
                    completion_ratio = topic_data["completed_sections"] / topic_data["total_sections"]
                    if completion_ratio < 0.8:  # Less than 80% complete
                        in_progress_but_incomplete.append(topic_data["name"])

        if not_started:
            recommendations.append(f"🚀 Start these foundational topics: {', '.join(not_started[:3])}")

        if in_progress_but_incomplete:
            recommendations.append(f"⚡ Complete these in-progress topics: {', '.join(in_progress_but_incomplete[:3])}")

        # Check for over-studying
        over_invested = []
        for module_key, module_data in progress["modules"].items():
            for topic_key, topic_data in module_data["topics"].items():
                if topic_data["actual_hours"] > topic_data["estimated_hours"] * 1.5:
                    over_invested.append(topic_data["name"])

        if over_invested:
            recommendations.append(f"⏰ Consider if extra time on these topics is necessary: {', '.join(over_invested[:2])}")

        # Default recommendations
        if not recommendations:
            recommendations.extend([
                "🎯 Focus on completing in-progress topics before starting new ones",
                "📚 Consider working through topics in curriculum order for best understanding",
                "🧪 Practice with side projects to reinforce learning",
                "📈 Track your progress regularly to stay motivated"
            ])

        return recommendations[:4]  # Limit to 4 recommendations


def print_with_color(text: str, color: str = "white") -> None:
    """Print text with ANSI color codes."""
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }

    color_code = colors.get(color, colors["white"])
    print(f"{color_code}{text}{colors['reset']}")


def main():
    """Main CLI entry point for the progress tracker."""
    parser = argparse.ArgumentParser(
        description="🧠 Karm Progress Tracker - Track your learning journey",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python progress-tracker.py                           # Show progress report
  python progress-tracker.py start 01-foundations programming-fundamentals
  python progress-tracker.py update 01-foundations programming-fundamentals --sections 8 --hours 6
  python progress-tracker.py complete 01-foundations programming-fundamentals --hours 12
  python progress-tracker.py recommendations            # Show personalized tips
        """
    )

    parser.add_argument('--file', help='Progress file path', default='karm-progress.json')

    subparsers = parser.add_subparsers(dest='command', metavar='COMMAND')

    # Default report command
    subparsers.add_parser('report', aliases=['r'], help='Show progress report')

    # Start topic command
    start_parser = subparsers.add_parser('start', aliases=['s'], help='Start working on a topic')
    start_parser.add_argument('module', help='Module name (e.g., 01-foundations)')
    start_parser.add_argument('topic', help='Topic name (e.g., programming-fundamentals)')

    # Update progress command
    update_parser = subparsers.add_parser('update', aliases=['u'], help='Update topic progress')
    update_parser.add_argument('module', help='Module name')
    update_parser.add_argument('topic', help='Topic name')
    update_parser.add_argument('--sections', '-s', type=int, help='Number of completed sections')
    update_parser.add_argument('--hours', '-t', type=int, help='Actual hours spent')
    update_parser.add_argument('--note', '-n', help='Add a progress note')

    # Complete topic command
    complete_parser = subparsers.add_parser('complete', aliases=['c'], help='Mark topic as completed')
    complete_parser.add_argument('module', help='Module name')
    complete_parser.add_argument('topic', help='Topic name')
    complete_parser.add_argument('--hours', '-t', type=int, help='Actual hours spent')

    # Recommendations command
    subparsers.add_parser('recommendations', aliases=['rec'], help='Show personalized recommendations')

    # List available topics
    list_parser = subparsers.add_parser('list', aliases=['l'], help='List available topics')
    list_parser.add_argument('--module', '-m', help='Filter by module')

    args = parser.parse_args()

    tracker = KarmProgressTracker(args.file)
    progress = tracker.load_progress()

    # Default to report if no command specified
    if not args.command:
        args.command = 'report'

    success = True

    if args.command == 'report':
        report = tracker.generate_report(progress)
        print(report)

    elif args.command == 'start':
        success = tracker.start_topic(progress, args.module, args.topic)
        if success:
            print_with_color(f"Started learning: {args.topic}", "green")
        else:
            success = False

    elif args.command == 'update':
        success = tracker.update_progress(
            progress, args.module, args.topic,
            args.sections, args.hours, args.note
        )
        if success:
            print_with_color(f"Updated progress: {args.topic}", "green")

    elif args.command == 'complete':
        success = tracker.complete_topic(progress, args.module, args.topic, args.hours)
        if success:
            print_with_color(f"Completed topic: {args.topic} ✅", "green")

    elif args.command == 'recommendations':
        recommendations = tracker.get_recommendations(progress)
        print("💡 Personalized Recommendations:")
        print("-" * 40)
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")

    elif args.command == 'list':
        print("📚 Available Karm Topics:")
        print("-" * 30)

        for module_key, module_data in progress["modules"].items():
            if args.module and args.module != module_key:
                continue

            print(f"🔧 {module_key.replace('-', ' ').title()}")
            for topic_key, topic_data in module_data["topics"].items():
                status = topic_data["status"]
                status_icon = {
                    "not_started": "⬜",
                    "in_progress": "🟡",
                    "completed": "✅"
                }.get(status, "⬜")

                print(f"   {status_icon} {topic_key}: {topic_data['name']}")
            print()

    if success:
        tracker.save_progress(progress)

    if not success:
        exit(1)


if __name__ == "__main__":
    main()
