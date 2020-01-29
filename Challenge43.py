def converter(string_, number_, buffer_):
    __space__ = buffer_
    if len(string_) < number_:
        New_String = (__space__ * (number_ - len(string_)))
        Mid = len(New_String) // 2
        Left = New_String[Mid:]
        Right = New_String[:Mid]
        return f"{Left}{string_}{Right}"
    else:
        _x = len(string_) - number_ + 1
        Mid = _x // 2        
        return string_[Mid:len(string_) - Mid]

print(converter("1234", 3, "b"))