#!/bin/bash

# This script runs INSIDE the Docker container

MODE="${1:-stdio}"

pip install -r requirements.txt > /dev/null 2>&1
pip install watchfiles > /dev/null 2>&1

echo "Starting DevBrain server in $MODE mode..."

if [ "$MODE" = "http" ]; then
    pip install uvicorn[standard] > /dev/null 2>&1
    echo "HTTP mode: http://0.0.0.0:8000/mcp"
    python src/mcp_server/server.py --transport http --host 0.0.0.0 --port 8000
else
    echo "STDIO mode"
    python src/mcp_server/server.py
fi
