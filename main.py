"""
main.py

Application entry point for Autonomous Workflow Bot.

Responsibilities:

- Initialize FastAPI server
- Register API routes
- Boot MCP registry
- Enable logging system
- Prepare workflow automation environment

Author: Hariom Patidar
"""

from fastapi import FastAPI
from api.routes import router
from config import API_HOST, API_PORT
from mcp.mcp_registry import mcp_registry
import logging


# =========================
# LOGGING CONFIGURATION
# =========================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# =========================
# FASTAPI APPLICATION INIT
# =========================

app = FastAPI(
    title="Autonomous Workflow Bot",
    description="Agentic AI automation system with MCP, SQL agents, HITL safety, and workflow orchestration.",
    version="1.0.0"
)


# =========================
# REGISTER ROUTES
# =========================

app.include_router(router)


# =========================
# STARTUP EVENT
# =========================

@app.on_event("startup")
def startup_event():
    """
    Executes when application starts.

    Initializes:
    - MCP registry
    - logging confirmation
    """

    logging.info("Starting Autonomous Workflow Bot API...")

    available_tools = mcp_registry.list_tools()

    logging.info(f"MCP tools loaded: {available_tools}")

    logging.info("System startup complete 🚀")


# =========================
# SHUTDOWN EVENT
# =========================

@app.on_event("shutdown")
def shutdown_event():
    """
    Executes when application stops.
    """

    logging.info("Shutting down Autonomous Workflow Bot API...")


# =========================
# LOCAL DEVELOPMENT RUNNER
# =========================

if __name__ == "__main__":
    import uvicorn

    logging.info(f"Launching server at http://{API_HOST}:{API_PORT}")

    uvicorn.run(
        "main:app",
        host=API_HOST,
        port=API_PORT,
        reload=True
    )