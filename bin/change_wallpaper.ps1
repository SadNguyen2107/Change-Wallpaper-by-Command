param (
    [string]$param
)

if (-not $param) {
    Write-Host "Usage: .\change_wallpaper.ps1 <param>"
    exit 1
}

# Run the Python script
python "scripts\change_wallpaper.py" $param