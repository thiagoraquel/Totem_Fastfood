# order.py

class Order:
  def __init__(self):
    self.cart = {}

  def add_item(self, item, quantity):
    if item.name in self.cart:
      self.cart[item.name]['quantity'] += quantity
    else:
      self.cart[item.name] = {'item': item, 'quantity': quantity}

  def remove_item(self, item_name):
    if item_name in self.cart:
      del self.cart[item_name]
    else:
      print("Item não encontrado no carrinho.")

  def reset(self):
    self.cart.clear()

  def total(self):
    return sum(entry['item'].price * entry['quantity'] for entry in self.cart.values())

  def print_cart(self):
    if not self.cart:
      print("Carrinho vazio.")
    for entry in self.cart.values():
      item = entry['item']
      quantity = entry['quantity']
      print(f"{item.name} x{quantity} - R$ {item.price * quantity:.2f}")

  def generate_receipt(self):
    print("==== CUPOM FISCAL ====")
    self.print_cart()
    print(f"Total: R$ {self.total():.2f}")
    print("======================")
