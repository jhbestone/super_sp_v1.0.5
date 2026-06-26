@echo off
chcp 65001 >nul
echo ============================================================
echo Super SP 广告全景分析系统 v1.0.5
echo ============================================================

set VENV_PYTHON=C:\Users\Administrator\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe

echo.
echo 正在生成分析报告...
"%VENV_PYTHON%" generate.py

echo.
echo 按任意键退出...
pause >nul
