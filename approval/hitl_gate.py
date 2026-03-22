"""
approval/hitl_gate.py

Human-in-the-Loop (HITL) approval system
for sensitive operations in Autonomous Workflow Bot.

Features:
- Approval queue
- CLI approval interface
- Audit logging
- Extendable for dashboard/API approval

Author: Hariom Patidar
"""

import json
import os
from datetime import datetime
from config import LOGS_DIR

# =========================
# APPROVAL LOG FILE
# =========================

APPROVAL_LOG_FILE = os.path.join(LOGS_DIR, "approval_logs.json")


# =========================
# ENSURE LOG FILE EXISTS
# =========================

if not os.path.exists(APPROVAL_LOG_FILE):
    with open(APPROVAL_LOG_FILE, "w") as f:
        json.dump([], f)


# =========================
# LOG APPROVAL EVENT
# =========================

def log_approval_event(query: str, approved: bool):
    """
    Stores approval decision in audit logs.
    """

    event = {
        "timestamp": datetime.now().isoformat(),
        "query": query,
        "approved": approved
    }

    with open(APPROVAL_LOG_FILE, "r+") as f:
        data = json.load(f)
        data.append(event)
        f.seek(0)
        json.dump(data, f, indent=4)


# =========================
# CLI APPROVAL INTERFACE
# =========================

def cli_approval_prompt(query: str) -> bool:
    """
    CLI-based approval system.

    Returns True if approved
    Returns False if rejected
    """

    print("\n⚠️  HUMAN APPROVAL REQUIRED")
    print("Sensitive operation detected:\n")
    print(query)
    print("\nApprove execution? (yes/no): ", end="")

    decision = input().strip().lower()

    return decision == "yes"


# =========================
# MAIN APPROVAL ENTRYPOINT
# =========================

def request_approval(query: str) -> bool:
    """
    Main approval gateway used by tools.

    Future versions can route approval to:
    - Web dashboard
    - Slack bot
    - Email approval
    - Mobile notification

    Currently uses CLI approval.
    """

    approved = cli_approval_prompt(query)

    log_approval_event(query, approved)

    return approved


# =========================
# FETCH APPROVAL HISTORY
# =========================

def get_approval_history():
    """
    Returns all past approval decisions.
    Useful for dashboards / audits.
    """

    with open(APPROVAL_LOG_FILE, "r") as f:
        return json.load(f)