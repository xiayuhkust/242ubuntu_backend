#!/bin/bash
cd "$(dirname "$0")"
if [ -f service.pid ]; then
    PID=$(cat service.pid)
    echo "Stopping service with PID: $PID"
    kill $PID 2>/dev/null || echo "Process not found"
    rm service.pid
    echo "Service stopped"
else
    echo "No service running"
fi
