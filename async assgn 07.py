class menu:
    def __init__(self):
        self.items = {}

    def __add__(self, item):
        self.items[item[0]] = item[1]
        return self

    def show(self):
        print(self.items)

m = menu()
m + ("idly", 10) + ("vada", 20)
m.show()
