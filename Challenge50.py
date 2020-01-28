def remove_item():
    Item_ = input("What item needs to be removed?")
    with open("shopping_list.txt", "r") as file:
        items = file.readlines()
        for i in items:
            if i == Item_:
                items.pop(items.index(i))
    with open("shopping_list.txt", "w") as file:
        file.writelines(items)


remove_item()
