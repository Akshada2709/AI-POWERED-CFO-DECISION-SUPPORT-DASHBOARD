@echo off
title Stop AI CFO Command Center
color 0C
cd /d "%~dp0"

echo ======================================================================
echo           STOPPING AI CFO DASHBOARD SERVICES
echo ======================================================================
echo.

echo [*] Terminating services on ports 3000 and 8000...
python -c "import psutil; [p.kill() for p in psutil.process_iter(['pid', 'name']) if p.info['name'] and any(k in p.info['name'].lower() for k in ['node', 'python']) and any(c.laddr.port in (3000, 8000) for c in p.net_connections(kind='tcp') if c.laddr)]" 2>nul

echo.
echo [OK] All CFO services have been stopped.
echo.
ping 127.0.0.1 -n 3 >nul
