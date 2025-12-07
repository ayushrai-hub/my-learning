#!/usr/bin/env python3
"""
Interactive Skill Assessment Tool for Karm Learning Platform

This tool loads assessment files from skill-testing/ and provides
an interactive assessment experience with timing, scoring, and feedback.

Usage:
    python skill-assessor.py --skill "backend-engineering"
    python skill-assessor.py --list
    python skill-assessor.py --skill "programming-foundations" --level 2
"""

import json
import os
import time
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import re


class SkillAssessor:
    """Interactive skill assessment tool for Karm platform."""

    def __init__(self, skill_testing_dir: str = "skill-testing"):
        self.skill_testing_dir = Path(skill_testing_dir)
        self.current_assessment = None
        self.scores = {}
        self.start_time = None
        self.responses = {}

    def list_available_skills(self) -> List[str]:
        """List all available skill assessment files."""
        if not self.skill_testing_dir.exists():
            print(f"Skill testing directory '{self.skill_testing_dir}' not found.")
            return []

        skills = []
        for file in self.skill_testing_dir.glob("*-tests.md"):
            skill_name = file.stem.replace("-tests", "").replace("-", " ").title()
            skills.append(skill_name)

        return skills

    def load_assessment(self, skill: str) -> bool:
        """Load assessment file for specified skill."""
        # Convert skill name to filename
        filename = skill.lower().replace(" ", "-") + "-tests.md"
        filepath = self.skill_testing_dir / filename

        if not filepath.exists():
            print(f"Assessment file not found: {filepath}")
            available = self.list_available_skills()
            if available:
                print(f"Available skills: {', '.join(available)}")
            return False

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            self.current_assessment = self._parse_assessment(content, skill)
            return True

        except Exception as e:
            print(f"Error loading assessment: {e}")
            return False

    def _parse_assessment(self, content: str, skill: str) -> Dict:
        """Parse markdown assessment content into structured data."""
        assessment = {
            "skill": skill,
            "levels": {},
            "sections": []
        }

        # Extract sections
        sections = re.split(r'^## ', content, flags=re.MULTILINE)

        for section in sections[1:]:  # Skip header
            section_name = section.split('\n')[0].strip()

            if "Level" in section_name and "Assessment" in section_name:
                level_num = re.search(r'Level (\d+)', section_name)
                if level_num:
                    level_key = f"level_{level_num.group(1)}"
                    assessment["levels"][level_key] = self._parse_level(section)

            assessment["sections"].append(section_name)

        return assessment

    def _parse_level(self, content: str) -> Dict:
        """Parse individual level content."""
        level = {
            "questions": [],
            "challenges": [],
            "exercises": [],
            "tasks": []
        }

        # Parse theoretical questions
        questions_match = re.search(r'### Theoretical Questions.*?(\d+) questions.*?(.*?)(?=###|\Z)', content, re.DOTALL)
        if questions_match:
            level["questions"] = [q.strip() for q in content.split('\n') if q.strip() and not q.startswith('###')][:5]  # Limit to 5

        return level

    def start_assessment(self, level: int = 1) -> bool:
        """Start assessment for specified level."""
        if not self.current_assessment:
            print("No assessment loaded. Use --skill to specify an assessment.")
            return False

        level_key = f"level_{level}"
        if level_key not in self.current_assessment["levels"]:
            print(f"Level {level} not available for this assessment.")
            return False

        print(f"🧠 Starting {self.current_assessment['skill'].title()} Assessment - Level {level}")
        print("=" * 60)
        print("Instructions: Answer to the best of your ability. Take your time.\n")

        self.start_time = time.time()
        self.scores[level_key] = self._run_level_assessment(level)
        duration = time.time() - self.start_time

        print("\n📊 Assessment Complete!")
        print(".2f")
        print(f"Score Breakdown: {self.scores[level_key]}")

        return True

    def _run_level_assessment(self, level: int) -> Dict:
        """Run assessment questions for specified level."""
        level_key = f"level_{level}"
        level_data = self.current_assessment["levels"][level_key]

        scores = {"theoretical": 0, "practical": 0, "total": 0}
        question_count = len(level_data.get("questions", []))

        if question_count > 0:
            print(f"📝 Theoretical Questions ({question_count} questions):\n")

            for i, question in enumerate(level_data["questions"][:3], 1):  # Limit to 3 for demo
                print(f"{i}. {question}")

                # Simulate question answering (in real implementation, get user input)
                user_answer = input(f"Your answer to question {i}: ").strip()
                self.responses[f"q{i}"] = user_answer

                # Simple scoring simulation
                score = len(user_answer) > 10  # Basic heuristic
                scores["theoretical"] += score

                print(f"✓ Scored {score}/1 for question {i}\n")

        # Practical sections would go here
        scores["total"] = scores["theoretical"] + scores["practical"]

        return scores

    def generate_report(self, level: int = 1) -> str:
        """Generate assessment report."""
        if not self.scores:
            return "No assessment data available."

        level_key = f"level_{level}"
        score_data = self.scores.get(level_key, {})

        report = f"""
🎯 Karm Skill Assessment Report
================================

Skill: {self.current_assessment['skill'].title() if self.current_assessment else 'Unknown'}
Level: {level}
Date: {time.strftime('%Y-%m-%d %H:%M:%S')}

📈 Performance Summary
----------------------
Theoretical Score: {score_data.get('theoretical', 0)}/3
Practical Score: {score_data.get('practical', 0)}/0
Total Score: {score_data.get('total', 0)}/3

🏆 Achievement Level: {self._calculate_achievement_level(score_data.get('total', 0))}

📋 Detailed Feedback
-------------------
"""

        # Add specific feedback based on scores
        total_score = score_data.get('total', 0)
        if total_score >= 2:
            report += "✨ Excellent! You demonstrate strong understanding of core concepts.\n"
        elif total_score >= 1:
            report += "👍 Good foundation. Consider reviewing areas with lower scores.\n"
        else:
            report += "💪 Keep learning! Focus on core concepts and practice regularly.\n"

        report += "\n🎯 Next Steps:\n"
        report += "- Review weak areas with additional study\n"
        report += "- Complete practice projects from Karm\n"
        report += "- Take advanced assessments when ready\n"

        return report

    def _calculate_achievement_level(self, score: int) -> str:
        """Calculate achievement level based on score."""
        if score >= 3:
            return "Expert"
        elif score >= 2:
            return "Advanced"
        elif score >= 1:
            return "Intermediate"
        else:
            return "Beginner"


def main():
    parser = argparse.ArgumentParser(description="Karm Skill Assessment Tool")
    parser.add_argument("--skill", help="Specify skill to assess")
    parser.add_argument("--level", type=int, default=1, help="Assessment level (1-4)")
    parser.add_argument("--list", action="store_true", help="List available skills")

    args = parser.parse_args()

    assessor = SkillAssessor()

    if args.list:
        print("📚 Available Skills:")
        skills = assessor.list_available_skills()
        for skill in skills:
            print(f"  • {skill}")
        return

    if not args.skill:
        parser.print_help()
        return

    # Load and run assessment
    skill_formatted = args.skill.lower().replace("-", " ").replace("_", " ")
    skill_file = skill_formatted.replace(" ", "-")

    if assessor.load_assessment(skill_file):
        if assessor.start_assessment(args.level):
            report = assessor.generate_report(args.level)
            print(report)

            # Save report to file
            report_file = f"assessment_report_{skill_file}_level_{args.level}.txt"
            with open(report_file, 'w') as f:
                f.write(report)
            print(f"📄 Report saved to: {report_file}")


if __name__ == "__main__":
    main()
