# order.py

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, qty):
        for i in self.items:
            if i['item'].name == item.name:
                i['qty'] += qty
                return
        self.items.append({'item': item, 'qty': qty})

    def remove_item(self, name):
        self.items = [i for i in self.items if i['item'].name != name]

    def total(self):
        return sum(i['item'].price * i['qty'] for i in self.items)

    def print_cart(self):
        for i in self.items:
            print(f"{i['item'].name} x{i['qty']} = R$ {i['item'].price * i['qty']:.2f}")

    def reset(self):
        self.items = []

    def generate_receipt(self):
        print("\n=== Recibo ===")
        self.print_cart()
        print(f"Total: R$ {self.total():.2f}")
