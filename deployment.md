
# Publishing to pypi


### Step 1 - bump version
Increase version in `pyproject.toml`.
Remember to increment the version before running `deploy.sh`.


### Step 2 - rebuild
Use `uv build`. This is done by `deploy.sh`.


### Step 3 - publish to test-pypi first
Publish to `test` first and then test the package before publishing to main (prod) pypi site.

`
./deploy.sh test
`

Project's official test-pypi page: https://test.pypi.org/project/devbrain/

To run the test locally:
`
uvx --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ --from devbrain devbrain-stdio-server
`


### Step 4 - publish to prod-pypi
After it was tested on test-pypi you may publish to prod.

`
./deploy.sh prod
`


### Notes
Note: - you may need to clean uv's cache to ensure that it downloads bumped (updated) version like so: `uv cache clean` - `deploy.sh` does this automatically.
This is done by `deploy.sh`.
