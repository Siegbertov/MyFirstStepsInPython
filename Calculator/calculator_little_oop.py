from tkinter import *

class BTN:
    global Calculator

    def __init__(self, element, r, c):
        self.element = element
        self.r = r
        self.c = c

        Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("Arial", 20, "bold"),
               text=str(self.element)).grid(row=self.r, column=self.c) # FIX ME: ADD Command


def main():
    global operator, color, txtDisplay, Calculator, text_input, elements, elnum
    Calculator = Tk()
    Calculator.title("OOP Calculator by Siegbertov")
    operator = ""
    text_input = StringVar()
    color = "ivory2"
    columns = 4
    txtDisplay = Entry(Calculator, font=("Arial", 20, "bold"), textvariable=text_input, bd=30, insertwidth=4,
                       bg=color, justify="right").grid(columnspan=columns)
    elements = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "C", "0", "=", "/"]
    elnum = len(elements)

    for i in range(elnum):
        r, c = divmod(i, columns)
        BTN(elements[i], r+1, c)

    Calculator.mainloop()

if __name__ == "__main__":
    main()