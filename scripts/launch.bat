@echo off

cd ..
:: Check if env is not built
if not exist ".venv" (
  echo ".venv not found, creating virtual environment..."
  python -m venv .venv
) else (
  echo "Virtual env already exists. plendid"
)

:: activate env
call .venv/Scripts/activate

:: install deps
pip install -r requirements.txt
echo "Environment setup and checked. Launching..."

:: Launch app
python app.py