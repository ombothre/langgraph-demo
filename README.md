# LangGraph Basic Example

This repository demonstrates a minimal LangGraph agent setup, runnable both locally and in [LangGraph Studio](https://smith.langchain.com/studio/).

## Quick Start

### 1. Environment Variables

Copy the following into a `.env` file at the project root:

```
LANGCHAIN_API_KEY=<>
LANGCHAIN_TRACING_V2=true
GEMINI_API_KEY=<>
TAVILY_API_KEY=<>
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

### 3. Run Locally

To run any project locally from the terminal:

```sh
python <project>_run.py
```

- This will prompt for a user message and print the agent's response.

### 4. Run in LangGraph Studio

- The project is configured for Studio via [`langgraph.json`](langgraph.json).
- The entrypoint for Studio is [`studio.py`] , which exposes the graph as `graph`.
- Launch Studio with:

```sh
langgraph dev
```

- Then open [LangGraph Studio](https://smith.langchain.com/studio/) and select your graph.

---

## Folder Structure

- **<project>/**
  - `main.py` — CLI entrypoint for local runs.
  - `studio.py` — Entrypoint for LangGraph Studio (exports the graph).
  - **ai/**
    - `graph.py` — Defines the agent's graph structure and flow.
    - `llm.py` — LLM and tool bindings (uses Gemini via API key).
    - `prompts.py` — System prompt for the assistant.
  - **config/**
    - `settings.py` — Loads environment variables (e.g., Gemini API key).
  - **models/**
    - `state.py` — Defines the agent's state (messages).
  - **services/**
    - `helpers.py` — Utility functions for message handling.
    - `tools.py` — Example tool functions (add, product).
- **<project>_run.py** - To run that project locally

---

## Configuration

- The project is configured for LangGraph Studio via [`langgraph.json`](langgraph.json).
- All environment variables are loaded from `.env`.

---

## References

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)