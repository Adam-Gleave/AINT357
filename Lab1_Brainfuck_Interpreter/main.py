def load(code_file):
  code = ""
  try:
    with open(code_file) as f:
      code = f.read()
  except:
    exit("Could not read code file.")
  return code


def main():
  debug = False

  mem = [0] * 30000
  code = load("helloworld.bf")
  code_ptr = 0
  mem_ptr = 0

  while code_ptr < len(code):
    c = code[code_ptr]
    
    if c == '>':
      mem_ptr += 1
    elif c == '<':
      mem_ptr -= 1
    elif c == '+':
      mem[mem_ptr] += 1
    elif c == '-':
      mem[mem_ptr] -= 1
    elif c == '.':
      print(chr(mem[mem_ptr]), end="")
    elif c == ',':
      mem[mem_ptr] = ord(input("Input: "))
    elif c == '[':
      if mem[mem_ptr] == 0:
        while c != ']':
          code_ptr += 1
          c = code[code_ptr]
    elif c == ']':
      if mem[mem_ptr] != 0:
        while c != '[':
          code_ptr -= 1
          c = code[code_ptr]
    elif c == '~':
      addr = mem[mem_ptr]*256 + mem[mem_ptr+1]
      code_ptr = addr-1
    elif c == '|':
      sign = False
      if mem[mem_ptr] != 0:
        sign = True

      jump = mem[mem_ptr+1] - 1
      if sign:
        code_ptr -= jump
      else:
        code_ptr += jump

    if debug:    
      print("code: ", c)
      print("mem_ptr: ", mem_ptr)
      print("code_ptr: ", code_ptr)
      print("mem: ", mem[mem_ptr])
      print()

    code_ptr += 1

if __name__ == "__main__":
  main()