class ShoppingList:

    def __init__(self, list_name):
        self.list_name = list_name
        self.items = []

    def add_item(self, item_name, quantity):
        self.items.append({'name': item_name, 'quantity': quantity})

    def remove_item(self, item_name):
        for item in self.items:
            if item['name'] == item_name:
                self.items.remove(item)
            else:
                print("Имени такого товара нет!")

    def display_list(self):
        print(f"Название - {self.list_name}")
        for item in self.items:
            print(f"Товар: {item['name']}\nКоличество: {item['quantity']}")


one = ShoppingList("Верный")
one.add_item("Молоко", 2)
one.add_item("Xleb", 5)
one.display_list()