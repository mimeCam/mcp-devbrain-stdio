import asyncio

from fastmcp import Client

client = Client("/app/src/mcp_server/server.py")


async def get_token_test_helper() -> str:
    """Calls the MCP get_token tool, parses its response, and returns the token string."""
    raw_response = await client.call_tool("get_token", {})
    extracted_token = None
    if (
        isinstance(raw_response, list)
        and raw_response
        and hasattr(raw_response[0], "text")
    ):
        extracted_token = raw_response[0].text
    elif isinstance(raw_response, str):
        extracted_token = raw_response
    return (
        extracted_token
        if extracted_token is not None
        else "Helper Error: unexpected None from get_token"
    )


async def set_token_test_helper(token_value: str) -> str:
    """Calls the MCP set_token tool, parses its response, and returns the confirmation string."""
    raw_response = await client.call_tool("set_token", {"token": token_value})
    extracted_response_text = None
    if (
        isinstance(raw_response, list)
        and raw_response
        and hasattr(raw_response[0], "text")
    ):
        extracted_response_text = raw_response[0].text
    elif isinstance(raw_response, str):
        extracted_response_text = raw_response
    return (
        extracted_response_text
        if extracted_response_text is not None
        else "Set Token Helper Error: Unexpected response format"
    )


async def test_token_management():
    print("--- Starting Token Management Test ---")
    async with client:
        try:
            # 1. Get initial token and assert
            initial_token = await get_token_test_helper()
            assert (
                initial_token
                == "Token not set. Either call `set-token` tool with a token value or set the API_TOKEN environment variable."
            ), (
                f"Main Assertion Failed: Initial token expected 'Token not set. Either call `set-token` tool with a token value or pass a token to the DevBrain MCP server during launch.', got '{initial_token}'"
            )

            # 2. Set a token and assert status
            test_value = "my_desired_token"
            set_status = await set_token_test_helper(test_value)
            assert set_status == "Token set successfully.", (
                f"Main Assertion Failed: Set status expected 'Token set successfully.', got '{set_status}'"
            )

            # 3. Get token after setting and assert value
            final_token = await get_token_test_helper()
            assert final_token == test_value, (
                f"Main Assertion Failed: Final token expected '{test_value}', but got '{final_token}'"
            )

            print("--- Token Management Tests Passed Successfully! ---")

        except Exception as e:
            print("--- !!! TOKEN MANAGEMENT TEST FAILED !!! ---")
            print(f"Error during token management test: {e}")
            raise


if __name__ == "__main__":
    asyncio.run(test_token_management())
