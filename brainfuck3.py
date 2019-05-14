
tape = [0] * 100

with open("code.txt", "r") as f:
    bf_code = f.read()

i = 0
j = 0
size = len(tape)
code_size = len(bf_code)

while j < code_size:
    c = bf_code[j]
    if c == '>':
        i += 1
        if i == size:
            tape += [0] * size
            size *= 2
    elif c == '<':
        if i > 0:
            i -= 1
    elif c == '+':
        tape[i] = (tape[i] + 1) % 256
    elif c == '-':
        tape[i] = (tape[i] - 1) % 256
    elif c == '.':
        print(chr(tape[i]), end='')
    elif c == '[':
        lbc = 1
        rbc = 0
        if tape[i] == 0:
            j += 1
            while lbc > rbc:
                c = bf_code[j]
                if c == '[':
                    lbc += 1
                elif c == ']':
                    rbc += 1
                j += 1
            continue
    elif bf_code[j] == ']':
        lbc = 0
        rbc = 1
        if tape[i] != 0:
            j -= 1
            while rbc > lbc:
                c = bf_code[j]
                if c == '[':
                    lbc += 1
                elif c == ']':
                    rbc += 1
                j -= 1
            j += 1
    j += 1
