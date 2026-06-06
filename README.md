# SchemaShift 🚀

![SchemaShift CI Verification](https://github.com)

An automated database-to-API contract validation framework built to proactively detect and repair structural system drift between live databases and OpenAPI specifications.

## 🛠️ The Problem It Solves
In modern microservice architectures, backend developers frequently modify database tables (e.g., dropping or renaming columns) without updating the API documentation or notifying downstream QA/testing teams. This communication gap creates **schema drift**, leading to sudden production API failures and broken client applications. 

**SchemaShift** solves this by acting as a continuous integration sentinel. It interrogates the database architecture, maps it against the declared OpenAPI contract, fails the build if a breaking change is detected, and triggers an automated self-healing patch to restore test environment stability.

## 🏗️ Architectural Overview
```text
[ OpenAPI Contract (YAML) ] ➔ Declares expected schema criteria.
             │
             ▼ (Python Engine cross-references structures via Port 5432)
[ Isolated DB Container ]   ➔ Docker Postgres holding live architecture tables.
             │
             ▼ (Chaos Simulation)
[ Chaos Engine (SQL) ]      ➔ Intentionally mutates tables to simulate drift.
             │
             ▼ (Automated Remediation)
[ Self-Healing Suite ]      ➔ Intercepts failures and injects DDL structural patches.
```

## 🧰 Tech Stack & Ecosystem
* **Language:** Python 3.10+
* **Database Engine:** PostgreSQL 15
* **Infrastructure & Containerization:** Docker, Docker Compose
* **Database Driver & Parsing:** `psycopg2-binary`, `PyYAML`
* **Continuous Integration:** GitHub Actions (Ubuntu Environment)

## 📁 Key Modules
* `openapi.yaml`: The static source-of-truth API design contract demanding specific target columns (`id`, `username`, `email`).
* `db_inspector.py`: Utilizes the `psycopg2` driver to safely query PostgreSQL's system-level `information_schema.columns` directory, targeting structural metadata without loading row-heavy production records.
* `contract_validator.py`: A lightweight algorithmic logic layer parsing the nested structures of the YAML specification against extracted database keys.
* `break_db.py`: A chaos-testing module mimicking a rogue database migration by programmatically dropping critical constraints (`ALTER TABLE users DROP COLUMN email`).
* `self_heal.py`: An operational reliability script that dynamically calculates missing schemas and writes situational SQL execution flows to repair the cluster.
* `.github/workflows/schema_check.yaml`: Fully automated cloud pipeline ensuring no broken schemas make it past a pull request.

## 🚀 Local Deployment & Verification

1. **Clone the repository and spin up infrastructure:**
   ```bash
   docker compose up -d
   ```

2. **Establish the environment & populate baseline structures:**
   ```bash
   python seed_db.py
   ```

3. **Verify the contract baseline passes:**
   ```bash
   python test_run.py
   ```

4. **Inject schema chaos & verify failure detection:**
   ```bash
   python break_db.py
   python test_run.py
   ```

5. **Trigger the self-healing cycle:**
   ```bash
   python self_heal.py
   python test_run.py
   ```