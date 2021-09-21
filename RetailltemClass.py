class Retailltem:

    def __init__(self,description, inventory, price):
        self.__description = description
        self.__UnitinInvenroty = inventory
        self.__price = price

    def get_item(self):
        item_detail = f"description: {self.__description},\n units in inventory: {self.__UnitinInvenroty},\n price: {self.__price}"
        return item_detail.title()
