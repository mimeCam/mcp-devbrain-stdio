#!/bin/bash

# This script runs INSIDE the Docker container

pip install -r requirements.txt > /dev/null 2>&1
pip install watchfiles > /dev/null 2>&1

echo "Starting FastMCP server..."
watchfiles python src/mcp_server/server.py src
