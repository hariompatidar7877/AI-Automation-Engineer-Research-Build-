"""
mcp/mcp_registry.py

Model Context Protocol (MCP) Tool Registry

Responsibilities:

- Register available tools
- Provide tool discovery interface
- Enable dynamic agent-tool interaction
- Maintain centralized tool metadata
- Support scalable multi-agent architecture

Author: Hariom Patidar
"""

from tools.sql_tool import sql_tool
from config import REGISTERED_TOOLS
import logging


class MCPRegistry:
    """
    MCPRegistry acts as a centralized tool manager.

    Agents query this registry to:
    - discover tools
    - access capabilities
    - execute tools dynamically
    """

    def __init__(self):
        self.tools = {}

        self._register_default_tools()


    # =========================
    # REGISTER DEFAULT TOOLS
    # =========================

    def _register_default_tools(self):
        """
        Registers tools defined in config.
        """

        logging.info("Initializing MCP tool registry")

        if "sql_tool" in REGISTERED_TOOLS:
            self.register_tool("sql_tool", sql_tool)

        logging.info(f"Registered tools: {list(self.tools.keys())}")


    # =========================
    # REGISTER NEW TOOL
    # =========================

    def register_tool(self, tool_name: str, tool_instance):
        """
        Registers a tool dynamically.
        """

        self.tools[tool_name] = tool_instance

        logging.info(f"Tool registered: {tool_name}")


    # =========================
    # GET TOOL INSTANCE
    # =========================

    def get_tool(self, tool_name: str):
        """
        Returns tool instance if available.
        """

        tool = self.tools.get(tool_name)

        if not tool:
            logging.warning(f"Tool not found: {tool_name}")

        return tool


    # =========================
    # LIST AVAILABLE TOOLS
    # =========================

    def list_tools(self):
        """
        Returns list of registered tools.
        """

        return list(self.tools.keys())


    # =========================
    # EXECUTE TOOL
    # =========================

    def execute_tool(self, tool_name: str, *args, **kwargs):
        """
        Executes tool dynamically.

        Example:
            registry.execute_tool("sql_tool", query="SELECT * FROM sales")
        """

        tool = self.get_tool(tool_name)

        if not tool:
            return {
                "status": "error",
                "message": f"Tool '{tool_name}' not found"
            }

        if hasattr(tool, "execute"):
            return tool.execute(*args, **kwargs)

        return {
            "status": "error",
            "message": f"Tool '{tool_name}' has no execute() method"
        }


    # =========================
    # TOOL METADATA (FOR LLM USE)
    # =========================

    def describe_tools(self):
        """
        Returns metadata describing available tools.

        Useful for LLM tool-selection reasoning.
        """

        metadata = {}

        for name in self.tools:
            metadata[name] = {
                "capability": "database_query_execution"
                if name == "sql_tool"
                else "custom_tool"
            }

        return metadata


# =========================
# GLOBAL MCP REGISTRY INSTANCE
# =========================

mcp_registry = MCPRegistry()