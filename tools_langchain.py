from langchain_core.tools import tool
from tools.arxiv_tool import search_arxiv
from tools.sandbox import run_python
from tools.tavily_tool import search_tavily
from tools.web_fetch import web_scrape

@tool
def arxiv_search(query: str) -> str:
    """Uses arxiv tool to gather information from academic research publications"""
    return search_arxiv(query)

@tool
def tavily_search(query: str) -> str:
    """Search the web for general context, articles, and recent news."""
    return search_tavily(query=query)

@tool
def web_fetch(url: str) -> str:
    """Fetch and extract clean text from a specific webpage or paper URL."""
    return web_scrape(url=url)

@tool
def python_sandbox(code: str) -> str:
    """Execute Python code in an isolated sandbox to process extracted metrics, calculate averages, or inspect tables. Use print() to output results."""
    return run_python(code=code)


TOOLS = [python_sandbox, web_fetch, tavily_search, arxiv_search]