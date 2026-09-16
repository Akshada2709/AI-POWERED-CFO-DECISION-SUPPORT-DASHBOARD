"""
One-click Python launcher for AI CFO Command Center
"""
import os
import sys
import time
import subprocess
import webbrowser
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

def cleanup_ports():
    try:
        import psutil
        for p in psutil.process_iter(['pid', 'name']):
            if p.info['name'] and any(k in p.info['name'].lower() for k in ['node', 'python']):
                try:
                    for c in p.net_connections(kind='tcp'):
                        if c.laddr and c.laddr.port in (3000, 8000):
                            p.kill()
                            break
                except Exception:
                    pass
    except Exception:
        pass

def main():
    print("=" * 70)
    print("        AI-POWERED CFO DECISION SUPPORT DASHBOARD")
    print("                   ONE-CLICK LAUNCHER")
    print("=" * 70)
    
    # 0. Clean stale processes
    cleanup_ports()

    # 1. Verify database
    db_file = ROOT_DIR / "cfo_dashboard.db"
    if not db_file.exists():
        print("[*] Database not detected. Ingesting Kaggle dataset and seeding database...")
        subprocess.run([sys.executable, "data/scripts/preprocess.py"], cwd=str(ROOT_DIR), check=True)
        subprocess.run([sys.executable, "data/scripts/load_database.py"], cwd=str(ROOT_DIR), check=True)
        print("[OK] Database created successfully.")
    else:
        print("[OK] Database detected (cfo_dashboard.db).")

    # 2. Start Backend
    print("[*] Starting FastAPI Backend on http://127.0.0.1:8000 ...")
    backend_cmd = f'start "CFO Backend (FastAPI)" cmd /k "cd /d "{ROOT_DIR}" && {sys.executable} -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000 --reload"'
    subprocess.Popen(backend_cmd, shell=True)

    # 3. Start Frontend
    print("[*] Starting Next.js Frontend on http://localhost:3000 ...")
    frontend_dir = ROOT_DIR / "frontend"
    frontend_cmd = f'start "CFO Frontend (Next.js)" cmd /k "cd /d "{frontend_dir}" && npm run dev"'
    subprocess.Popen(frontend_cmd, shell=True)

    # 4. Wait and Open Browser
    print("[*] Waiting 6 seconds for services to boot...")
    time.sleep(6)
    print("[*] Opening browser at http://localhost:3000 ...")
    webbrowser.open("http://localhost:3000")

    print("\n" + "=" * 70)
    print(" [SUCCESS] Services are running:")
    print(" - Dashboard: http://localhost:3000")
    print(" - API Docs:  http://127.0.0.1:8000/docs")
    print(" - To stop: Close the terminal windows or run 'stop.bat'")
    print("=" * 70)

if __name__ == "__main__":
    main()
