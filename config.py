"""
config.py

Central configuration file for the Autonomous Workflow Bot.
All environment-level settings are defined here.

Author: Hariom Patidar
Role: AI Automation Engineer Project
"""

import os
from pathlib import Path


# =========================
# BASE DIRECTORY SETTINGS
# =========================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "database"
REPORTS_DIR = BASE_DIR / "reports"
LOGS_DIR = BASE_DIR / "logs"

# Ensure required folders exist
REPORTS_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)


# =========================
# DATABASE CONFIGURATION
# =========================

DATABASE_TYPE = "sqlite"

SQLITE_DB_PATH = DATA_DIR / "business_data.db"


# =========================
# MCP CONFIGURATION
# =========================

MCP_ENABLED = True

REGISTERED_TOOLS = [
    "sql_tool",
    "file_tool",
    "report_tool"
]


# =========================
# SAFETY CONFIGURATION
# =========================

HITL_ENABLED = True

SENSITIVE_SQL_KEYWORDS = [
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "UPDATE"
]


# =========================
# REPORT CONFIGURATION
# =========================

DEFAULT_REPORT_FORMAT = "txt"

SUPPORTED_REPORT_FORMATS = [
    "txt",
    "csv",
    "json"
]


# =========================
# AGENT CONFIGURATION
# =========================

AGENT_MODE = "autonomous"

MAX_RETRY_ATTEMPTS = 3


# =========================
# LOGGING CONFIGURATION
# =========================

LOG_FILE_PATH = LOGS_DIR / "execution.log"

LOG_LEVEL = "INFO"


# =========================
# API CONFIGURATION
# =========================

API_HOST = "127.0.0.1"
API_PORT = 8000


# =========================
# SCHEDULER CONFIGURATION
# =========================

ENABLE_WEEKLY_AUTOMATION = True

SCHEDULE_DAY = "MONDAY"
SCHEDULE_TIME = "09:00"