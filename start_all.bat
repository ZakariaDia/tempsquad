@echo off
echo ========================================
echo  DAVID Dashboard System Launcher
echo ========================================
echo.

REM Check if we're in the right directory
if not exist "sender.py" (
    echo ERROR: sender.py not found!
    echo Make sure you're running this from the project directory.
    pause
    exit /b 1
)

if not exist "connector.py" (
    echo ERROR: connector.py not found!
    echo Make sure you're running this from the project directory.
    pause
    exit /b 1
)

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Make sure Python is installed and in your PATH.
    echo If using a venv, activate it first with: .venv\Scripts\activate
    pause
    exit /b 1
)

echo Python found: 
python --version
echo.

echo Starting sender.py in new window...
start "DAVID - Sender Script" cmd /k "python sender.py"
timeout /t 2 /nobreak >nul

echo Starting connector.py in new window...
start "DAVID - Connector Script" cmd /k "python connector.py"
timeout /t 2 /nobreak >nul

echo.
echo Background scripts started!
echo Starting Streamlit dashboard...
echo.
echo Press Ctrl+C to stop the dashboard
echo.

REM Start Streamlit in this window
streamlit run streamlitMain.py

echo.
echo Dashboard stopped.
pause