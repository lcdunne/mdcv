# Check if the venv directory exists
if (-Not (Test-Path -Path "venv")) {
    # Create venv
    python -m venv venv
}

# Activate venv if not already activated
if (-Not $env:VIRTUAL_ENV) {
    & .\venv\Scripts\Activate.ps1
}

# Upgrade pip
python -m pip install --upgrade pip
python -m pip install --upgrade build
python -m build
