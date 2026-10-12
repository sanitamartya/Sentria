# Sentria

Sentria is an AI Engineering & Operations System designed to understand software systems, investigate engineering problems using evidence, use controlled tools, verify outcomes, and keep humans in control of consequential actions.

## Current Status

The project is in its initial foundation phase.

Currently implemented:

- FastAPI application
- Basic root endpoint
- Health endpoint
- Initial configuration using Pydantic Settings
- Automated health endpoint test

## Local Development

Activate the Python virtual environment:

```bash
source .venv/bin/activate
```

Install the project in editable mode:

```bash
python -m pip install -e .
```

Run the development server:

```bash
uvicorn sentria.main:app --reload
```

Health endpoint:

`http://127.0.0.1:8000/health`

Run tests:

```bash
python -m pytest -v
```

## Project Principles

- Evidence-driven engineering
- Verification before claiming success
- Human approval for consequential actions
- Simple, modular architecture
- Incremental implementation and testing
