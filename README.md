# DevBrain MCP Server

This `devbrain` MCP server retrieves tech-related information, such as code snippets and links to developer blogs, based on developer questions.
It is like a web-search but tailors only curated knowledge from dev blogs and posts by software developers.

| <img width="400" alt="usage-claude" src="https://github.com/user-attachments/assets/f87b80ee-7829-43e8-9223-a02a38b4fd12" /> | <img width="400" alt="usage-goose" src="https://github.com/user-attachments/assets/a0525745-8435-4cce-aadb-418e6af81a21" /> |
|:--------:|:--------:|
| Claude app | Goose app |

DevBrain returns articles as short description + URL, you can then:
 - instruct LLM agent like `Claude` or `Goose` to fetch full contents of the articles using provided URLs
 - instruct LLM to implement a feature based on all or selected articles

## Installation and Usage

Via `uv` or `uvx`. Install `uv` and `uvx` (if not installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Example command to run MCP server in `stdio` mode:
```bash
uvx --from devbrain devbrain-stdio-server
```

To add `devbrain` to Claude's config, edit the file:
`~/Library/Application Support/Claude/claude_desktop_config.json`
and insert `devbrain` to existing `mcpServers` block like so:
```json
{
  "mcpServers": {
    "devbrain": {
      "command": "uvx",
      "args": [
        "--from",
        "devbrain",
        "devbrain-stdio-server"
      ]
    }
  }
}
```
Set your `API_TOKEN` in the `env` block.

[Claude is known to fail](https://gist.github.com/gregelin/b90edaef851f86252c88ecc066c93719) when working with `uv` and `uvx` binaries. See related: https://gist.github.com/gregelin/b90edaef851f86252c88ecc066c93719. If you encounter this error then run these commands in a Terminal:
```bash
sudo mkdir -p /usr/local/bin
```
```bash
sudo ln -s ~/.local/bin/uvx /usr/local/bin/uvx
```
```bash
sudo ln -s ~/.local/bin/uv /usr/local/bin/uv
```
and restart Claude.

To run via Docker first build an image with `build.sh` then add a config to Claude like so:
```json
{
  "mcpServers": {
    "devbrain": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "mcp-devbrain-stdio:my"
      ]
    }
  }
}
```
Test command:
```bash
docker run -i --rm mcp-devbrain-stdio:my
```

## License
This project is released under the MIT License and is developed by mimeCam as an open-source initiative.
