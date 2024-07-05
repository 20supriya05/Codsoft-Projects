from tkinter import *
import ttkbootstrap as ttk  # Correctly import ttkbootstrap with an alias
from tkinter import ttk as tk_ttk  # Import standard ttk from tkinter

class Calculator(ttk.Window):
    def __init__(self):
        super().__init__(themename="flatly")
        self.title("Calculator")
        self.geometry("330x250")
        
        self.first_num = None
        self.math_operator = None
        
        self.create_widgets()
        
    def create_widgets(self):
        # Create the display widget
        self.display = tk_ttk.Entry(self, font=("Helvetica", 20), justify=RIGHT)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Create digit buttons
        digits = [
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('0', 4, 0)
        ]
        for (text, row, col) in digits:
            ttk.Button(self, text=text, bootstyle="", command=lambda t=text: self.add_digit(t)).grid(row=row, column=col, padx=5, pady=5)
        
        # Create operator buttons
        operators = [
            ('+', 1, 3), ('-', 2, 3),
            ('*', 3, 3), ('/', 4, 3)
        ]
        for (text, row, col) in operators:
            ttk.Button(self, text=text, bootstyle="warning", command=lambda t=text: self.add_operator(t)).grid(row=row, column=col, padx=5, pady=5)
        
        # Create special buttons
        ttk.Button(self, text="=", bootstyle="success", command=self.calculate).grid(row=4, column=1, padx=5, pady=5)
        ttk.Button(self, text="C", bootstyle="success", command=self.clear).grid(row=4, column=2, padx=5, pady=5)
    
    def add_digit(self, digit):
        value = self.display.get()
        if value == "0":
            value = digit
        else:
            value += digit
        self.display.delete(0, END)
        self.display.insert(0, value)

    def add_operator(self, operator):
        value = self.display.get()
        if value[-1] in "+-*/":
            value = value[:-1] + operator
        else:
            value += operator
        self.first_num = int(self.display.get().split(operator)[0])
        self.math_operator = operator
        self.display.delete(0, END)
        self.display.insert(0, value)

    def calculate(self):
        try:
            value = self.display.get()
            second_num = int(value.split(self.math_operator)[1])
            self.display.delete(0, END)
            if self.math_operator == "+":
                result = self.first_num + second_num
            elif self.math_operator == "-":
                result = self.first_num - second_num
            elif self.math_operator == "*":
                result = self.first_num * second_num
            elif self.math_operator == "/":
                if second_num == 0:
                    result = "Error"
                else:
                    result = self.first_num / second_num
            else:
                result = "Error"
            self.display.insert(0, result)
        except Exception as e:
            self.display.insert(0, "Error")

    def clear(self):
        self.display.delete(0, END)
        self.display.insert(0, "0")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
