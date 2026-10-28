import trafilatura
import tiktoken
from pydantic import BaseModel, Field

class WebFetchSchema(BaseModel):
    url: str = Field(description="The url from where contents needs to be fetched")

def truncate_text(text: str, max_tokens: int = 8000) -> str:
    try:
        encoding = tiktoken.get_encoding("cl100k_base")
    except Exception:
        return text[:30000]

    tokens = encoding.encode(text)
    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]
        return encoding.decode(tokens) + '\n\n [Truncated Content due to excessive length...]'
    return text

def web_scrape(url: str) -> str:
    try:
        downloaded = trafilatura.fetch_url(url)
        if not downloaded:
            return f"Error: Couldn't load data from {url}"
        
        text = trafilatura.extract(downloaded, include_links=False, include_images=False)

        if not text:
            return f"Could not get text from {url}"

        return truncate_text(text)

    except Exception as e:
        return f"Error: fetching {url}: {str(e)}"