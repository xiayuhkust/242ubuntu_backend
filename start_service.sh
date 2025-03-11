#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > service.log 2>&1 &
echo $! > service.pid
echo "Service started with PID: $(cat service.pid)"
