def Beutiful(number):
    Sequence = []
    for i in range(len(number)):
        Sequence.append(number[i])
    for i in range(len(Sequence)):
        if i < len(Sequence) - 1:
            if int(Sequence[i]) == int(Sequence[i + 1]) - 1:
                print(Sequence[i], Sequence[i + 1])
            else:
                try:
                    if int(Sequence[i]) == int(f"{Sequence[i]}{Sequence[i + 1]}") - 1:
                        print(Sequence[i], f"{Sequence[i]}{Sequence[i + 1]}")

                    elif int(f"{Sequence[i]}{Sequence[i + 1]}") == int(f"{Sequence[i + 2]}{Sequence[i + 3]}") - 1:
                        print(Sequence[i], f"{Sequence[i]}{Sequence[i + 1]}")
                except:
                    print("Numbers not beutiful")

        else:
            print("End Of list")
    print(Sequence)

Beutiful("123")