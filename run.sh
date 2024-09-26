#!/bin/bash
# Check if the virtual environment directory exists
if [ -d ".venv" ]; then
    # Activate the virtual environment
    source .venv/Scripts/activate.bat
    echo "Virtual environment activated."
else
    echo "Virtual environment not found. Please create one."
    exit 1
fi
# Navigate to the project directory

# Activate the virtual environment if you have one
# source venv/bin/activate

# Run the FastAPI app with uvicorn
uvicorn app:app --host 0.0.0.0 --port 8000 --reload