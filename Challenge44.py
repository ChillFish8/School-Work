
def is_prime(number_):
    nums_ = [i+1 for i in range(number_)]
    nums_.pop(0)
    for item in nums_:
        for i in range(2, item):
            if (item % i) == 0:
                break
        else:
            print(item)
    print("End Of Numbers")

is_prime(28)