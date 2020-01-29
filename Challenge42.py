
def converter(string_, number_, buffer_):
    __space__ = buffer_
    if len(string_) < number_:
        return f"{string_}{(__space__ * (number_ - len(string_)))}"
    else:
        return string_[:len(string_) - number_]

print(converter("1234", 5, "b"))
