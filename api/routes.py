"""
api/routes.py

FastAPI route definitions for Autonomous Workflow Bot.

Responsibilities:

- Accept user prompts
- Trigger planner agent
- Execute weekly workflow
- Retrieve generated reports
- Fetch approval logs

Author: Hariom Patidar
"""

from fastapi import APIRouter
from agents.planner_agent import planner_agent
from workflows.weekly_report_workflow import weekly_report_workflow
from approval.hitl_gate import get_approval_history
from config import REPORTS_DIR
from pathlib import Path
import logging


router = APIRouter()


# =========================
# HEALTH CHECK ENDPOINT
# =========================

@router.get("/")
def health_check():
    """
    Basic API health check endpoint.
    """

    return {
        "status": "running",
        "service": "Autonomous Workflow Bot API"
    }


# =========================
# PROMPT EXECUTION ENDPOINT
# =========================

@router.post("/query")
def execute_prompt(prompt: str):
    """
    Sends user prompt to PlannerAgent.

    Example:
        POST /query?prompt=last week revenue
    """

    logging.info(f"Received prompt: {prompt}")

    response = planner_agent.run(prompt)

    return response


# =========================
# RUN WEEKLY WORKFLOW
# =========================

@router.post("/workflow/weekly-report")
def run_weekly_report(format_type: str = "txt"):
    """
    Triggers full weekly report automation workflow.

    Example:
        POST /workflow/weekly-report?format_type=json
    """

    logging.info("Weekly workflow triggered via API")

    response = weekly_report_workflow.run(format_type=format_type)

    return response


# =========================
# LIST GENERATED REPORTS
# =========================

@router.get("/reports")
def list_reports():
    """
    Returns list of generated report files.
    """

    reports_path = Path(REPORTS_DIR)

    report_files = [
        file.name
        for file in reports_path.iterdir()
        if file.is_file()
    ]

    return {
        "status": "success",
        "reports": report_files
    }


# =========================
# FETCH APPROVAL HISTORY
# =========================

@router.get("/approvals")
def approval_logs():
    """
    Returns approval history for HITL system.
    """

    logging.info("Fetching approval history")

    history = get_approval_history()

    return {
        "status": "success",
        "approvals": history
    }