# Agentic Researcher

An autonomous AI research assistant that gathers information across academic papers and the web, extracts article content, and executes code in a sandboxed environment to synthesize comprehensive reports.

## Features

- **arXiv Search**: Search academic papers, preprints, and abstracts.
- **Tavily Search**: Real-time web search for articles and current events.
- **Web Fetch**: Scrape and extract clean text from web pages.
- **Python Sandbox**: Execute Python in an isolated E2B sandbox for data analysis and computation.
- **Two Implementations**: Graph-based workflow using **LangGraph** and a custom **manual agent loop**.

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *(or using [uv](https://github.com/astral-sh/uv): `uv sync`)*

2. **Configure environment variables**:
   Create a `.env` file from `.env.example`:
   ```env
   OPENROUTER_API_KEY="your-openrouter-key"
   TAVILY_API_KEY="your-tavily-key"
   E2B_API_KEY="your-e2b-key"
   ```

## Usage

Run the Streamlit application:

- **LangGraph Agent UI**:
  ```bash
  streamlit run app_agent.py
  ```

- **Manual Loop Agent UI**:
  ```bash
  streamlit run manual/app.py
  ```

