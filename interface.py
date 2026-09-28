from keyboard import add_hotkey as key
from os import _exit as exitcode
import customtkinter as ctk 
from main import compile
import sys as s

root = ctk.CTk()
root.title("asm2Bash")
root.geometry("800x600")

entry = ctk.CTkEntry(
    root, 
    placeholder_text="enter ASM code path", 
    width=250,
    height=35
)

entry.pack()

asm_file_or_path = entry.get()

def exit():
  try:
    s.exit(0)
  finally:
    exitcode(0)

key('esc', exit)

def enter():
    global asm_code, bash_line_code, asm_file_or_path

    with open(asm_file_or_path, "r", encoding="utf-8") as file:
        asm_code = file.read()
    
    for line in asm_code:
        bash_line_code += compile()
    
    if not bash_line_code == "err":
        error_label = ctk.CTkLabel(root, text="Syntax error: ")
        error_label.pack(pady=(20, 5))
    
    else:
        print(bash_line_code)
        
        success_label = ctk.CTkLabel(root, text="The code transpiled to bash was printed in the terminal console.")
        success_label.pack(pady=(20, 5))
    
btn = ctk.CTkButton(root, text="transpile", command=enter)
btn.pack(pady=20)

root.mainloop()
