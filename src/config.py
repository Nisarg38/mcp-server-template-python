"""Configuration settings for the MCP server."""

from typing import Any, Dict, Optional


class ServerConfig:
    """Server configuration settings."""

    def __init__(self):
        """Initialize with default configuration."""
        self.name: str = "MCP Server Template"
        self.description: str = "A boilerplate for Model Context Protocol servers in Python"
        self.version: str = "0.1.0"
        self.port: int = 8080
        self.host: str = "0.0.0.0"
        self.debug: bool = False
        self.log_level: str = "info"
        self.metadata: Dict[str, Any] = {
            "github": "https://github.com/yourusername/mcp-server-template-python",
        }

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "port": self.port,
            "host": self.host,
            "debug": self.debug,
            "log_level": self.log_level,
            "metadata": self.metadata,
        }


# Global configuration instance
config = ServerConfig() 