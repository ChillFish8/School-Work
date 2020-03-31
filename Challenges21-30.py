def ch21():
    income = int(input("How much do you earn per year? "))
    if income < 10000:
        print("You pay £0 income tax!")
    elif income <= 50000:
        tax = (income - 10000) * 0.2
        print(f"You pay £{tax} income tax!")
    elif income > 50000:
        tax = (income - 50000) * 0.4
        print(f"You pay £{tax} income tax!")


def ch22():
    income = int(input("How much do you earn per year? "))
    if income < 10000:
        print("You pay £0 income tax!")
    elif income <= 50000:
        tax = (income - 10000) * 0.2
        print(f"You pay £{tax} income tax!")
    elif income > 50000:
        tax = (income - 50000) * 0.4
        print(f"You pay £{tax} income tax!")

    if income < 700:
        print("You pay £0 insurance tax!")
    elif 700 <= income <= 4000:
        print(f"You pay £{income * 0.12} insurance tax!")
    else:
        print(f"You pay £{income * 0.02} insurance tax!")


def ch23():
    income = int(input("How much do you earn per year? "))
    print(f"You pay {income * 0.075} to your pension")
    print(f"Your employer pays {income * 0.025} to your pension")


class Ch24:
    @classmethod
    def payslip(cls, amount):
        net, tax, insurance, pension = cls.get_figures(amount)
        print(f"Your payslip:\n"
              f"Net Yearly pay: £{net}\n"
              f"Net Monthly pay: £{net / 12}\n"
              f"==============================\n"
              f"Yearly Tax: £{tax}\n"
              f"Yearly Insurance: £{insurance}\n"
              f"Yearly Pension: £{pension}\n")

    @classmethod
    def get_figures(cls, amount):
        tax = cls.get_tax(amount)
        pension = cls.get_pension(amount)
        insurance = cls.get_insurance(amount)
        net = amount - (tax + pension + insurance)
        return net, tax, insurance, pension

    @classmethod
    def get_pension(cls, amount):
        return amount * 0.075

    @classmethod
    def get_insurance(cls, amount):
        if amount < 700:
            return 0
        elif 700 <= amount <= 4000:
            return amount * 0.12
        else:
            return amount * 0.02

    @classmethod
    def get_tax(cls, amount):
        if amount < 10000:
            return 0
        elif amount <= 50000:
            return (amount - 10000) * 0.2
        elif amount > 50000:
            return (amount - 50000) * 0.4


def ch25():
    valid = False
    while not valid:
        date = input("Enter a date. ")
        if date.count('/') == 2:
            day, month, year = date.split('/')
            if (len(day) == 2) and (len(month) == 2) and (len(year) == 4):
                if day.isdigit() and month.isdigit() and year.isdigit():
                    year = int(year)
                    if (year % 4 == 0) and (year % 100 != 0):
                        print("This date is a leap year!")
                    else:
                        print("This date is not a leap year!")
                    valid = True


def ch26(binary):
    hex_code, den = "", 0
    table = "123456789ABCDEF"
    for i, num in enumerate(str(binary)):
        if (i % 4 == 0) and (i != 0):
            hex_code = table[den - 1] + hex_code
            den = 0
        if num:
            den += ((i + 1) % 4)**2
        print(den, hex_code)
    hex_code = table[den - 1] + hex_code
    return hex_code

