import tkinter as tk
from tkinter import ttk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x600")
        self.resizable(False, False)

        self.resultado_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Entrada
        entrada = ttk.Entry(self, textvariable=self.resultado_var, font=("Arial", 24), justify="right", state="disabled")
        entrada.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Botões
        botoes = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row_val = 1
        col_val = 0

        for botao in botoes:
            ttk.Button(self, text=botao, command=lambda b=botao: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configurar o layout da grade
        for i in range(1, 5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, valor):
        if valor == "=":
            try:
                resultado = eval(self.resultado_var.get())
                self.resultado_var.set(resultado)
            except Exception as e:
                self.resultado_var.set("Erro")
        else:
            current_text = self.resultado_var.get()
            self.resultado_var.set(current_text + valor)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
