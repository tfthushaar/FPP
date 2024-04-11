class menu:
    def __init__(self):
        self.items = {}

    def __setitem__(self, item, price):
        self.items[item] = price

    def __iter__(self):
        return iter(self.items.items())

m = menu()
m["idly"] = 10
m["vada"] = 20
for item, price in m:
    print(f"({item},{price})")
