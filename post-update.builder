#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
if [[ "${TRACE-0}" == "1" ]]; then
    set -o xtrace
fi

cd "$(dirname "$0")"

VERSION="1.1.9"

IMAGE_NAME_ROOT="svenai/mcp-devbrain-stdio"
IMAGE_NAME_VERSION="$IMAGE_NAME_ROOT:$VERSION"
IMAGE_NAME_LATEST="$IMAGE_NAME_ROOT:latest"

docker buildx use rc-builder

docker buildx build --platform=linux/amd64,linux/arm64 \
   --provenance=false \
	-f "Dockerfile" \
	--push \
	-t $IMAGE_NAME_VERSION \
	-t $IMAGE_NAME_LATEST \
	.
    # . > /dev/null

echo "Finished building docker image: $IMAGE_NAME_VERSION"
