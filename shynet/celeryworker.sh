#!/bin/bash

# Start queue worker processes
echo Launching Shynet queue worker...
exec uv run celery -A shynet worker -E --loglevel=INFO --concurrency=3
