# Reloj Digital - Christian Lera
# Script de inicio para PowerShell

Write-Host "====================================" -ForegroundColor Cyan
Write-Host "   Reloj Digital - Christian Lera" -ForegroundColor White
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Iniciando el reloj..." -ForegroundColor Yellow
Write-Host ""

try {
    python RelojDigital.py
}
catch {
    Write-Host ""
    Write-Host "[ERROR] No se pudo ejecutar el reloj." -ForegroundColor Red
    Write-Host "Asegurate de tener Python instalado y en el PATH." -ForegroundColor Red
    Write-Host ""
    Read-Host "Presiona Enter para salir"
}