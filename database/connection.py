"""
database/connection.py

Handles database connection lifecycle and query execution
for the Autonomous Workflow Bot.

Supports:
- SQLite (default)
- Extendable to PostgreSQL / MySQL later
- Query logging
- Schema inspection (for AI SQL Agent)

Author: Hariom Patidar
"""

import sqlite3
from contextlib import contextmanager
from typing import List, Dict, Any
from config import SQLITE_DB_PATH, LOG_FILE_PATH
import logging


# =========================
# LOGGER SETUP
# =========================

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# =========================
# DATABASE CONNECTION CLASS
# =========================

class DatabaseConnection:
    """
    Handles safe database connections and query execution.
    Used by SQLTool and SQLAgent.
    """

    def __init__(self, db_path=SQLITE_DB_PATH):
        self.db_path = db_path


    @contextmanager
    def connect(self):
        """
        Context manager for database connection.
        Ensures automatic closing.
        """

        connection = None

        try:
            connection = sqlite3.connect(self.db_path)
            connection.row_factory = sqlite3.Row
            yield connection

        except Exception as e:
            logging.error(f"Database connection error: {str(e)}")
            raise

        finally:
            if connection:
                connection.close()


    # =========================
    # READ QUERY EXECUTION
    # =========================

    def execute_read_query(self, query: str) -> List[Dict[str, Any]]:
        """
        Executes SELECT queries safely.
        Returns list of dictionaries.
        """

        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(query)

                rows = cursor.fetchall()

                result = [dict(row) for row in rows]

                logging.info(f"READ QUERY EXECUTED: {query}")

                return result

        except Exception as e:
            logging.error(f"Read query failed: {query}")
            raise e


    # =========================
    # WRITE QUERY EXECUTION
    # =========================

    def execute_write_query(self, query: str) -> None:
        """
        Executes INSERT / UPDATE / DELETE queries.
        """

        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(query)

                conn.commit()

                logging.info(f"WRITE QUERY EXECUTED: {query}")

        except Exception as e:
            logging.error(f"Write query failed: {query}")
            raise e


    # =========================
    # GET DATABASE TABLES
    # =========================

    def get_tables(self) -> List[str]:
        """
        Returns list of available tables.
        Useful for AI schema awareness.
        """

        query = """
        SELECT name
        FROM sqlite_master
        WHERE type='table';
        """

        result = self.execute_read_query(query)

        return [row["name"] for row in result]


    # =========================
    # GET TABLE SCHEMA
    # =========================

    def get_table_schema(self, table_name: str) -> List[Dict]:
        """
        Returns schema of a table.
        Critical for AI SQL generation.
        """

        query = f"PRAGMA table_info({table_name});"

        return self.execute_read_query(query)


    # =========================
    # GET FULL DATABASE SCHEMA
    # =========================

    def get_full_schema(self) -> Dict[str, List[Dict]]:
        """
        Returns schema for entire database.
        Used by SQL Agent reasoning engine.
        """

        schema = {}

        tables = self.get_tables()

        for table in tables:
            schema[table] = self.get_table_schema(table)

        return schema


# =========================
# GLOBAL DB INSTANCE
# =========================

db = DatabaseConnection()