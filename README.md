# AI-Powered CFO Decision Support System

An enterprise-grade Executive CFO Decision Support Dashboard combining real-world **Kaggle DataCo Smart Supply Chain** data, data engineering preprocessing pipelines, PostgreSQL/relational storage, FastAPI backend analytics, Next.js 16 frontend with Apache ECharts, and an AI natural language business assistant.

---

## 1. Project Overview

The **AI CFO Command Center** consolidates financial and operational intelligence into a unified executive interface:
- **Sales Analytics**: 4-region performance (North, South, East, West) and 4-segment analysis (Government, Enterprise, Retail, SME).
- **Profitability & P&L**: Mathematical profit analysis (`profit = revenue - cost`, `margin = profit / revenue * 100`).
- **Vendor Payables**: Outstanding & overdue liabilities across industrial suppliers.
- **Cash Flow Trajectory**: Monthly cash inflows, outflows, and net working capital.
- **Production Capacity**: Plant-wise utilization monitoring across Pune, Chennai, Gurugram, and Kolkata.
- **Orders & Logistics**: Order queues, dispatch execution, and shipping delivery adherence.
- **AI CFO Assistant**: Natural language business interface converting executive questions into structured intents and dynamic charts with zero SQL injection risk.

---

## 2. Dataset & Academic Integrity

- **Primary Dataset**: **DataCo Smart Supply Chain for Big Data Analysis** (obtained from Kaggle, 180,519 raw transaction records).
  - Preprocessed into a high-performance, validated dataset of 15,000 active sales rows, 3,000 orders, and 3,000 dispatches.
- **Auxiliary Datasets**:
  - `auxiliary_payables.csv`: 70 industrial vendor invoices with realistic due dates and overdue statuses.
  - `auxiliary_cash_flow.csv`: 312 monthly cash transaction records with inflow and outflow categories.
  - `auxiliary_production.csv`: 144 manufacturing plant capacity and output utilization records.

---

## 3. Technology Stack

- **Frontend**: Next.js 16 (App Router), TypeScript, Tailwind CSS, Apache ECharts, Lucide Icons.
- **Backend**: Python 3.11, FastAPI, Pydantic v2, SQLAlchemy 2.x, PostgreSQL / SQLite engine.
- **Data Engineering**: Pandas, NumPy.
- **AI**: Structured intent classification engine with deterministic fallback matching.

---

## 4. Quick Start Instructions

### Option A: One-Click Launcher (Recommended)
Simply double-click:
```
start.bat
```
*(Or in terminal: `python run.py`)*

This will automatically:
1. Verify the database (seeds from Kaggle data if missing).
2. Start the FastAPI backend on `http://127.0.0.1:8000`.
3. Start the Next.js frontend on `http://localhost:3000`.
4. Open the dashboard directly in your browser.
5. To stop all services anytime, double-click `stop.bat`.

---

### Option B: Manual Step-by-Step Setup

### Step 2: Data Preprocessing & Database Ingestion
```bash
# Run data preprocessing pipeline on Kaggle dataset
python data/scripts/preprocess.py

# Ingest preprocessed records into the database
python data/scripts/load_database.py
```

### Step 3: Run Backend Tests
```bash
# Execute automated test suite (APIs, mathematical consistency, AI intents)
python -m pytest backend/tests/test_cfo_api.py -v
```

### Step 4: Launch FastAPI Backend
```bash
python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000 --reload
```
*API documentation available at `http://127.0.0.1:8000/docs`*

### Step 5: Launch Next.js Frontend
```bash
# In a new terminal window:
cd frontend
npm run dev
```
*Open dashboard at `http://localhost:3000`*

---

## 5. Demonstration Queries (Top 10 Scenarios)

1. **"Show sales by region."** *(Displays regional bar chart comparing North, South, East, West)*
2. **"Which segment is most profitable?"** *(Identifies Government/Enterprise margin yield with bar chart)*
3. **"Show overdue vendor payments."** *(Renders overdue invoice register with supplier names & amounts)*
4. **"Can we fulfill pending orders with current production capacity?"** *(Cross-module comparison between pending order demand and plant spare capacity)*
5. **"Which regions have high sales but low profit?"** *(Cross-module margin variance analysis)*
6. **"Why was cash flow negative last month?"** *(Analyzes July Capex investment & supplier settlements)*
7. **"What is our net cash flow?"** *(Shows monthly inflow vs outflow trajectory)*
8. **"What is our production capacity?"** *(Displays plant capacity utilization %)*
9. **"How many orders are pending?"** *(Shows order fulfillment queue breakdown)*
10. **"What is the dispatch status?"** *(Displays delivery and shipping performance)*
