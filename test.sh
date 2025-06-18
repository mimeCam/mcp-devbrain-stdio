#!/bin/bash
#
# Expected parameter: <test_name> where test_name is a name of the test file from `tests/` folder.

PYTHON_IMAGE="python:3.10-slim-buster"
N="mcp_devbrain_local_test"

docker stop $N > /dev/null 2>&1;

docker run --rm -i -a stdin -a stdout -a stderr \
  -e FASTMCP_LOG_LEVEL=ERROR \
  -v "$(pwd)":/app \
  -w /app \
  --name="$N" \
  "$PYTHON_IMAGE" /app/test.in-docker.sh "$1"
