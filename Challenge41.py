
def converter(string_, number_):
    __space__ = " "
    if len(string_) < number_:
        return f"{(__space__ * (number_ - len(string_)))}{string_}"
    else:
        return string_[len(string_) - number_:]

print(converter("1234", 3))
