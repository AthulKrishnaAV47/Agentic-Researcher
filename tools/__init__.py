from arxiv_tool import ArxivSearchSchema, search_arxiv
from tavily_tool import TavilySearchSchema, search_tavily
from web_fetch import WebFetchSchema, web_scrape
from sandbox import SandBoxSchema, run_python

AVAILABLE_TOOLS = {
    "arxiv_search":{
        "function": search_arxiv,
        "schema": ArxivSearchSchema,
        "description": "Search arXiv for academic papers and abstracts."
    },
    "python_sandbox":{
            "function": run_python,
            "schema": SandBoxSchema,
            "description": "Run Python code to analyze data, compute statistics, or format text."
    },
    "tavily_search":{
            "function": search_tavily,
            "schema": TavilySearchSchema,
            "description": "Search the web for general context and recent news."
    },
    "web_fetch":{
            "function": web_scrape,
            "schema": WebFetchSchema,
            "description":  "Fetch and extract clean article text from a URL."
    }
}
