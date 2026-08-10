@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 RUN_SEXA_MASTER_AUDIT.py
) else (
  python RUN_SEXA_MASTER_AUDIT.py
)
echo.
echo Audit complete. See the reports folder.
pause
