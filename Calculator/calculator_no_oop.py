from tkinter import *

def btnClick(numbers):
    global operator
    operator +=str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")

def btnEquals():
    global operator
    result = str(eval(operator))
    text_input.set(result)
    operator = result

Calculator =Tk()
Calculator.title("Caclulator by Siegbertov")
operator = ""
text_input = StringVar()
color = "green"
columns = 4
txt_Display = Entry(Calculator, font=("arial", 20, "bold"), textvariable=text_input, bd=30,
                    insertwidth=4, bg=color, justify="right").grid(columnspan=columns)


btn7=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="7",
            command=lambda:btnClick(7)).grid(row=1, column=0)
btn8=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="8",
            command=lambda:btnClick(8)).grid(row=1, column=1)
btn9=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="9",
            command=lambda:btnClick(9)).grid(row=1, column=2)
addit=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="+",
             command=lambda:btnClick("+")).grid(row=1, column=3)

btn4=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="4",
            command=lambda:btnClick(4)).grid(row=2, column=0)
btn5=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="5",
            command=lambda:btnClick(5)).grid(row=2, column=1)
btn6=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="6",
            command=lambda:btnClick(6)).grid(row=2, column=2)
subs=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="-",
            command=lambda:btnClick("-")).grid(row=2, column=3)

btn1=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="1",
            command=lambda:btnClick(1)).grid(row=3, column=0)
btn2=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="2",
            command=lambda:btnClick(2)).grid(row=3, column=1)
btn3=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="3",
            command=lambda:btnClick(3)).grid(row=3, column=2)
mult=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="*",
            command=lambda:btnClick("*")).grid(row=3, column=3)

btnclr=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="C",
              command=btnClearDisplay).grid(row=4, column=0)
btn0=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="0",
            command=lambda:btnClick(0)).grid(row=4, column=1)
btneq=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="=",
             command=btnEquals).grid(row=4, column=2)
divid=Button(Calculator, padx=16, pady=16, bd=8, bg=color, fg="black", font=("arial", 20, "bold"), text="/",
             command=lambda:btnClick("/")).grid(row=4, column=3)


Calculator.mainloop()
