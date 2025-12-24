import sys

def seal_terminal():
    cells = [0] * 30000
    ptr = 0
    
    print("--- EggFibshSeal Interactive Terminal ---")
    print("Commands: egg!, egg-crack, l'egg, d'egff, fibsh, giggphbh, AAAAAAA, *sneezes*")
    print("-" * 42)

    while True:
        try:
            line = input(f"seal@{ptr}> ")
            if line.lower() == 'exit': break
            
            tokens = line.split()
            # Loop pre-processing
            stack = []
            loops = {}
            for i, t in enumerate(tokens):
                if t == "fibsh": stack.append(i)
                elif t == "giggphbh" and stack:
                    start = stack.pop()
                    loops[start] = i
                    loops[i] = start

            pc = 0
            while pc < len(tokens):
                cmd = tokens[pc]
                if cmd == "egg!": cells[ptr] = (cells[ptr] + 1) % 256
                elif cmd == "egg-crack": cells[ptr] = (cells[ptr] - 1) % 256
                elif cmd == "l'egg": ptr += 1
                elif cmd == "d'egff": ptr -= 1
                elif cmd == "AAAAAAA": print(chr(cells[ptr]), end="", flush=True)
                elif cmd == "*sneezes*": cells[ptr] = 0
                elif cmd == "fibsh" and cells[ptr] == 0: pc = loops[pc]
                elif cmd == "giggphbh" and cells[ptr] != 0: pc = loops[pc]
                pc += 1
            print(f"\nMemory: {cells[:10]}...") 
            
        except Exception: pass

if __name__ == "__main__":
    seal_terminal()
