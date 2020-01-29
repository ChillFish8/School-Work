def ReadShoppingList(file):
    with open(file, "r") as file:
        print(file.read())

ReadShoppingList("ShoppingList.txt")