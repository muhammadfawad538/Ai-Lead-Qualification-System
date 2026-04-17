# manage-n8n

A WAT framework project for managing n8n workflows and automation.

## Architecture

This project follows the **WAT framework** (Workflows, Agents, Tools):

- **Workflows** (`workflows/`): Markdown SOPs defining what to do and how
- **Agents**: AI coordination layer (Claude) that reads workflows and executes tools
- **Tools** (`tools/`): Python scripts for deterministic execution

## Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

3. **Set up Google OAuth (if using Google services):**
   - Place `credentials.json` in the project root
   - First run will generate `token.json` automatically

## Directory Structure

```
workflows/          # Markdown SOPs
tools/              # Python execution scripts
.tmp/               # Temporary processing files (gitignored)
.env                # API keys and secrets (gitignored)
CLAUDE.md           # Agent instructions
```

## Usage

Work with Claude Code to execute workflows. Claude will:
1. Read the relevant workflow from `workflows/`
2. Execute tools from `tools/` in the correct sequence
3. Handle errors and update workflows as needed
4. Deliver outputs to cloud services

## Principles

- Local files are for processing only
- Deliverables go to cloud services (Google Sheets, Slides, etc.)
- Everything in `.tmp/` is disposable and regenerated as needed
- Workflows evolve based on learnings
