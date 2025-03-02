param (
    [string]$mood  # Accepts mood as a command-line argument
)

# Ensure Python is available
$python = Get-Command python -ErrorAction SilentlyContinue

if (-not $python) {
    Write-Host "Python is not installed or not in PATH. Please install Python and try again."
    exit
}


# Get the directory of the PowerShell script
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Get the path to main.py in ../scripts/
$pythonScript = Join-Path $scriptDir "..\scripts\main.py"

# Run the Python script with the mood argument
python $pythonScript $mood
