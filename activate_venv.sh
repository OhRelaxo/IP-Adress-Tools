#!/bin/bash

VENV_DIR=".venv"
ACTIVATE_SCRIPT="$VENV_DIR/bin/activate"


if [ ! -d "$VENV_DIR" ]; then
    echo "no folder with the name .venv was found :("
fi


if [ -f "$ACTIVATE_SCRIPT" ]; then
    echo "activate virtual environment"
    source "$ACTIVATE_SCRIPT"
else
    echo "error: no activate script was found at: $ACTIVATE_SCRIPT"
    exit 1
fi
