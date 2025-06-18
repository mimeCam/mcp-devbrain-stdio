# DevBrain MCP Server

This `devbrain` MCP server retrieves tech-related information, such as code snippets and links to developer blogs, based on developer questions.
It is like a web-search but tailors only curated knowledge from dev blogs and posts by software developers.

## Installation and Usage

1. Via `uv` or `uvx`
Assuming `uv` and `uvx` installed:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

[Claude app often fails](https://gist.github.com/gregelin/b90edaef851f86252c88ecc066c93719) to find `uv` and `uvx` binaries. See related: https://gist.github.com/gregelin/b90edaef851f86252c88ecc066c93719
If you encounter this error then run these:
```bash
sudo ln -s ~/.local/bin/uvx /usr/local/bin/uvx
sudo ln -s ~/.local/bin/uv /usr/local/bin/uv
```

To add `devbrain` to Claude's config, edit:
`~/Library/Application Support/Claude/claude_desktop_config.json`


## License
This project is released under the MIT License and is developed by mimeCam as an open-source initiative.
