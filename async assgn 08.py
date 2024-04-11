class menu:
    def __init__(self):
        self.items = {}

    def __setitem__(self, item, price):
        self.items[item] = price

    def __str__(self):
        return '\n'.join([f"{item} {price}" for item, price in self.items.items()])

m = menu()
m["idly"] = 10
m["vada"] = 20
print(m)
