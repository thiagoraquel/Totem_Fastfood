# menu.py

class MenuItem:
  def __init__(self, name: str, price: float):
    self.name = name
    self.price = price

class Menu:
  def __init__(self):
    self.items = [
      MenuItem("X-Tudo", 14.99),
      MenuItem("Batata P", 4.99),
      MenuItem("Batata M", 5.99),
      MenuItem("Big Monstro", 16.99),
      MenuItem("Lata Refrigerante", 3.99),
    ]
