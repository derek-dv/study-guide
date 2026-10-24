#!/usr/bin/env python3
"""
check_study_notes.py

What this script does:
  Checks a Markdown study guide to make sure it is truly "bite-sized" for students.
  It counts total words, estimates reading time, checks that bullet points stay
  within the 25-word limit, verifies that at least 3 Q:/A: flashcards exist,
  and can optionally export flashcards to a CSV file for Anki or Quizlet.

How to run it:
  1. Check a study guide file:
     python3 scripts/check_study_notes.py path/to/study_notes.md

  2. Export flashcards to a CSV file:
     python3 scripts/check_study_notes.py path/to/study_notes.md --export-csv flashcards.csv

  3. Run a built-in demo check (no extra file needed):
     python3 scripts/check_study_notes.py --demo
"""

import argparse
import csv
import math
import re
import sys
from pathlib import Path

MAX_BULLET_WORDS = 25
MIN_FLASHCARDS = 3
WORDS_PER_MINUTE = 200

DEMO_NOTES = """# Study Guide: Supply and Demand

## The 1-Sentence Big Picture
Prices go up when everyone wants something scarce, and prices drop when there is more stuff than buyers.

## Bite-Sized Core Concepts

### 1. Law of Demand
- When the price of an item rises, fewer people want to buy it.
- When the price drops, more buyers jump in.

### 2. Law of Supply
- Higher prices motivate sellers to produce and sell more of a product.
- Lower prices make sellers produce less because profit shrinks.

### 3. Market Equilibrium
- Equilibrium is the sweet-spot price where buyer demand exactly matches seller supply.
- At this point, there are no leftover goods and no shortages.

## Real-World Analogy
Think of concert tickets: when a famous band plays a tiny venue, ticket prices skyrocket; if they play an empty stadium, tickets go on discount.

## Key Insight & Exam Trap
- **Core Insight**: Price is the signal that balances what buyers want with what sellers make.
- **Watch Out**: A change in the item's own price moves ALONG the curve; outside factors SHIFT the whole curve.

## Active Recall Flashcards
Q: What happens to quantity demanded when the price of a good goes up?
A: Quantity demanded goes down.

Q: What is market equilibrium?
A: The price and quantity where supply equals demand, with no surplus or shortage.

Q: Does a change in an item's price shift the demand curve or move along it?
A: It causes a movement along the existing demand curve.
"""


def analyze_markdown(text: str):
    lines = text.splitlines()
    words = re.findall(r"\b\w+\b", text)
    total_words = len(words)
    reading_time_min = max(1, math.ceil(total_words / WORDS_PER_MINUTE))

    bullets = []
    long_bullets = []
    questions = []
    answers = []

    for line_num, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()
        if line.startswith(("- ", "* ")):
            bullet_text = line[2:].strip()
            bullet_words = re.findall(r"\b\w+\b", bullet_text)
            bullets.append((line_num, len(bullet_words), bullet_text))
            if len(bullet_words) > MAX_BULLET_WORDS:
                long_bullets.append((line_num, len(bullet_words), bullet_text))
        elif re.match(r"^[-*]?\s*Q:\s+", line, re.IGNORECASE):
            q_text = re.sub(r"^[-*]?\s*Q:\s+", "", line, flags=re.IGNORECASE).strip()
            questions.append(q_text)
        elif re.match(r"^[-*]?\s*A:\s+", line, re.IGNORECASE):
            a_text = re.sub(r"^[-*]?\s*A:\s+", "", line, flags=re.IGNORECASE).strip()
            answers.append(a_text)

    flashcards = list(zip(questions, answers))
    return {
        "total_words": total_words,
        "reading_time_min": reading_time_min,
        "bullet_count": len(bullets),
        "long_bullets": long_bullets,
        "flashcards": flashcards,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Check study notes for bite-size readability and extract flashcards."
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="Path to the Markdown study notes file to check.",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run the checker on a built-in sample study guide.",
    )
    parser.add_argument(
        "--export-csv",
        metavar="CSV_PATH",
        help="Optional path to export Q:/A: flashcards as a CSV file.",
    )
    args = parser.parse_args()

    if args.demo or not args.file:
        source_name = "Built-in Demo Study Guide (Supply and Demand)"
        text = DEMO_NOTES
    else:
        file_path = Path(args.file)
        if not file_path.is_file():
            print(f"Error: File not found: {file_path}", file=sys.stderr)
            sys.exit(1)
        source_name = str(file_path)
        text = file_path.read_text(encoding="utf-8")

    report = analyze_markdown(text)

    print("=== Bite-Size Study Guide Check ===")
    print(f"Source            : {source_name}")
    print(f"Total words       : {report['total_words']} words (~{report['reading_time_min']} min read)")
    print(f"Bullet points     : {report['bullet_count']} total (limit: {MAX_BULLET_WORDS} words per bullet)")
    print(f"Flashcards found  : {len(report['flashcards'])} Q&A pairs (minimum: {MIN_FLASHCARDS})")

    passed = True

    if report["long_bullets"]:
        passed = False
        print("\n[!] Bullets exceeding 25 words (shorten these for bite-size reading):")
        for line_num, count, snippet in report["long_bullets"]:
            preview = snippet[:60] + ("..." if len(snippet) > 60 else "")
            print(f"  - Line {line_num} ({count} words): {preview}")
    else:
        print("Bullet length check: PASSED (all bullets are 25 words or fewer)")

    if len(report["flashcards"]) < MIN_FLASHCARDS:
        passed = False
        print(
            f"Flashcard check   : FAILED (found {len(report['flashcards'])}, need at least {MIN_FLASHCARDS} Q:/A: pairs)"
        )
    else:
        print("Flashcard check   : PASSED")

    if args.export_csv:
        csv_path = Path(args.export_csv)
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Question", "Answer"])
            for q, a in report["flashcards"]:
                writer.writerow([q, a])
        print(f"Exported {len(report['flashcards'])} flashcards to {csv_path}")

    print("-----------------------------------")
    if passed:
        print("Overall Status    : PASS (Ready for students!)")
        sys.exit(0)
    else:
        print("Overall Status    : NEEDS REVISION")
        sys.exit(1)


if __name__ == "__main__":
    main()
