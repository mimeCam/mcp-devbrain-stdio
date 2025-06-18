# Project setup

This folder contains sources for devbrain mcp server (local on-client mcp server with stdio transport). It is build on top of [FastMCP python framework](https://gofastmcp.com/getting-started/quickstart)

`dev.sh` is used to start a development container. It usually needs to be launched once - do not do it - I will run this command myself once - only remind me about the command. You may look for docker logs for the container occasionally to confirm there are no errors during the build process.

`build.sh` is used to build docker image. I may ask you to do it occasionally.

To test a specific tool use `test.sh`. It pipes stdin/out/err so that you can send and receive MCP protocol data directly and test various MCP tools. Tests are located in `tests` folder. Execute `tests.sh` with a test name where test name is a name of the test file from `tests` folder.

See `deployment.md` for instructions on how to deploy the project to pypi.


# MCP docs

MCP protocol full documentation: https://modelcontextprotocol.io/llms-full.txt

Python MCP sdk: https://github.com/modelcontextprotocol/python-sdk

Simple guide to developing & testing MCP servers with LLMs: https://modelcontextprotocol.io/tutorials/building-mcp-with-llms

Servers composition: https://gofastmcp.com/servers/composition - this is a very important feature in FastMCP framework that allows to compose / chain / combine many tools together.
