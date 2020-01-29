def is_factor(number_):
    for i in range(1, number_):
        if number_ % i == 0:
            print(i)
    print("End of list")

is_factor(566)