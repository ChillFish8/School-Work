import os


def change_file_add(_newItem):
    with open("dictionary.txt", "r") as file:
        items = file.readlines()
    items.append(f"{_newItem}\n")
    items.sort()
    with open("dictionary.txt", "w") as file:
        file.writelines(items)


def change_file_remove(_oldItem):
    with open("dictionary.txt", "r") as file:
        items = file.readlines()
    items.remove(f"{_oldItem}\n")
    items.sort()
    with open("dictionary.txt", "w") as file:
        file.writelines(items)


def search_word(_word):
    with open("dictionary.txt", "r") as file:
        for word in file:
            if _word == word.strip():
                return True
        return False


def check_file():
    if not os.path.exists("dictionary.txt"):
        with open("dictionary.txt", "x"): pass

    word_ = input("What word would you like to search? ")
    Result = search_word(word_)
    if Result:
        user_input_ = input("Word Found! would you like to remove it y/n ")
        if user_input_.lower() == "y":
            change_file_remove(word_)
            print("All done!")
        else:
            print("See you next time!")
    else:
        user_input_ = input("Word not found! would you like to add it y/n ")
        if user_input_.lower() == "y":
            change_file_add(word_)
            print("All done!")
        else:
            print("See you next time!")

check_file()