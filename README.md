# DevBrain MCP Server

This `devbrain` MCP server retrieves tech-related information, such as code snippets and links to developer blogs, based on developer questions.
It is like a web-search but tailors only curated knowledge from dev blogs and posts by software developers.

## Installation and Usage

1. Via `uv` or `uvx`. Install `uv` and `uvx` (if not installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
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
      ],
      "env": {
        "API_TOKEN": "Ab9Cj2Kl5Mn8Pq1Rs4Tu"
      }
    }
  }
}
```
Set your `API_TOKEN` in the `env` block.

[Claude is known to fail](https://gist.github.com/gregelin/b90edaef851f86252c88ecc066c93719) when working with `uv` and `uvx` binaries. See related: https://gist.github.com/gregelin/b90edaef851f86252c88ecc066c93719. If you encounter this error then run these commands in a Terminal:
```bash
sudo ln -s ~/.local/bin/uvx /usr/local/bin/uvx
sudo ln -s ~/.local/bin/uv /usr/local/bin/uv
```


## License
This project is released under the MIT License and is developed by mimeCam as an open-source initiative.
