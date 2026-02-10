#!/bin/bash

echo "========================================"
echo "  Resume RAG System - Quick Start"
echo "========================================"
echo ""

echo "[1/2] Starting Backend Server..."
gnome-terminal -- bash -c "source venv/bin/activate && python -m backend.main; exec bash" &

sleep 3

echo "[2/2] Starting Frontend Server..."
cd frontend
python start_server.py

echo ""
echo "========================================"
echo "  Servers Started!"
echo "========================================"
echo ""
echo "Backend:  http://localhost:8000"
echo "Frontend: Check terminal for URL"
echo ""
