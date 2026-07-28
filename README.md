# Educational Skills

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/) [![AI Tutor](https://img.shields.io/badge/project-AI%20Math%20Tutor-orange)](https://github.com/)

Educational Skills is an interactive mathematics learning project that combines Python-based tutors with AI-driven guidance. It helps students explore topics such as fractions, algebra, statistics, geometry, percentages, ratios, and more through guided lessons and quiz-style practice.

## What this project does

This repository contains a collection of math tutoring scripts and supporting skill definitions. The main experience is powered by [main.py](main.py), which launches a conversational tutor that can direct learners to the right topic and start the relevant lesson.

Key capabilities include:

- Topic-based tutoring for elementary math and algebra
- Interactive quiz-style practice for students
- AI-assisted explanations and lesson routing through the skills system
- Visual and statistical helpers for selected topics

## Why it is useful

The project is designed for educators, learners, and developers who want a lightweight way to:

- Practice math concepts in a guided, interactive format
- Explore a modular set of educational scripts
- Extend the tutor with new skills or lesson modules
- Use the repository as a teaching demo or prototype for AI-assisted education

## Project structure

A quick overview of the main parts of the repository:

- [main.py](main.py) – entry point for the main tutor experience
- [elementary_algebra.py](elementary_algebra.py) – elementary algebra tutor
- [statistics_tutor.py](statistics_tutor.py) – statistics tutor and quiz flow
- [skills](skills) – skill documents used by the AI tutor
- [demo](demo) – demonstration and test materials

## Getting started

### Prerequisites

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/) for dependency and environment management

### Installation

Follow these steps to set up the project locally.

1. Install uv

   Install uv from PyPI using Python:

   ```bash
   pipx install uv
   ```

   Verify the installation:

   ```bash
   uv --version
   ```

   For more details, see the official uv installation guide: https://docs.astral.sh/uv/getting-started/installation/

2. Install Ollama and a model for the AI tutor

   The project uses the Deep Agents integration with Ollama. Install Ollama from https://ollama.com/download

   If you prefer a different model, update the `model=` value in [main.py](main.py) and [elementary_algebra.py](elementary_algebra.py) to match your local setup.

3. Install the project dependencies

   From the repository root, run:

   ```bash
    uv init
    uv add deepagents
    uv sync
   ```

   This installs the dependencies declared in [pyproject.toml](pyproject.toml), including the Deep Agents package.

4. Set up your API keys

   ```bash
   # Local: Ollama must be running on your machine
    # Cloud: Set your Ollama API key for hosted inference
    export OLLAMA_API_KEY="your-api-key"
    export TAVILY_API_KEY="your-tavily-api-key"
   ```

   The quickstart reference for this setup is here: https://docs.langchain.com/oss/python/deepagents/quickstart#ollama

5. Run the tutor

   ```bash
   uv run main.py
   ```

### Run the main tutor

```bash
uv run main.py
```

You will be prompted to choose a topic. The tutor will then launch the appropriate lesson or exercise.

### Run a specific lesson directly

You can also launch an individual lesson script directly, for example:

```bash
uv run percentage.py
```

## Usage examples

The main experience is conversational. After starting the app, enter a topic such as:

- percentages
- fractions
- algebra
- statistics
- pythagorean
- angles

The tutor will route you to the right module and begin the lesson flow.

## Getting help

If you want to understand how the tutoring flow works, start with:

- [main.py](main.py)
- [skills](skills)
- [demo](demo)

For topic-specific guidance, inspect the corresponding lesson script and its skill documentation in [skills](skills).

## Latest skill
The following skills are latest skills:
-  angle
-  pythagorean
-  statistics_tutor

## Contributing

Contributions are welcome. If you would like to improve the tutor, add a new lesson, or refine the AI prompts, please open an issue or submit a pull request with a clear description of the change.

This project is maintained by the repository contributors and is intended as an educational and experimental codebase.
