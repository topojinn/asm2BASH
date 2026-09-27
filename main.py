from keyboard import add_hotkey as key
from os import _exit as exitcode
from functs import compile
import sys as s

print("Inert a line of ASSEMBLY code\n")
asm_code = input("")

for line in asm_code:
  bash_line_code += compile()

if not bash_line_code == "err":
  print("\n"bash_line_code)

else:
  print(bash_line_code)

def exit():
  try:
    s.exit(0)
  finally:
    exitcode(0)

key('esc', exit)
