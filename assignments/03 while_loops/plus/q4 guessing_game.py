print("Think of a number between 1 and 100 (inclusive)")
print("I am going to guess what it is")
input("Press enter when you are ready to play")

hi = 100
lo = 1

while lo <= hi:
    guess = (lo + hi) // 2
    print("Is the number", guess, "?")
    print("Type one of the following letters and press enter:")
    print("h: if the guess is too (h)igh")
    print("l: if the guess is too (l)ow")
    print("c: if the guess is (c)orrect")
    print("q: to (q)uit the game")
    cmd = input()
    if cmd == "h":
        hi = guess - 1
    elif cmd == "l":
        lo = guess + 1
    elif cmd == "c":
        print("I AM VICTORIOUS")
        break
    elif cmd == "q":
        print("Quitter")
        break
    else:
        print(f"{cmd} is not among the recognized commands")

if hi < lo:
    print("Tsk, tsk, don't try to cheat me")
