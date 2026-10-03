#!/bin/bash 

INSTALL_PATH="./asm2bash"

python3 -m venv "$INSTALL_PATH"
MAIN_FILE="./asm2bash/interface.py"

"$INSTALL_PATH/bin/pip" install --upgrade pip
"$INSTALL_PATH/bin/pip" install keyboard
"$INSTALL_PATH/bin/pip" install customtkinter

start $MAIN_FILE
