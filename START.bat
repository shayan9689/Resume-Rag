@echo off
echo ========================================
echo   Resume RAG System - Quick Start
echo ========================================
echo.

echo [1/2] Starting Backend Server...
echo.
start "Backend Server" cmd /k "venv\Scripts\activate && python -m backend.main"

timeout /t 3 /nobreak >nul

echo [2/2] Starting Frontend Server...
echo.
start "Frontend Server" cmd /k "cd frontend && python start_server.py"

echo.
echo ========================================
echo   Both servers are starting...
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: Will open automatically
echo.
echo Press any key to exit this window...
pause >nul
