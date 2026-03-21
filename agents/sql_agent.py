"""
agents/sql_agent.py

SQL Agent responsible for:

- Understanding natural language requests
- Inspecting database schema
- Generating SQL queries
- Executing queries via SQLTool
- Returning structured results

Designed for integration with MCP architecture.

Author: Hariom Patidar
"""

from tools.sql_tool import sql_tool
import logging


class SQLAgent:
    """
    SQLAgent converts user/business prompts into SQL queries
    and executes them safely through SQLTool.
    """

    def __init__(self):
        self.sql_tool = sql_tool


    # =========================
    # LOAD DATABASE SCHEMA
    # =========================

    def get_schema_context(self):
        """
        Retrieves database schema for reasoning.
        """

        schema = self.sql_tool.get_schema()

        logging.info("Schema loaded successfully")

        return schema


    # =========================
    # SIMPLE RULE-BASED SQL GENERATOR
    # (LLM REPLACEABLE MODULE)
    # =========================

    def generate_sql(self, user_prompt: str) -> str:
        """
        Converts user request into SQL query.

        Currently rule-based.
        Can be replaced with LLM later.
        """

        prompt = user_prompt.lower()

        # Example rules (expandable)

        if "total revenue" in prompt:
            return "SELECT SUM(revenue) AS total_revenue FROM sales;"

        elif "last week revenue" in prompt:
            return """
            SELECT SUM(revenue) AS weekly_revenue
            FROM sales
            WHERE date >= DATE('now', '-7 day');
            """

        elif "revenue by region" in prompt:
            return """
            SELECT region, SUM(revenue) AS revenue
            FROM sales
            GROUP BY region;
            """

        elif "show all customers" in prompt:
            return "SELECT * FROM customers;"

        else:
            raise ValueError(
                "Unable to generate SQL query for this request."
            )


    # =========================
    # EXECUTE GENERATED SQL
    # =========================

    def execute_query(self, sql_query: str):
        """
        Sends generated SQL query to SQLTool.
        """

        logging.info(f"Executing SQL query: {sql_query}")

        result = self.sql_tool.execute(sql_query)

        return result


    # =========================
    # FULL PIPELINE EXECUTION
    # =========================

    def run(self, user_prompt: str):
        """
        End-to-end SQL reasoning pipeline.

        Steps:
        1. Load schema
        2. Generate SQL
        3. Execute query
        4. Return structured result
        """

        try:

            logging.info(f"SQLAgent received prompt: {user_prompt}")

            # Step 1: Schema awareness
            schema = self.get_schema_context()

            logging.debug(f"Schema context: {schema}")

            # Step 2: Generate SQL
            sql_query = self.generate_sql(user_prompt)

            logging.info(f"Generated SQL: {sql_query}")

            # Step 3: Execute query
            result = self.execute_query(sql_query)

            return {
                "status": "success",
                "query": sql_query,
                "result": result
            }

        except Exception as e:

            logging.error(f"SQLAgent execution failed: {str(e)}")

            return {
                "status": "error",
                "message": str(e)
            }


# =========================
# GLOBAL AGENT INSTANCE
# =========================

sql_agent = SQLAgent()