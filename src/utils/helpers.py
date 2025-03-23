"""Helper utilities for the MCP server."""

import importlib.metadata
import logging
import os
import sys
from typing import Optional


def get_version() -> str:
    """Get the package version from metadata."""
    try:
        return importlib.metadata.version("mcp-server-template")
    except importlib.metadata.PackageNotFoundError:
        return "0.1.0"  # Default version if package not installed


def setup_logging(log_level: Optional[str] = None) -> None:
    """Set up logging configuration.
    
    Args:
        log_level: The log level to use (debug, info, warning, error, critical).
            If None, uses the LOG_LEVEL environment variable or defaults to 'info'.
    """
    if log_level is None:
        log_level = os.environ.get("LOG_LEVEL", "info").lower()
    
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        numeric_level = logging.INFO
    
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    
    # Adjust third-party library logging levels
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("fastapi").setLevel(logging.WARNING)


def get_server_url(host: str, port: int, https: bool = False) -> str:
    """Get the server URL based on host and port.
    
    Args:
        host: The host name or IP address.
        port: The port number.
        https: Whether to use HTTPS instead of HTTP.
        
    Returns:
        The complete server URL.
    """
    protocol = "https" if https else "http"
    host_str = host if host != "0.0.0.0" else "localhost"
    return f"{protocol}://{host_str}:{port}" 