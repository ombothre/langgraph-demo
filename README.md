# LangGraph Basic & Router Examples

This repository demonstrates minimal LangGraph agent setups, runnable both locally and in [LangGraph Studio](https://smith.langchain.com/studio/). There are two main example projects: `simple` (basic assistant) and `router` (assistant with tool use and routing).

---

## Quick Start

### 1. Environment Variables

Copy the following into a `.env` file at the project root:

```
LANGCHAIN_API_KEY=<your_langchain_api_key>
LANGCHAIN_TRACING_V2=true
GEMINI_API_KEY=<your_gemini_api_key>
TAVILY_API_KEY=<your_tavily_api_key>
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

### 3. Run Locally

To run a project locally from the terminal:

```sh
cd <project>
python main.py
```

- Replace `<project>` with either `simple` or `router`.
- This will prompt for a user message and print the agent's response.

### 4. Run in LangGraph Studio

- The project is configured for Studio via [`langgraph.json`](langgraph.json).
- The entrypoint for Studio is `<project>/studio.py`, which exposes the graph as `graph`.
- Launch Studio with:

```sh
langgraph dev -c langgraph.json
```

- Then open [LangGraph Studio](https://smith.langchain.com/studio/) and select your graph.

---

## Folder Structure

Each project (`simple`, `router`) follows this structure:

```
<project>/
  main.py         # CLI entrypoint for local runs
  studio.py       # Entrypoint for LangGraph Studio (exports the graph)
  ai/
    graph.py      # Defines the agent's graph structure and flow
    llm.py        # LLM and tool bindings (uses Gemini via API key)
    prompts.py    # System prompt for the assistant
  config/
    settings.py   # Loads environment variables (e.g., Gemini API key)
  models/
    state.py      # Defines the agent's state (messages)
    node.py       # (router only) Node enum for graph nodes
  services/
    helpers.py    # Utility functions for message handling
    tools.py      # (router only) Example tool functions (add, product)
```

- `simple/` is a minimal assistant.
- `router/` demonstrates tool use and conditional routing.

---

## How it Works

- **simple**: A basic assistant that responds to user queries using Gemini LLM.
- **router**: An assistant that can use tools (like add/product) and routes between LLM/tool nodes based on the message.

- The graph logic is defined in `<project>/ai/graph.py`.
- Tools (for `router`) are in `<project>/services/tools.py`.
- State is managed in `<project>/models/state.py`.
- For local runs, use `<project>/main.py`.
- For Studio, use `<project>/studio.py`.

---

## Configuration

- The project is configured for LangGraph Studio via [`langgraph.json`](langgraph.json).
- All environment variables are loaded from `.env`.

---

## References

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)