# CodeForge

An AI-powered coding assistant that runs in your terminal. It can read, write, and edit files, execute commands, and autonomously complete coding tasks.

Powered by **Google Gemini API** — free, fast, and capable.

## Features

- **File operations** — read, write, edit, and list files
- **Command execution** — run code, install packages, check outputs
- **Smart planning** — analyses requests before writing code
- **Auto test & fix** — runs your code and fixes errors
- **Interactive mode** — have a conversation with your coding agent
- **Single command mode** — one-shot tasks

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up your API key
cp .env.example .env
# Edit .env and add your Gemini API key

# Run in interactive mode
python main.py

# Or use a single prompt
python main.py "create a python script that prints fibonacci numbers"
```

## Requirements

- Python 3.10+
- Google Gemini API key (get one free at https://aistudio.google.com/apikey)

## Project Structure

```
codeforge/
├── main.py                 # CLI entry point
├── agent/
│   ├── core.py             # Main agent loop
│   ├── llm.py              # Gemini API client
│   ├── config.py           # Configuration
│   ├── prompts.py          # System prompts
│   └── tools/
│       ├── file_ops.py     # File operations
│       ├── shell.py        # Command execution
│       └── think.py        # Planning tool
├── requirements.txt
├── .env.example
└── .gitignore
```

## How It Works

1. You give the agent a task
2. The agent plans its approach
3. It creates files, writes code, and runs tests
4. If something fails, it fixes it
5. You get the final result
