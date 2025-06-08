import tkinter as tk
from controller.totem_controller import TotemController
from view.gui import TotemGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = TotemGUI(root)
    totem = TotemController()
    root.mainloop()
