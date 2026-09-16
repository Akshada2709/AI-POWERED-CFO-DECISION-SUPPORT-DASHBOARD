@echo off
setlocal
cd /d "%~dp0"
title AI CFO Command Center Launcher
color 0B

echo ======================================================================
echo           AI-POWERED CFO DECISION SUPPORT DASHBOARD
echo                     ONE-CLICK LAUNCHER
echo ======================================================================
echo.

:: 1. Free any stale processes on 3000 / 8000
python -c "import psutil; [p.kill() for p in psutil.process_iter(['pid', 'name']) if p.info['name'] and any(k in p.info['name'].lower() for k in ['node', 'python']) and any(c.laddr.port in (3000, 8000) for c in p.net_connections(kind='tcp') if c.laddr)]" 2>nul

:: 2. Database check
if not exist "cfo_dashboard.db" (
    echo [*] Setting up database...
    python data\scripts\preprocess.py
    python data\scripts\load_database.py
) else (
    echo [OK] Database detected: cfo_dashboard.db
)

echo.
echo [*] Launching FastAPI Backend on port 8000...
start "CFO Backend (FastAPI)" cmd /k "cd /d "%~dp0" && python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000 --reload"

echo [*] Launching Next.js Frontend on port 3000...
start "CFO Frontend (Next.js)" cmd /k "cd /d "%~dp0frontend" && npm run dev"

echo.
echo [*] Waiting 6 seconds for services to boot...
ping 127.0.0.1 -n 7 >nul

echo [*] Opening Dashboard in browser...
start http://localhost:3000

echo.
echo ======================================================================
echo   [SUCCESS] Both Backend and Frontend are now running!
echo   - Dashboard: http://localhost:3000
echo   - API Docs:  http://127.0.0.1:8000/docs
echo   - To stop:   Double-click stop.bat or close the open windows.
echo ======================================================================
echo.
pause
