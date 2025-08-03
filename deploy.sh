#!/bin/bash

set -e # Exit immediately if aany command fails with a non-zero status.

VARIANT="$1"

if [ -z "$VARIANT" ]; then
    echo "Error: No variant provided. Usage: ./deploy.sh [prod|test]"
    exit 1
fi

if [ "$VARIANT" != "prod" ] && [ "$VARIANT" != "test" ]; then
    echo "Error: Invalid variant \'$VARIANT\'. Must be \'prod\' or \'test\'."
    exit 1
fi

# Clean the dist directory before building
echo "Cleaning dist directory..."
rm -rf dist/*

echo "Building project for $VARIANT environment..."
uv build

if [ "$VARIANT" == "test" ]; then
    echo "Publishing to Test PyPI..."
    # Use uvx uv-publish to leverage .pypirc for credentials
    uvx uv-publish --repository testpypi
elif [ "$VARIANT" == "prod" ]; then
    echo "Publishing to Production PyPI..."
    # Use uvx uv-publish for production as well, default repository is 'pypi'
    uvx uv-publish
fi

echo "Deployment for $VARIANT completed."

echo "Clearing uv cache so that it fetches the updated version later..."
uv cache clean
