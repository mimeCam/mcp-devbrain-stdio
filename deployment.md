
# Publishing to pypi


### Step 1 - bump version
Increase version in `pyproject.toml`.
Remember to increment the version before running `deploy.sh`.


### Step 2 - rebuild
Use `uv build`. This is done by `deploy.sh`.


### Step 3 - publish to test-pypi first
---
YO ignore test-pypi - do not upload to here as a pre-prod test - it does not work with uv/uvx correctly - or vice versa.
uvx pulls from prod no matter what.
Go straight to pypi (prod).
---
Publish to `test` first and then test the package before publishing to main (prod) pypi site.

`
./deploy.sh test
`

Project's official test-pypi page: https://test.pypi.org/project/devbrain/

To run the test locally:
```bash
uvx --force-reinstall --index-url https://test.pypi.org/simple/ --from devbrain devbrain-stdio-server
```
<!----extra-index-url https://pypi.org/simple/-->
Claude config:
```json
"devbrain": {
      "command": "uvx",
      "args": [
        "--force-reinstall",
        "--index-url",
        "https://test.pypi.org/simple/",
        "--extra-index-url",
        "https://pypi.org/simple/",
        "--from",
        "devbrain",
        "devbrain-stdio-server"
      ]
    }
```

When deployment to `test` env finished successfully show URL to the project on test.pypi: `https://test.pypi.org/project/devbrain`. Also output a testing command to let me know how to verify that just uploaded tool works correctly.


### Step 4 - publish to prod-pypi
After it was tested on test-pypi you may publish to prod.
`
./deploy.sh prod
`

To run locally:
```bash
uvx --from devbrain devbrain-stdio-server
```
to force new update download:
```bash
uvx --force-reinstall --from devbrain devbrain-stdio-server
 ```

When deployment to `prod` env finished successfully show URL to the project on test.pypi: `https://pypi.org/project/devbrain`. Also output a testing command to let user know how to verify that just uploaded tool works correctly.


### Notes
Note: - you may need to clean uv's cache to ensure that it downloads bumped (updated) version like so: `uv cache clean` - `deploy.sh` does this automatically.
This is done by `deploy.sh`.
