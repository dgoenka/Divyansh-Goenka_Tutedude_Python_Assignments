import tkinter.messagebox
from tkinter import *

firstNum = None
selectedOperand = None


def validate_number_input(new_text):
    if new_text == "" or new_text.isdigit():
        return True
    else:
        return False


window = Tk()
window.geometry("470x250")
window.resizable(False, False)
window.title("Calculator")
calcVal = StringVar(window, value="0")
e = Entry(window, textvariable=calcVal, font=('Arial', 30, 'bold'), width=25, justify='right', borderwidth=5,
          validate='all',
          validatecommand=(window.register(validate_number_input), '%P'))
e.place(x=10, y=5)


def numClicked(num):
    currentNum = int(calcVal.get())
    currentNum = currentNum * 10 + num
    calcVal.set(str(currentNum))


def operandClicked(operand):
    global firstNum
    global selectedOperand
    if selectedOperand is not None:
        return
    firstNum = int(calcVal.get())
    selectedOperand = operand
    calcVal.set("0")


def equalsClicked():
    global firstNum
    global selectedOperand
    secondNum = int(calcVal.get())
    result = 0
    match selectedOperand:
        case "+":
            result = firstNum + secondNum
        case "-":
            result = firstNum - secondNum
        case "*":
            result = firstNum * secondNum
        case "/":
            if secondNum == 0:
                tkinter.messagebox.showerror(title="Division by Zero", message="Division by zero is not allowed")
                allClear()
                return
            result = firstNum / secondNum
        case _:
            return
    calcVal.set(str(result))
    firstNum = None
    selectedOperand = None


def allClear():
    global firstNum
    global selectedOperand
    firstNum = None
    selectedOperand = None
    calcVal.set('0')


b1 = Button(window, text="1", width=12, command=lambda: numClicked(1))
b1.place(x=10, y=60)
b2 = Button(window, text="2", width=12, command=lambda: numClicked(2))
b2.place(x=160, y=60)
b3 = Button(window, text="3", width=12, command=lambda: numClicked(3))
b3.place(x=310, y=60)
b4 = Button(window, text="4", width=12, command=lambda: numClicked(4))
b4.place(x=10, y=90)
b5 = Button(window, text="5", width=12, command=lambda: numClicked(5))
b5.place(x=160, y=90)
b6 = Button(window, text="6", width=12, command=lambda: numClicked(6))
b6.place(x=310, y=90)
b7 = Button(window, text="7", width=12, command=lambda: numClicked(7))
b7.place(x=10, y=120)
b8 = Button(window, text="8", width=12, command=lambda: numClicked(8))
b8.place(x=160, y=120)
b9 = Button(window, text="9", width=12, command=lambda: numClicked(9))
b9.place(x=310, y=120)
b0 = Button(window, text="0", width=12, command=lambda: numClicked(0))
b0.place(x=160, y=150)
bp = Button(window, text="+", width=8, command=lambda: operandClicked("+"))
bp.place(x=10, y=180)
bmin = Button(window, text="-", width=8, command=lambda: operandClicked("-"))
bmin.place(x=123, y=180)
bmult = Button(window, text="×", width=8, command=lambda: operandClicked("*"))
bmult.place(x=238, y=180)
bdiv = Button(window, text="÷", width=8, command=lambda: operandClicked("/"))
bdiv.place(x=348, y=180)
bac = Button(window, text="AC", width=21, command=allClear)
bac.place(x=10, y=210)
beq = Button(window, text="=", width=21, command=equalsClicked)
beq.place(x=238, y=210)
mainloop()
