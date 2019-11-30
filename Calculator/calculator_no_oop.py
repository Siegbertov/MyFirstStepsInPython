from tkinter import *

Calculator =Tk()
Calculator.title("Caclulator by Siegbertov")
operator = ""
text_input = StringVar()
color = "green"
columns = 4
txt_Display = Entry(Calculator, font=("arial", 20, "bold"), textvariable=text_input, bd=30,
                    insertwidth=4, bg=color, justify="center").grid(columnspan=columns)


Calculator.mainloop()