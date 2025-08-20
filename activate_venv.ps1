# activate_venv.ps1
$venvPath = ".venv\Scripts\Activate.ps1"

if (Test-Path $venvPath) {
    Write-Host "activate virtual environment"
    & $venvPath
} else {
    Write-Host "error: no activate script was found at: $venvPath"
}
