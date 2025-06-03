# CVE WebApp  – Securin Assessment Submission

## 👋 Hello Securin Team

Greetings! This repository contains my solution for the backend engineering assessment as part of the application process at **Securin**.

---

## 📌 Project Overview

This project is a full-featured **CVE (Common Vulnerabilities and Exposures) data ingestion and API service**, built using **FastAPI** with an asynchronous architecture. It fetches CVE data from the NVD (National Vulnerability Database), stores it in a SQLite database, and exposes secure, paginated, and searchable API endpoints.

---

## 🚀 Features

- ⚡ **Asynchronous Backend** using FastAPI 
- 📥 **CVE Fetching & Syncing** from NVD API
- 📂 **CVE Storage** in SQLLite
- 🔍 **API Endpoints** for listing and searching CVEs
- 🌐 **Modern Frontend Support** 
- 📑 **Auto-generated API Docs** available at `/docs`
- 🧪 Easily testable and extendable design
---

## 📥 Installation
```console
# 1. Clone the repository
git clone https://github.com/th3sanjai/cvedb.git

# 2. Navigate to the project directory
cd cvedb

# 3. View available options and flags
uv run main.py -h
```

## Usage

```console
[DESCRIPTION]:

    CVE WebApp Backend CLI tool to manage FastAPI server setup and control behavior of  database setup and running server

[USAGE]:

    [flags]

[FLAGS]:

    [SERVER OPTIONS]:
        -host,   --host            :  Host address to bind FastAPI server (default: 0.0.0.0)
        -port,   --port            :  Port number for FastAPI server (default: 8000)
        -reload, --reload          :  Enable auto-reload on code changes (default: True)

    [DATABASE OPTIONS]:
        -sdb,    --setup-db        :  Create database schema before starting the server

    [MISC]:
        -h,      --help            :  Show this help menu
```

## 🚀 Running the Server

```console
# 1. Setup the database and fetch initial CVE data
uv run main.py --setup-db

# 2. Start the FastAPI server with custom host and port
uv run main.py --host 127.0.0.1 --port 5000 --reload
```

## Info
Once the server starts, visit:
- Swagger API Docs: http://127.0.0.1:5000/docs
- Frontend App: http://127.0.0.1:5000/





