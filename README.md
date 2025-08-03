# DevBrain MCP Server

**Chat with your favorite newsletters** (coding, tech, founder).

# Audit

| <a href="https://glama.ai/mcp/servers/@mimeCam/mcp-devbrain-stdio">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@mimeCam/mcp-devbrain-stdio/badge" alt="DevBrain MCP server" /></a> | [![MseeP.ai Security Assessment Badge](https://mseep.net/pr/mimecam-mcp-devbrain-stdio-badge.png)](https://mseep.ai/app/mimecam-mcp-devbrain-stdio) |
|:--------:|:--------:|
|  | [![Verified on MseeP](https://mseep.ai/badge.svg)](https://mseep.ai/app/121bc8fb-67e7-4d57-b953-2d30b91cdfb5) |

# About

It is a newsletter-based MCP that searches for relevant code snippets, indie developer articles and blog posts so you don't have to hunt through generic web results again. Just ask LLM: "research <topic> on devbrain"

It's kind of like a web search, but specifically tuned for high-quality, developer-curated content. You can easily plug in your favorite newsletter to expand its knowledge base even further.

_**For example**, when you are implementing feature "A", DevBrain can pull related articles that would serve as a solid reference and a foundation for your implementation._

| <img width="400" alt="usage-claude" src="https://github.com/user-attachments/assets/f87b80ee-7829-43e8-9223-a02a38b4fd12" /> | [![](https://github.com/user-attachments/assets/a0525745-8435-4cce-aadb-418e6af81a21)](https://youtu.be/7UFtKqI9CjQ) |
|:--------:|:--------:|
| Claude app | Goose app (tap on an image to open utube) |

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
uvx --python ">=3.10" --from devbrain devbrain-stdio-server
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
        "--python", ">=3.10",
        "--force-reinstall",
        "--from",
        "devbrain",
        "devbrain-stdio-server"
      ]
    }
  }
}
```

Claude issues:
- Somehow it fails to get the latest version even when OS has it installed. Forcing an update (at least once) is required for Claude app. This is done with `--force-reinstall` arg.
- [Claude is known to fail](https://gist.github.com/gregelin/b90edaef851f86252c88ecc066c93719) when working with `uv` and `uvx` binaries. See related: https://gist.github.com/gregelin/b90edaef851f86252c88ecc066c93719. If you encounter this error then run these commands in a Terminal:
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

## Integration for Cline and other AI agents
Command to start DevBrain MCP in `stdio` mode:
```bash
uvx --python ">=3.10" --force-reinstall --from devbrain devbrain-stdio-server
```
and add this command to a config file of the AI agent (Cline or other).

Note that DevBrain requires Python 3.10+ support. Most systems have it installed. However VS Code (that Cline depends on) is shipped with Python 3.9. Use correct version of Python when running DevBrain MCP. A corrected version to launch DevBrain MCP looks like this:
```bash
uvx --python ">=3.10" --force-reinstall --from devbrain devbrain-stdio-server
```

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
        "svenai/mcp-devbrain-stdio:latest"
      ]
    }
  }
}
```
Test command to verify that docker container works correctly:
```bash
docker run -i --rm svenai/mcp-devbrain-stdio:latest
```


## License
This project is released under the MIT License and is developed by mimeCam as an open-source initiative.
