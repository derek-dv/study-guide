---
name: bite-size-study-guide
description: Researches a topic, course, or subject, builds clear insights, and summarizes it into bite-sized study chunks and quiz flashcards for students. Use when a user says "Help me study about this topic:", "Break down this subject for me", "Make bite-sized study notes on", or asks for an easy-to-digest study guide.
---

# Bite-Size Study Guide

Help students learn any topic quickly by researching the core ideas, stripping away textbook fluff, and organizing the lesson into short, memorable study blocks.

## Step-by-Step Instructions

1. **Read the Formatting & Quality Rules**
   Before writing the study guide, read `references/bite-size-framework.md` to follow the Bite-Size Study Rules, required section layout, and good vs. bad examples.

2. **Research the Topic**
   - Identify the student's topic, subject, or course level.
   - Gather the essential facts, definitions, and cause-and-effect relationships (use web search or workspace files if needed).
   - Focus on **why it matters** and **how it works**, not just raw facts to memorize.

3. **Draft the Bite-Size Study Guide**
   Follow the template in `references/bite-size-framework.md`:
   - **The 1-Sentence Big Picture**: Explain the whole topic in one plain-English sentence.
   - **Bite-Sized Core Concepts (3 to 5 blocks)**: Give each block a bold title and 2 to 3 short bullet points (keep bullets under 25 words each).
   - **Real-World Analogy**: Connect the topic to an everyday situation students already understand.
   - **Key Insight / Exam Trap**: Highlight one common mistake students make and how to avoid it.
   - **Active Recall Flashcards (3 Q&A pairs)**: Write 3 quick test questions using `Q:` and `A:` lines.

4. **Verify Bite-Size Readability with the Script**
   Whenever you save study notes to a file (or when checking a draft), run `scripts/check_study_notes.py` to confirm bullets are short, sections are balanced, and flashcards are properly formatted:
   ```bash
   python3 scripts/check_study_notes.py path/to/study_notes.md
   ```
   - If the script reports any bullet over 25 words or missing flashcards, shorten the text and re-run the script until it passes.
   - If the student asks for flashcards to import into Anki or Quizlet, run:
     ```bash
     python3 scripts/check_study_notes.py path/to/study_notes.md --export-csv flashcards.csv
     ```

## Examples

### Example 1: Science Topic
**User says:** `Help me study about this topic: Photosynthesis`

**Agent response structure:**
- **The 1-Sentence Big Picture**: Photosynthesis is how plants use sunlight to turn water and air into sugar for food and oxygen for us to breathe.
- **Bite-Sized Core Concepts**:
  1. **The Ingredients (Inputs)**: Plants take in water through roots, carbon dioxide through leaves, and light through chlorophyll.
  2. **The Two Stages**: Light reactions capture solar energy; the Calvin cycle uses that energy to build glucose (sugar).
  3. **The Output**: Glucose feeds the plant, and oxygen is released into the air as a bonus.
- **Real-World Analogy**: Think of a leaf as a solar-powered kitchen that bakes sugar cakes out of air and water.
- **Key Insight / Exam Trap**: Plants still do cellular respiration at night! Don't say plants only make oxygen and never use it.
- **Active Recall Flashcards**:
  - `Q: Where inside the plant cell does photosynthesis happen?`
  - `A: Inside the chloroplasts.`
  - `Q: What are the two main stages of photosynthesis?`
  - `A: The light-dependent reactions and the Calvin cycle.`
  - `Q: What gas do plants take in during photosynthesis, and what gas do they release?`
  - `A: They take in carbon dioxide (CO2) and release oxygen (O2).`

### Example 2: Computer Science Topic
**User says:** `Help me study about this topic: Recursion in programming`

**Agent action:** Reads `references/bite-size-framework.md`, explains recursion using the "base case vs. recursive step" breakdown and a Russian nesting dolls analogy, writes 3 `Q:`/`A:` flashcards, and validates saved notes with `scripts/check_study_notes.py`.
