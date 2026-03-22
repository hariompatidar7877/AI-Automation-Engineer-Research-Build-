"""
workflows/weekly_report_workflow.py

Weekly Report Workflow Orchestrator

Responsibilities:

- Trigger weekly analytics workflow
- Fetch business metrics via SQLAgent
- Generate structured reports via ReportAgent
- Maintain execution logs
- Support scheduler integration

Author: Hariom Patidar
"""

from agents.sql_agent import sql_agent
from agents.report_agent import report_agent
from config import DEFAULT_REPORT_FORMAT
from datetime import datetime
import logging


class WeeklyReportWorkflow:
    """
    Orchestrates full weekly report automation pipeline.
    """

    def __init__(self):
        self.sql_agent = sql_agent
        self.report_agent = report_agent


    # =========================
    # FETCH BUSINESS METRICS
    # =========================

    def fetch_metrics(self):
        """
        Collects weekly revenue metrics from SQLAgent.
        """

        logging.info("Fetching weekly business metrics")

        response = self.sql_agent.run("last week revenue")

        if response["status"] != "success":
            raise Exception("Failed to fetch weekly revenue")

        return response


    # =========================
    # GENERATE REPORT
    # =========================

    def generate_report(self, format_type=DEFAULT_REPORT_FORMAT):
        """
        Calls ReportAgent to generate weekly report.
        """

        logging.info("Generating weekly report file")

        report_response = report_agent.generate_weekly_report(
            format_type=format_type
        )

        if report_response["status"] != "success":
            raise Exception("Report generation failed")

        return report_response


    # =========================
    # EXECUTION LOGGER
    # =========================

    def log_workflow_execution(self, report_path):
        """
        Logs workflow execution metadata.
        """

        logging.info("Logging workflow execution details")

        execution_metadata = {
            "workflow": "weekly_report_workflow",
            "timestamp": datetime.now().isoformat(),
            "report_path": report_path
        }

        logging.info(f"Workflow execution metadata: {execution_metadata}")

        return execution_metadata


    # =========================
    # MAIN WORKFLOW PIPELINE
    # =========================

    def run(self, format_type=DEFAULT_REPORT_FORMAT):
        """
        Executes full automation workflow.

        Pipeline:

        Step 1: Fetch metrics
        Step 2: Generate report
        Step 3: Log execution
        """

        try:

            logging.info("Starting Weekly Report Workflow")

            # Step 1: Fetch metrics
            metrics = self.fetch_metrics()

            logging.debug(f"Metrics fetched: {metrics}")

            # Step 2: Generate report
            report_response = self.generate_report(format_type)

            report_path = report_response["file"]

            # Step 3: Log execution
            execution_log = self.log_workflow_execution(report_path)

            logging.info("Weekly workflow completed successfully")

            return {
                "status": "success",
                "report_file": report_path,
                "execution_log": execution_log
            }

        except Exception as e:

            logging.error(f"Workflow execution failed: {str(e)}")

            return {
                "status": "error",
                "message": str(e)
            }


# =========================
# GLOBAL WORKFLOW INSTANCE
# =========================

weekly_report_workflow = WeeklyReportWorkflow()