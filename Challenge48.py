def WriteShoppingList():
    Shopping_List = []
    Finished = False
    while not Finished:
        Item = input("What item to be added to the list? Type 'END' to stop and save. ")
        if Item.upper() == "END":
            Finished = True
            with open("ShoppingList.txt", "w+") as file:
                for item in Shopping_List:
                    file.write(f"{item}\n")
        else:
            Shopping_List.append(Item)

WriteShoppingList()
