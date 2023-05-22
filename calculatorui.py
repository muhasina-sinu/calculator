from tkinter import *
import tkinter.font as font


expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def percent():
    global expression
    expression = str(eval(expression)/100)
    equation.set(expression)
    
    
def sign_change():
    global expression
    if expression[0]=='-':
        expression = expression[1:]
    else:
        expression = '-'+expression
    equation.set(expression)      


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total

    except:
        equation.set(" error ")
        expression = ""
        
window = Tk()


window.title("CALCULATOR")



window.geometry("230x310")

equation = StringVar()

expression_field = Entry(window, width=25, bd=0, textvariable=equation)

expression_field.grid(columnspan=4,ipady=7)



button1 = Button(window, width=3, height=3, bd=0, text="1", bg="yellow", command=lambda: press("1"))
button2 = Button(window, width=3, height=3, bd=0,text="2", command=lambda: press("2"))
button3 = Button(window, width=3, height=3, bd=0,text="3", command=lambda: press("3"))
button4 = Button(window, width=3, height=3, bd=0,text="4", command=lambda: press("4"))
button5 = Button(window, width=3, height=3, bd=0,text="5", command=lambda: press("5"))
button6 = Button(window, width=3, height=3, bd=0,text="6", command=lambda: press("6"))
button7 = Button(window, width=3, height=3, bd=0,text="7", command=lambda: press("7"))
button8 = Button(window, width=3, height=3, bd=0,text="8", command=lambda: press("8"))
button9 = Button(window, width=3, height=3, bd=0,text="9", command=lambda: press("9"))
button0 = Button(window, width=3, height=3, bd=0,text="0", command=lambda: press("0"))
buttonplus = Button(window, width=3, height=3, bd=0,bg='yellow', text="+", command=lambda: press("+"))
buttonminus = Button(window, width=3, height=3, bd=0, text="-", command=lambda: press("-"))
buttonmult = Button(window, width=3, height=3, bd=0, text="x", command=lambda: press("*"))
buttondiv = Button(window, width=3, height=3, bd=0, text="/", command=lambda: press("/"))
buttoneql = Button(window, width=3, height=3, bd=0, text="=", command=lambda: equalpress())
buttonclr = Button(window, width=3, height=3, bd=0, text="AC", command=clear)
buttonpercentage = Button(window, width=3, height=3, bd=0, text="%", command=lambda: percent())
buttondecimal = Button(window, width=3, height=3, bd=0, text=".", command=lambda: press("."))
buttonnegative = Button(window, width=3, height=3, bd=0, text="+/-", command=lambda: sign_change())




button1.grid(row=8, column=0, sticky="EW")
button2.grid(row=8, column=1)
button3.grid(row=8, column=2)
button4.grid(row=7, column=0)
button5.grid(row=7, column=1)
button6.grid(row=7, column=2)
button7.grid(row=6, column=0)
button8.grid(row=6, column=1)
button9.grid(row=6, column=2)
button0.grid(row=9, column=0, columnspan=2, sticky="we")
buttonplus.grid(row=8, column=3)
buttonminus.grid(row=7, column=3)
buttonmult.grid(row=6, column=3)
buttondiv.grid(row=5, column=3)
buttoneql.grid(row=9, column=3)
buttonclr.grid(row=5, column=0)
buttonpercentage.grid(row=5, column=2)
buttondecimal.grid(row=9, column=2)
buttonnegative.grid(row=5, column=1)





window.mainloop()