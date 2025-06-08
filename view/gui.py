# gui.py

import tkinter as tk
from tkinter import messagebox
from model.menu import Menu
from model.order import Order

class TotemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Totem de Autoatendimento")
        self.menu = Menu()
        self.order = Order()

        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.pack()

        self.label = tk.Label(self.main_frame, text="Escolha um item do menu:")
        self.label.pack()

        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.pack()

        for item in self.menu.items:
            btn = tk.Button(
                self.buttons_frame,
                text=f"{item.name} - R$ {item.price:.2f}",
                width=30,
                command=lambda i=item: self.add_item(i)
            )
            btn.pack(pady=2)

        self.cart_label = tk.Label(self.main_frame, text="Carrinho vazio.")
        self.cart_label.pack(pady=10)

        self.checkout_button = tk.Button(self.main_frame, text="Finalizar Pedido", command=self.checkout)
        self.checkout_button.pack()

    def add_item(self, item):
        self.order.add_item(item, 1)
        self.update_cart_display()

    def update_cart_display(self):
        if not self.order.items:
            self.cart_label.config(text="Carrinho vazio.")
        else:
            text = "\n".join([f"{i['item'].name} x{i['qty']} = R$ {i['item'].price * i['qty']:.2f}"
                              for i in self.order.items])
            total = self.order.total()
            self.cart_label.config(text=f"{text}\n\nTotal: R$ {total:.2f}")

    def checkout(self):
        if not self.order.items:
            messagebox.showinfo("Carrinho", "O carrinho está vazio!")
            return
        self.order.generate_receipt()
        messagebox.showinfo("Pedido Finalizado", "Pedido concluído com sucesso!\nO recibo foi gerado no terminal.")
        self.order.reset()
        self.update_cart_display()
