# Bite-Size Study Guide (`bite-size-study-guide`)

This skill helps your AI agent research any school topic, course, or subject, find the most important insights, and turn them into short, easy-to-read study notes for students. Instead of giving you long walls of textbook text, it breaks lessons into small blocks, real-world analogies, exam traps, and self-test flashcards.

---

## Example Prompts That Trigger This Skill

Ask your AI agent any of these:
- `"Help me study about this topic: Photosynthesis"`
- `"Help me study about this topic: Supply and Demand in Economics"`
- `"Break down this subject for me: Recursion in computer science"`
- `"Make bite-sized study notes on the French Revolution"`

---

## What Is in This Repo?

- **`SKILL.md`** — The main instruction card the agent always reads to know when to activate and what steps to follow.
- **`scripts/check_study_notes.py`** — A small program inside `scripts/` that the agent runs to do an exact job: checking that every bullet point stays short (25 words or fewer), counting the flashcards, estimating reading time, and optionally exporting flashcards to a `.csv` file for Anki or Quizlet.
- **`references/bite-size-framework.md`** — Extra reading inside `references/` that the agent opens only when needed, containing the 5 Bite-Size Study Rules, the study note template, and good vs. bad examples.
- **`LICENSE`** — Standard MIT open-source license.
- **`.gitignore`** — Keeps temporary and system files out of Git.

---

## How to Install

> **Note:** Replace `YOUR_GITHUB_USERNAME` and `REPO_NAME` (for example, `bite-size-study-guide`) with your actual GitHub username and repository name.

### 1. Check the skill before installing
```bash
npx skills add YOUR_GITHUB_USERNAME/REPO_NAME --list
```

### 2. Install with one command (`npx`)
```bash
npx skills add YOUR_GITHUB_USERNAME/REPO_NAME
```

*Other AI coding agents (including **Cursor**, **OpenCode**, **Windsurf**, **Antigravity**, and more) are automatically supported through the `npx skills add` command above.*

### 3. Manual Install for Claude Code
If you prefer to install it by hand for Claude Code, clone this repository and copy the folder into your skills directory:

**For a single project (`.claude/skills/SKILL_NAME/`):**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/REPO_NAME.git
mkdir -p .claude/skills/bite-size-study-guide
cp -r REPO_NAME/* .claude/skills/bite-size-study-guide/
```

**For all your projects (`~/.claude/skills/SKILL_NAME/`):**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/REPO_NAME.git
mkdir -p ~/.claude/skills/bite-size-study-guide
cp -r REPO_NAME/* ~/.claude/skills/bite-size-study-guide/
```

---

## How to Test That It Works

1. Install the skill using one of the commands above.
2. Open your AI agent and ask one of the example prompts:
   ```text
   Help me study about this topic: Mitosis
   ```
3. You can also test the included checker script directly in your terminal:
   ```bash
   python3 scripts/check_study_notes.py --demo
   ```

---

## Hacktoberfest

Built for the **Hacktoberfest** hackathon! Contributions, improvements, and new study templates are welcome—feel free to open an issue or submit a pull request.
