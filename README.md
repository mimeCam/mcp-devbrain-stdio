# DevBrain MCP Server

**Chat with your favorite newsletters** (coding, tech, business).

DevBrain pulls up relevant code snippets, indie developer articles, and blog posts, all based on what you're looking for.

It's kind of like a web search, but specifically tuned for high-quality, developer-curated content. You can easily plug in your favorite newsletters to expand its knowledge base even further.

_**For example**, when you are implementing feature "A", DevBrain can pull related articles that would serve as a solid reference and a foundation for your implementation._

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

## Use in Claude

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

## Docker integration

You can run this MCP as a Docker container in STDIO mode. First build an image with `build.sh`. Then add a config to Claude like so:
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
Test command to verify that docker container works correctly:
```bash
docker run -i --rm mcp-devbrain-stdio:my
```

## License
This project is released under the MIT License and is developed by mimeCam as an open-source initiative.
