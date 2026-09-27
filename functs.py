bash = ""

def clear():
  global asm
  asm = ""
  asm += "\n"

def compile(asm_line):
  global asm, bash
  
  for line in asm_line
    asm = asm_line.strip().upper()
  
    if "MOV AX," in asm:
      bash += f"AX={asm.split(",")}"
      clear()

    elif "MOV AX, BX" in asm:
      bash += "AX=$BX"
      clear()

    elif "ADD AX," in asm:
      bash += f"AX=$((AX + {asm.split(",")}))"
      clear()

    elif "SUB AX," in asm:
      bash += f"AX=$((AX - {asm.split(",")}))"
      clear()

    elif "ADD BX," in asm:
      bash += f"BX=$((BX + {asm.split(",")}))"
      clear()

    elif "SUB BX," in asm:
      bash += f"BX=$((BX - {asm.split(",")}))"
      clear()

    elif "MUL AX," in asm:
      bash += f"AX=$((AX*{asm.split(",")}))"
      clear()

    elif "MUL BX," in asm:
      bash += f"BX=$((BX*{asm.split(",")}))"
      clear()

    elif "DIV AX," in asm:
      bash += f"AX=$((AX/{asm.split(",")}))"
      clear()

    elif "DIV BX," in asm:
      bash += f"BX=$((BX/{asm.split(",")}))"
      clear()

    elif "INC AX" in asm:
      bash += "AX++"
      clear()

    elif "INC BX" in asm:
      bash += "BX++"
      clear()
      
    elif "DEC AX" in asm:
      bash += "AX--"
      clear()

    elif "DEC BX" in asm:
      bash += "BX++"
      clear()

    elif "AND AX, BX" in asm:
      bash += "AX=$((AX & BX))"
      clear()

    elif "AND BX, AX" in asm:
      bash += "BX=$((BX & AX))"
      clear()

    elif "OR AX, BX" in asm:
      bash += "AX=$((AX | BX))"
      clear()

    elif "OR BX, AX" in asm:
      bash += "BX=$((BX | AX))"
      clear()

    elif "XOR AX, BX" in asm:
      bash += "AX=$((AX ^ BX))"
      clear()

    elif "XOR BX, AX" in asm:
      bash += "BX=$((BX ^ AX))"
      clear()
          
    elif "SHL AX," in asm:
      bash += f"AX=$((AX << {asm.split(",")}))"
      clear()

    elif "SHR AX," in asm:
      bash += f"AX=$((AX >> {asm.split(",")}))"
      clear()

    elif "SHL BX," in asm:
      bash += f"BX=$((BX << {asm.split(",")}))"
      clear()

    elif "SHR BX," in asm:
      bash += f"BX=$((BX >> {asm.split(",")}))"
      clear()

# JMP can't be emulated in bash, since it hasn't a goto command

    elif "CMP AX, BX" in asm:
      bash += f"if [ $AX -eq $BX ]; then"
      clear()

    elif "CMP BX, AX" in asm:
      bash += f"if [ $BX -eq $AX ]; then"
      clear()

    elif "JE label" in asm:
      bash += "if [ $AX -eq $BX ]; then"
      clear()

    elif "JNE label" in asm:
      bash += "if [ $AX -ne $BX ]; then"
      clear()

    elif "JG label" in asm:
      bash += "if [ $AX -gt $BX ]; then"
      clear()

    elif "JL label" in asm:
      bash += "if [ $AX -lt $BX ]; then"
      clear()

    elif "CALL func" in asm:
      bash += "func"
      clear()

    elif "RET" in asm:
      bash += "ret"
      clear()

    elif "PUSH AX" in asm:
      bash += "stack+=($AX)"
      clear()

    elif "PUSH BX" in asm:
      bash += "stack+=($BX)"
      clear()

    elif "POP AX" in asm:
      bash += "AX = ${stack[-1]}"; unset 'stack[-1]'"
      clear()

    elif "POP BX" in asm:
      bash += "BX = ${stack[-1]}"; unset 'stack[-1]'"
      clear()

    else:
      return "Syntax Error: command not archived."

    return bash
