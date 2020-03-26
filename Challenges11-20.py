# Run using JIT Compiler 3.8

def ch11():
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    running = True
    while running:
        num = input("Enter a number between 1 and 26 ")
        if num.isdigit():
            if int(num) in range(1, 27):
                print(LETTERS[int(num) - 1])
                running = False

print(ch11())