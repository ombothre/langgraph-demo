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

To run the agent locally from the terminal:

```sh
python main.py
```

- This will prompt for a user message and print the agent's response.

### 4. Run in LangGraph Studio

- The project is configured for Studio via [`langgraph.json`](langgraph.json).
- The entrypoint for Studio is [`studio.py`](simple/studio.py), which exposes the graph as `graph`.
- Launch Studio with:

```sh
langgraph dev
```

- Then open [LangGraph Studio](https://smith.langchain.com/studio/) and select your graph.

---

## Folder Structure

- **simple/**
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

---

## How it Works

- The agent is a simple tool-using assistant.
- The graph is defined in [`simple/ai/graph.py`](simple/ai/graph.py).
- Tools are defined in [`simple/services/tools.py`](simple/services/tools.py) and bound to the LLM in [`simple/ai/llm.py`](simple/ai/llm.py).
- The state is managed as a list of messages ([`simple/models/state.py`](simple/models/state.py)).
- For local runs, [`simple/main.py`](simple/main.py) takes user input and prints the response.
- For Studio, [`simple/studio.py`](simple/studio.py) exposes the graph for the UI.

---

## Configuration

- The project is configured for LangGraph Studio via [`langgraph.json`](langgraph.json).
- All environment variables are loaded from `.env`.

---

## References

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
-