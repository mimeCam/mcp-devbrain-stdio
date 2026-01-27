#!/bin/bash

# Usage: ./dev.sh [stdio|http]

PYTHON_IMAGE="python:3.10-slim-buster"
N="mcp_devbrain_local_dev"

MODE="${1:-stdio}"

docker stop "$N" > /dev/null 2>&1;
docker rm "$N" > /dev/null 2>&1;
sleep 1;

echo "Starting $N in $MODE mode..."

if [ "$MODE" = "http" ]; then
    PORT_MAPPING="-p 8000:8000"
else
    PORT_MAPPING=""
fi

docker run --rm -i -a stdin -a stdout -a stderr \
    $PORT_MAPPING \
    -v "$(pwd)":/app \
    -w /app \
    --name="$N" \
    "$PYTHON_IMAGE" /app/dev.in-docker.sh "$MODE"
