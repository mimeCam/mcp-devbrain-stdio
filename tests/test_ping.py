# `ping` tool was disabled in src, so test below also disabled.


# import asyncio

# from fastmcp import Client

# client = Client("/app/src/mcp_server/server.py")


# async def test_ping_tool():
#     print("--- Starting Ping Test ---")
#     async with client:
#         try:
#             result = await client.call_tool("ping", {})
#             # Check if result is a list and contains TextContent objects
#             if (
#                 isinstance(result, list)
#                 and result
#                 and hasattr(result[0], "text")
#             ):
#                 assert result[0].text == "pong", (
#                     "Assertion Failed: Ping tool did not return 'pong'"
#                 )
#             else:
#                 raise AssertionError(
#                     f"Assertion Failed: Unexpected ping tool response format: {result}"
#                 )
#             print("--- Ping Test Passed Successfully! ---")

#         except Exception as e:
#             print(f"--- !!! PING TEST FAILED !!! ---")
#             print(f"Error calling ping tool: {e}")
#             raise


# if __name__ == "__main__":
#     asyncio.run(test_ping_tool())
