import tkinter as tk

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora GUI OO")
        
        self.expression = ""
        
        self.display = tk.Entry(root, font=("Arial", 16), borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)
        
   
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        
        for (text, row, col) in buttons:
            self.create_button(text, row, col)
    
    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, font=("Arial", 14), padx=5, pady=5, command=lambda: self.on_button_click(text), width=5, height=2, bg="Blue")
        button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Erro"
        else:
            self.expression += str(char)

        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = CalculadoraGUI(root)
    root.mainloop()