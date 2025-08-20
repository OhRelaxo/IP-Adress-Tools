@echo off
SET VENV_PATH=.venv\Scripts\activate.bat

IF EXIST %VENV_PATH% (
    echo activate virtual environment
    call %VENV_PATH%
) ELSE (
    echo error: no activate script was found at: %VENV_PATH%.
)
