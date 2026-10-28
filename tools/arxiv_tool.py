import arxiv
from pydantic import BaseModel, Field

class ArxivSearchQuery(BaseModel):
    query: str = Field(description="The search query for arxiv tool")
    max_results: int = Field(default=5 ,description="Max number of result per search")

def search_arxiv(query: str, max_results: int = 5) -> str:
    """Searches arxiv and returns metadata and abstract"""
    client = arxiv.Client()
    search = arxiv.Search(query= query, max_results=max_results, sort_by= arxiv.SortCriterion.Relevance)

    results = []

    try:
        for paper in client.results(search):
            results.append( f"Title: {paper.title}\n"
                f"Authors: {', '.join([a.name for a in paper.authors])}\n"
                f"Published: {paper.published}\n"
                f"URL: {paper.pdf_url}\n"
                f"Abstract: {paper.summary}\n"
                "---"
                )
        return "\n".join(results) if results else "No results found on arXiv."
    except Exception as e:
        print(f"Error searching using arXiv: {str(e)}")