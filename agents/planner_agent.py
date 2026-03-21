"""
agents/planner_agent.py

Planner Agent for Autonomous Workflow Bot.

Responsibilities:

- Understand user intent
- Route tasks to correct agents
- Trigger workflows
- Coordinate multi-agent execution
- Maintain structured execution pipeline

Acts as the central orchestration layer.

Author: Hariom Patidar
"""

from agents.sql_agent import sql_agent
import logging


class PlannerAgent:
    """
    PlannerAgent routes user requests to the correct agent
    or workflow based on detected intent.
    """

    def __init__(self):
        self.sql_agent = sql_agent


    # =========================
    # INTENT DETECTOR
    # =========================

    def detect_intent(self, user_prompt: str) -> str:
        """
        Detects user intent using rule-based classification.

        Future upgrade:
        Replace with LLM intent classification.
        """

        prompt = user_prompt.lower()

        if "revenue" in prompt:
            return "sql_query"

        elif "customer" in prompt:
            return "sql_query"

        elif "report" in prompt:
            return "generate_report"

        elif "weekly business report" in prompt:
            return "weekly_workflow"

        else:
            return "unknown"


    # =========================
    # ROUTE TASK
    # =========================

    def route_task(self, intent: str, user_prompt: str):
        """
        Routes execution to appropriate agent/workflow.
        """

        logging.info(f"Routing task with intent: {intent}")

        if intent == "sql_query":
            return self.sql_agent.run(user_prompt)

        elif intent == "generate_report":
            return {
                "status": "pending",
                "message": "Report Agent will handle this task (next module)."
            }

        elif intent == "weekly_workflow":
            return {
                "status": "pending",
                "message": "Weekly workflow module will handle this task."
            }

        else:
            return {
                "status": "error",
                "message": "Unable to determine intent."
            }


    # =========================
    # MAIN EXECUTION PIPELINE
    # =========================

    def run(self, user_prompt: str):
        """
        Full planning pipeline:

        Step 1: Detect intent
        Step 2: Route task
        Step 3: Execute selected agent/workflow
        """

        try:

            logging.info(f"PlannerAgent received input: {user_prompt}")

            # Step 1: Detect intent
            intent = self.detect_intent(user_prompt)

            logging.info(f"Detected intent: {intent}")

            # Step 2: Route task
            result = self.route_task(intent, user_prompt)

            return {
                "status": "success",
                "intent": intent,
                "response": result
            }

        except Exception as e:

            logging.error(f"PlannerAgent failed: {str(e)}")

            return {
                "status": "error",
                "message": str(e)
            }


# =========================
# GLOBAL PLANNER INSTANCE
# =========================

planner_agent = PlannerAgent()