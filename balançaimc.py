import tkinter as tk
from tkinter import messagebox


class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")
        self.create_widgets()

    def create_widgets(self):
        # Labels para altura e peso
        self.label_height = tk.Label(self.root, text="Altura (m):")
        self.label_height.grid(row=0, column=0, padx=10, pady=10)

        self.label_weight = tk.Label(self.root, text="Peso (kg):")
        self.label_weight.grid(row=1, column=0, padx=10, pady=10)

        # Entradas para altura e peso
        self.entry_height = tk.Entry(self.root)
        self.entry_height.grid(row=0, column=1, padx=10, pady=10)

        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.grid(row=1, column=1, padx=10, pady=10)

        # Botão para calcular o IMC
        self.button_calculate = tk.Button(
            self.root, text="Calcular IMC", command=self.calculate_bmi)
        self.button_calculate.grid(
            row=2, column=0, columnspan=2, padx=10, pady=10)

        # Rótulo para exibir o resultado do IMC
        self.label_result = tk.Label(self.root, text="")
        self.label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def calculate_bmi(self):
        try:
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())
            bmi = weight / (height ** 2)
            self.label_result.config(text=f"Seu IMC é: {bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError:
            messagebox.showerror(
                "Erro", "Por favor, insira valores válidos para altura e peso.")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso normal"
        elif 25 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        self.label_result.config(
            text=f"Seu IMC é: {bmi:.2f}\nCategoria: {category}")


# Executando o programa principal
if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
