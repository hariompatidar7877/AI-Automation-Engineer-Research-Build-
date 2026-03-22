"""
tools/sql_tool.py

SQL Tool for Autonomous Workflow Bot.

Acts as an MCP-compatible interface between AI agents
and the database layer.

Features:
- Safe query execution
- Automatic READ/WRITE detection
- HITL approval integration
- Schema access support
- Logging support

Author: Hariom Patidar
"""

from database.connection import db
from config import SENSITIVE_SQL_KEYWORDS, HITL_ENABLED
from approval.hitl_gate import request_approval
import logging


class SQLTool:
    """
    SQLTool enables agents to interact with database safely.
    Supports:
        - SELECT queries
        - INSERT / UPDATE
        - Restricted DELETE / DROP with approval
    """

    def __init__(self):
        self.db = db


    # =========================
    # QUERY TYPE DETECTOR
    # =========================

    def detect_query_type(self, query: str) -> str:
        """
        Detects whether query is READ or WRITE operation.
        """

        query_upper = query.strip().upper()

        if query_upper.startswith("SELECT"):
            return "READ"

        return "WRITE"


    # =========================
    # SENSITIVE QUERY DETECTOR
    # =========================

    def is_sensitive_query(self, query: str) -> bool:
        """
        Detects whether query contains sensitive SQL operations.
        """

        query_upper = query.upper()

        for keyword in SENSITIVE_SQL_KEYWORDS:
            if keyword in query_upper:
                return True

        return False


    # =========================
    # EXECUTE QUERY
    # =========================

    def execute(self, query: str):
        """
        Executes SQL query safely.

        Applies:
        - Query classification
        - Safety detection
        - HITL approval if required
        """

        query_type = self.detect_query_type(query)

        logging.info(f"SQLTool received query: {query}")

        # Check sensitive query
        if self.is_sensitive_query(query):

            logging.warning("Sensitive SQL detected")

            if HITL_ENABLED:

                approved = request_approval(query)

                if not approved:
                    logging.warning("Query rejected by HITL system")
                    return {
                        "status": "rejected",
                        "reason": "Human approval denied"
                    }

        # Execute query
        if query_type == "READ":
            result = self.db.execute_read_query(query)

            return {
                "status": "success",
                "type": "read",
                "rows": result
            }

        else:
            self.db.execute_write_query(query)

            return {
                "status": "success",
                "type": "write",
                "message": "Write query executed successfully"
            }


    # =========================
    # GET DATABASE SCHEMA
    # =========================

    def get_schema(self):
        """
        Returns full database schema.
        Used by SQL Agent for reasoning.
        """

        return self.db.get_full_schema()


    # =========================
    # GET TABLE LIST
    # =========================

    def get_tables(self):
        """
        Returns available database tables.
        """

        return self.db.get_tables()


# =========================
# GLOBAL TOOL INSTANCE
# =========================

sql_tool = SQLTool()