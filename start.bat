@echo off
cls
echo Initializing...
rem Check if Python and pip are installed
python --version >nul 2>&1 || (echo Python is not installed. Please install Python and try again. & pause & exit /b 1)
pip --version >nul 2>&1 || (echo pip is not installed. Please install pip and try again. & pause & exit /b 1)

rem Check if modules are installed and install them if necessary
python -c "import easygui" >nul 2>&1 || (echo easygui module not found. Installing easygui module... & pip install easygui)

rem Run the pyTeX.py script
python pyTeX.py