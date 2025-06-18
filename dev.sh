#!/bin/bash

PYTHON_IMAGE="python:3.10-slim-buster"
N="mcp_devbrain_local_dev"

docker stop "$N" > /dev/null 2>&1;
docker rm "$N" > /dev/null 2>&1;
sleep 2;

docker run --rm -i -a stdin -a stdout -a stderr \
  -v "$(pwd)":/app \
  -w /app \
  --name="$N" \
  "$PYTHON_IMAGE" /app/dev.in-docker.sh
