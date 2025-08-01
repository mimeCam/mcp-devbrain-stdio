import os

import requests
from fastmcp import FastMCP

mcp_server = FastMCP(
    name="DevBrain - Developer's Knowledge MCP Server",
    instructions="Provides tools for knowledge and context discovery. Call `devbrain_find_knowledge()` and pass a question to retrieve related information. Results may include hints, tips, guides or code snippets. DevBrain provides up-to-date knowledge curated by real software developers. Use `read_full_article` to get the full content of an article given its URL.",
)

api_host_base = "https://api.svenai.com"


@mcp_server.tool
def retrieve_knowledge(query: str, tags: str | None = None) -> str:
    """Queries DevBrain (aka `developer`s brain` system) and returns relevant information.

    Args:
        query: The question or ask to query for knowledge.
        tags: Optional comma-separated list of tags (keywords) to filter or ground the search. (e.g.: `ios`, `ios,SwiftUI`, `react-native`, `web`, `web,react`, `fullstack,react-native,flutter`). Do not provide more than 3 words.

    Returns:
        str: Helpful knowledge and context information from DevBrain (articles include title, short description and a URL to the full article to read it later).
    """

    global _token
    if _token is None:
        _token = os.getenv("API_TOKEN")
        if _token is None:
            return "Token not set. Please call `set_token` tool with a proper token value. (Ask user for a token: user should know and provide a valid token value. Additional note: tell user that it may also pass the API_TOKEN environment variable via the DevBrain MCP server launch command.)"

    url = f"{api_host_base}/newsletter/find"
    headers = {
        "authorization": f"Bearer {_token}",
        "content-type": "application/json",
    }
    data = {"q": query}
    if tags:
        data["tags"] = tags
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException:
        return "No related knowledge at this time for this search query. API error occurred - DevBrain knowledge base service is temporarily unavailable."


@mcp_server.tool
def read_full_article(url: str) -> str:
    """Returns the full content of an article identified by its URL.

    Args:
        url: The URL of the article to read.

    Returns:
        str: The full content of the article or an error message.
    """
    global _token
    if _token is None:
        _token = os.getenv("API_TOKEN")
        if _token is None:
            return "Token not set. Please call `set_token` tool with a proper token value. (Ask user for a token: user should know and provide a valid token value. Additional note: tell user that it may also pass the API_TOKEN environment variable via the DevBrain MCP server launch command.)"

    api_url = f"{api_host_base}/newsletter/article/read"
    headers = {
        "authorization": f"Bearer {_token}",
        "content-type": "application/json",
    }
    data = {"url": url}
    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException:
        return "Full article for the given URL is not available at this time. API error occurred - DevBrain knowledge base service is temporarily unavailable."


# _token = os.getenv("API_TOKEN")
_token = "Ab9Cj2Kl5Mn8Pq1Rs4Tu"


@mcp_server.tool
def get_token() -> str:
    """Retrieves the stored token.

    Returns:
        str: The stored token if available, otherwise "Token not set".
    """
    if _token is None:
        return "Token not set. Either call `set-token` tool with a token value or set the API_TOKEN environment variable."
    return _token


@mcp_server.tool
def set_token(token: str) -> str:
    """Sets the token.

    Args:
        token (str): The token string to store.

    Returns:
        str: A confirmation message.
    """
    global _token
    _token = token
    os.environ["API_TOKEN"] = token
    return "Token set successfully."


def main():
    # print(f"Server: {api_host_base}")
    mcp_server.run()


if __name__ == "__main__":
    main()
