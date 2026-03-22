# =========================
# BASE IMAGE
# =========================

FROM python:3.11-slim


# =========================
# SET WORKING DIRECTORY
# =========================

WORKDIR /app


# =========================
# COPY PROJECT FILES
# =========================

COPY . /app


# =========================
# INSTALL DEPENDENCIES
# =========================

RUN pip install --upgrade pip

RUN pip install fastapi uvicorn pandas


# =========================
# CREATE REQUIRED DIRECTORIES
# =========================

RUN mkdir -p logs reports database


# =========================
# EXPOSE APPLICATION PORT
# =========================

EXPOSE 8000


# =========================
# START APPLICATION
# =========================

CMD ["python", "main.py"]