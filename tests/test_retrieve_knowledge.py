import asyncio

from fastmcp import Client

# Assuming the main MCP server is in `server.py` in the parent directory.
client = Client("/app/src/mcp_server/server.py")


async def test_retrieve_knowledge_tool():
    print("Attempting to call 'retrieve_knowledge' tool...")
    async with client:
        try:
            result = await client.call_tool(
                "retrieve_knowledge", {"query": "algorithms"}
            )
            print(f"Retrieve Knowledge tool response: {result}")
        except Exception as e:
            print(f"Error calling retrieve_knowledge tool: {e}")
            raise


if __name__ == "__main__":
    asyncio.run(test_retrieve_knowledge_tool())
