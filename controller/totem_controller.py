from enum import Enum, auto
from model.menu import Menu
from model.order import Order

class TotemState(Enum):
    WELCOME = auto()
    BROWSING = auto()
    MODIFYING = auto()
    CHECKOUT = auto()
    AWAITING_PAYMENT = auto()
    COMPLETED = auto()

class TotemController:
    def __init__(self):
        self.state = TotemState.WELCOME
        self.menu = Menu()
        self.order = Order()
        self.selected_item = None

    def run(self):
        while True:
            match self.state:
                case TotemState.WELCOME:
                    self.show_welcome()
                case TotemState.BROWSING:
                    self.browse_menu()
                case TotemState.MODIFYING:
                    self.modify_item()
                case TotemState.CHECKOUT:
                    self.checkout()
                case TotemState.AWAITING_PAYMENT:
                    self.await_payment()
                case TotemState.COMPLETED:
                    self.complete_order()

    def show_welcome(self):
        print("\n=== Bem-vindo ao Totem de Autoatendimento! ===")
        input("Pressione Enter para começar o pedido...")
        self.order.reset()
        self.state = TotemState.BROWSING

    def browse_menu(self):
        print("\n--- Menu de Produtos ---")
        for i, item in enumerate(self.menu.items):
            print(f"{i+1}. {item.name} - R$ {item.price:.2f}")
        print(f"\nTotal atual: R$ {self.order.total():.2f}")
        print("0. Ir para o pagamento")

        choice = input("Escolha um produto pelo número ou vá para o pagamento: ")
        if choice == "0":
            self.state = TotemState.CHECKOUT
        else:
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.menu.items):
                    self.selected_item = self.menu.items[index]
                    self.state = TotemState.MODIFYING
                else:
                    print("Escolha inválida.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def modify_item(self):
        print(f"\nProduto selecionado: {self.selected_item.name} - R$ {self.selected_item.price:.2f}")
        try:
            qty = int(input("Quantas unidades deseja adicionar? "))
            if qty > 0:
                total = self.selected_item.price * qty
                print(f"Total do item: R$ {total:.2f}")
                confirm = input("Adicionar ao carrinho? (s/n): ").lower()
                if confirm == 's':
                    self.order.add_item(self.selected_item, qty)
            else:
                print("Quantidade deve ser maior que zero.")
        except ValueError:
            print("Digite um número válido.")
        self.state = TotemState.BROWSING

    def checkout(self):
        print("\n--- Carrinho ---")
        self.order.print_cart()
        print(f"Total: R$ {self.order.total():.2f}")
        print("\n1. Escolher forma de pagamento")
        print("2. Remover item")
        print("3. Cancelar pedido")
        print("4. Voltar para o menu")

        choice = input("Escolha uma opção: ")

        match choice:
            case "1":
                self.state = TotemState.AWAITING_PAYMENT
            case "2":
                name = input("Digite o nome do item para remover: ")
                self.order.remove_item(name)
            case "3":
                print("Pedido cancelado.")
                self.state = TotemState.WELCOME
            case "4":
                self.state = TotemState.BROWSING
            case _:
                print("Opção inválida.")

    def await_payment(self):
        print("\n=== Pagamento ===")
        print("Escolha o método de pagamento:")
        print("1. Pix")
        print("2. Débito")
        print("3. Crédito")
        choice = input("Digite o número da opção: ")

        if choice in {"1", "2", "3"}:
            print("Processando pagamento...")
            input("Pressione Enter após o pagamento ser confirmado.")
            self.state = TotemState.COMPLETED
        else:
            print("Método inválido.")

    def complete_order(self):
        print("\n=== Pedido Concluído ===")
        self.order.generate_receipt()
        input("Pressione Enter para retornar à tela inicial...")
        self.state = TotemState.WELCOME
