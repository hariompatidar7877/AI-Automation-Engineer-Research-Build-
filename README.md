<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&height=260&text=Autonomous%20Workflow%20Bot&fontSize=48&fontAlignY=40&color=0:0f2027,50:203a43,100:2c5364&fontColor=ffffff"/>
</p>

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=28&duration=3000&pause=800&color=00E7FF&center=true&vCenter=true&width=900&lines=Agentic+AI+Automation+Platform;Natural+Language+%E2%86%92+SQL+Reasoning;MCP+Tool+Registry+Architecture;Human-in-the-Loop+Safety+Layer;Autonomous+Workflow+Orchestration"/>
</p>

<p align="center">

<img src="https://img.shields.io/badge/Architecture-Agentic%20AI-blueviolet?style=for-the-badge"/>
<img src="https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Agents-Multi--Agent-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Database-SQLite-yellow?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Safety-HITL-red?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Deployment-Docker-0db7ed?style=for-the-badge"/>

</p>

---

# 🤖 Autonomous Workflow Bot

> A production-style **Agentic AI Automation Platform** that converts natural language business queries into SQL insights, executes workflows securely using **Human-in-the-Loop approvals**, and generates structured intelligence reports automatically.
>
> ---

# 🎬 System Preview

<p align="center">
<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdG9hZ2g1a2p1azM0aXJrZ2Q1N3d0Y3Q1MGpxb2E3a3Y2eWJsc3ZxZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/coxQHKASG60HrHtvkt/giphy.gif" width="650"/>
</p>

---

# 🧠 Project Overview

**Autonomous Workflow Bot** is a multi-agent AI automation system that transforms natural language business queries into executable workflows using schema-aware SQL reasoning, Model Context Protocol (MCP) tool orchestration, and Human-in-the-Loop safety controls.

Instead of writing manual SQL queries or generating static reports, users can simply ask:

The system automatically:

• Detects intent using a Planner Agent  
• Generates SQL queries using a SQL Agent  
• Executes tools via MCP registry  
• Applies HITL approval for sensitive actions  
• Produces structured intelligence reports  
• Exposes automation through FastAPI endpoints  

This architecture mirrors real-world **enterprise Agentic AI workflow orchestration systems**.
---

# 🏗 System Architecture

The Autonomous Workflow Bot follows a structured **multi-agent orchestration pipeline** inspired by modern Agentic AI system design patterns.

User Prompt
     ↓
Planner Agent
(Intent Detection Layer)
     ↓
SQL Agent
(Natural Language → SQL Reasoning)
     ↓
MCP Tool Registry
(Dynamic Tool Selection Layer)
     ↓
SQL Tool
(Database Execution Engine)
     ↓
Database
(SQLite Business Dataset)
     ↓
Report Agent
(Intelligence Report Generator)
     ↓
Workflow Engine
(Automation Orchestrator)
     ↓
Exported Reports (TXT / CSV / JSON)


This layered architecture ensures modularity, scalability, and safe execution across autonomous workflows.

---

# ⚙ Execution Pipeline Explained

### Step 1 — User Prompt

The workflow starts when a user submits a natural language query:

last week revenue


---

### Step 2 — Planner Agent

The Planner Agent detects intent and routes the request to the appropriate execution module:

Example:

| Query | Routed To |
|------|-----------|
| revenue by region | SQL Agent |
| weekly report | Workflow Engine |
| show customers | SQL Agent |

---

### Step 3 — SQL Agent

Transforms natural language into executable SQL using schema-aware reasoning.

Example:


SELECT SUM(revenue)
FROM sales
WHERE date >= DATE('now', '-7 day');


---

### Step 4 — MCP Tool Registry

Provides dynamic discovery of available execution tools:

• SQL Tool  
• File Tool  
• Report Tool  

Agents interact with tools through a centralized registry layer.

---

### Step 5 — HITL Safety Layer

Sensitive operations trigger approval before execution:


DELETE
DROP
ALTER
UPDATE


This ensures enterprise-grade execution safety and audit compliance.

---

### Step 6 — Report Agent

Generates structured business intelligence reports automatically:

Supported formats:

• TXT  
• CSV  
• JSON  

---

### Step 7 — Workflow Engine

Coordinates multi-agent execution pipelines for autonomous analytics workflows such as:


Generate weekly business report


End-to-end automation completes without manual intervention.

---

# ⚡ Core Features

The Autonomous Workflow Bot implements a production-style **Agentic AI execution stack** designed for intelligent workflow automation.

| Feature | Description | Status |
|--------|-------------|--------|
| Multi-Agent Architecture | Planner, SQL, Report, Safety agents coordinate execution | ✅ Implemented |
| Natural Language → SQL | Converts business queries into executable SQL automatically | ✅ Implemented |
| MCP Tool Registry | Centralized tool discovery & routing layer | ✅ Implemented |
| HITL Safety Layer | Human approval required before sensitive operations | ✅ Implemented |
| Workflow Automation Engine | Executes structured multi-step analytics pipelines | ✅ Implemented |
| Autonomous Report Generator | Weekly reports in TXT / CSV / JSON formats | ✅ Implemented |
| FastAPI Orchestration API | REST interface for agent control & automation | ✅ Implemented |
| Schema-Aware Query Execution | Database-aware intelligent SQL generation | ✅ Implemented |
| Execution Logging System | Tracks workflow execution & approvals | ✅ Implemented |
| Docker Deployment Support | Containerized environment for production usage | ✅ Implemented |

---

# 🧩 MCP Tooling Layer

Agents dynamically interact with tools using a centralized **Model Context Protocol-style registry**:

| Tool | Purpose |
|------|---------|
| SQL Tool | Executes structured database queries |
| File Tool | Reads local datasets for workflows |
| Report Tool | Generates intelligence reports |

This modular tool layer enables scalable extension of agent capabilities without modifying orchestration logic.

---

# 🔐 Safety & Compliance Engine

Enterprise-grade safeguards included:

| Safety Feature | Description |
|---------------|-------------|
| HITL Approval Queue | Prevents unsafe automated execution |
| Sensitive Query Detection | Blocks destructive SQL operations |
| Approval Logging | Maintains audit-ready execution history |
| Schema Validation | Ensures correct database interaction |

Designed to support **secure autonomous execution environments**.

---

# 🛠 Tech Stack

The system is built using a modular **Agentic AI automation architecture** combining backend orchestration, intelligent agents, workflow execution, and containerized deployment.

### 🧠 AI & Agent Layer

<p>
<img src="https://img.shields.io/badge/Multi--Agent%20Architecture-Agentic%20AI-blueviolet"/>
<img src="https://img.shields.io/badge/Natural%20Language%20SQL-Reasoning-success"/>
<img src="https://img.shields.io/badge/MCP-Tool%20Registry-orange"/>
<img src="https://img.shields.io/badge/HITL-Safety%20Layer-red"/>
</p>

---

### ⚙ Backend & Execution Layer

<p>
<img src="https://img.shields.io/badge/Python-3.10+-yellow"/>
<img src="https://img.shields.io/badge/FastAPI-Orchestration-009688"/>
<img src="https://img.shields.io/badge/REST%20API-Automation-blue"/>
<img src="https://img.shields.io/badge/Workflow-Execution%20Engine-purple"/>
</p>

---

### 🗄 Data Layer

<p>
<img src="https://img.shields.io/badge/SQLite-Structured%20Storage-lightgrey"/>
<img src="https://img.shields.io/badge/Schema--Aware-SQL%20Execution-informational"/>
</p>

---

### 🐳 Deployment Layer

<p>
<img src="https://img.shields.io/badge/Docker-Containerized%20Environment-0db7ed"/>
<img src="https://img.shields.io/badge/API-Production%20Ready-brightgreen"/>
</p>

---

### 🧩 Architecture Design Patterns Used

| Pattern | Purpose |
|--------|---------|
| Multi-Agent Orchestration | Task routing between planner, SQL, and reporting agents |
| MCP Tool Registry | Dynamic tool discovery & execution |
| HITL Approval Pipeline | Safety control before execution |
| Workflow Automation Engine | End-to-end analytics pipeline execution |
| Schema-Aware Querying | Intelligent SQL generation from structured metadata |

This stack mirrors modern **enterprise Agentic AI workflow systems**.

---

# 🌐 API Endpoints

The Autonomous Workflow Bot exposes a FastAPI-powered orchestration interface that allows users to interact with agents, trigger workflows, and retrieve analytics outputs programmatically.

Interactive documentation available at:

http://127.0.0.1:8000/docs

---

## 🔍 Health Check

Verify system status:

GET /

Response:

---

## 🧠 Execute Natural Language Query

Send business queries directly to the Planner Agent:

POST /query?prompt=last week revenue

Example supported prompts:

last week revenue  
revenue by region  
show all customers  
total revenue  

Execution flow:

Planner Agent → SQL Agent → MCP Registry → SQL Tool → Database

---

## 📊 Trigger Weekly Report Workflow

Run full automation pipeline:

POST /workflow/weekly-report

Optional format selection:

POST /workflow/weekly-report?format_type=json

Supported formats:

txt  
csv  
json  

Pipeline executed:

SQL Generation  
→ Data Extraction  
→ Report Creation  
→ File Export  
→ Execution Logging  

---

## 📂 List Generated Reports

Retrieve all generated analytics reports:

GET /reports

Example response:



### ✅ Result

Iske baad tumhara **API Endpoints section complete** ho jayega aur README:

- production-ready lagega 🚀  
- automation backend show karega 🤖  
- HITL safety highlight karega 🔐  
- recruiter-friendly banega ⭐

Agar next section (**Project Structure visualization**) bhi similarly strong banana hai to main woh bhi ready de deta hoon.

---

# 📂 Project Structure

The project follows a modular multi-agent architecture designed for scalable workflow automation systems.

autonomous-workflow-bot/
│
├── main.py                  # FastAPI application entry point
├── config.py                # Central configuration manager
├── requirements.txt         # Project dependencies
│
├── agents/                  # Intelligent agent modules
│   ├── planner_agent.py     # Intent detection & routing agent
│   ├── sql_agent.py         # Natural language → SQL generator
│   ├── report_agent.py      # Automated report generator
│   └── safety_agent.py      # HITL approval enforcement agent
│
├── tools/                   # MCP-compatible execution tools
│   ├── sql_tool.py          # Database interaction engine
│   ├── file_tool.py         # Local file reader utility
│   └── report_tool.py       # Report export handler
│
├── mcp/
│   └── mcp_registry.py      # Tool discovery & routing layer
│
├── workflows/
│   └── weekly_report_workflow.py   # Autonomous reporting pipeline
│
├── approval/
│   └── hitl_gate.py         # Human-in-the-Loop approval system
│
├── api/
│   └── routes.py            # FastAPI route definitions
│
├── database/
│   └── connection.py        # Database connection manager
│
├── reports/                 # Generated analytics output directory
│
└── docker/
    └── Dockerfile           # Containerized deployment config


---

# 🧠 Architecture Design Philosophy

The system is designed using modern **Agentic AI workflow orchestration principles**:

| Layer | Responsibility |
|------|----------------|
| Agents Layer | Decision-making & reasoning modules |
| MCP Layer | Dynamic tool discovery & execution routing |
| Tools Layer | External system interaction (DB, files, reports) |
| Workflow Layer | Multi-step automation pipelines |
| API Layer | External system integration interface |
| Safety Layer | HITL approval & execution validation |

This layered architecture enables extensibility, safety, and production-ready automation workflows.

---

# ⚙️ Installation & Quick Start Guide

Follow the steps below to set up and run the Autonomous Workflow Bot locally.

---

## ⚙️ Quick Start

Follow these steps to run the Autonomous Workflow Bot locally.

---

### 📥 Step 1 — Clone the Repository

bash
git clone https://github.com/hariompatidar7877/AI-Automation-Engineer-Research-Build-.git
cd autonomous-workflow-bot

---
###📦 Step 2 — Create Virtual Environment
python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Mac / Linux

source venv/bin/activate

--- 
##📚 Step 3 — Install Dependencies
pip install -r requirements.txt
🗄 Step 4 — Initialize Sample Database
python database/init_db.py

This creates sample business tables:

sales
customers
orders

---
##🚀 Step 5 — Start the Server
python main.py

Server will start at:

http://127.0.0.1:8000

---
###📊 Step 6 — Open Swagger Interface

Interactive API documentation available at:

http://127.0.0.1:8000/docs
