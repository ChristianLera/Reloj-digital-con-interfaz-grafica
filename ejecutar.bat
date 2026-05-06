@echo off
title Reloj Digital
echo ====================================
echo    Reloj Digital - Christian Lera
echo ====================================
echo.
echo Iniciando el reloj...
echo.

python RelojDigital.py

if errorlevel 1 (
    echo.
    echo [ERROR] No se pudo ejecutar el reloj.
    echo Asegurate de tener Python instalado y en el PATH.
    echo.
    pause
)