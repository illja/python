from tkinter import *
import parser
import math

root=Tk()
root.title('My_Calculator')

i = 0


def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

def clear_all():
    display.delete(0, END)


def calculate():
    whole_string = display.get()
    try:
        formula = parser.expr(whole_string).compile()
        result = eval(formula)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i += length

def btnSqrt():
    whole_string = display.get()
    try:
        formula = parser.expr(whole_string).compile()
        result = math.sqrt(formula)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")


display = Entry(root, font = ("Calibri", 13))
display.grid(row = 1, columnspan = 6    , sticky = W+E)



btn7 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text="7", command = lambda : get_variables(7)).grid(
    row=2, column=0)
btn8 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='8', command = lambda : get_variables(8)).grid(
    row=2, column=1)
btn9 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='9', command = lambda : get_variables(9)).grid(
    row=2, column=2)
Addition = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='+',
                  command=lambda: get_operation('+')).grid(row=3, column=3)
bracket_1 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='(',
                  command=lambda: get_operation('(')).grid(row=2, column=5)
bracket_2 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text=')',
                  command=lambda: get_operation(')')).grid(row=3, column=5)
Func_1 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='√', command= lambda:get_operation("")).grid(row=2,column=4)
# -------------------------------------------------------------------------------------------------------------------------

btn4 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='4', command=lambda: get_variables(4)).grid(
    row=3, column=0)
btn5 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='5', command=lambda: get_variables(5)).grid(
    row=3, column=1)
btn6 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='6', command=lambda: get_variables(6)).grid(
    row=3, column=2)
Subtraction = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='-',command=lambda: get_operation('-')).grid(row=2, column=3)
Func_2 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text="exp",command=lambda :get_operation("**")).grid(row=3,column=4)
# -------------------------------------------------------------------------------------------------------------------------

btn1 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='1', command=lambda: get_variables(1)).grid(
    row=4, column=0)
btn2 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='2', command=lambda: get_variables(2)).grid(
    row=4, column=1)
btn3 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='3', command=lambda: get_variables(3)).grid(
    row=4, column=2)
Multiple = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='*',command=lambda: get_operation('*')).grid(row=4, column=3)
#Func_3 = Button(root, padx=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='Q', command=lambda: get_variables(7)).grid(row=4, column=4)
# -------------------------------------------------------------------------------------------------------------------------

btn0 = Button(root, padx=10, bd=8, pady=10, fg="black", font=('arial', 20, 'bold'), text='0',command=lambda: get_variables(0)).grid(row=5, column=0)
btnClear = Button(root, padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='C',command=clear_all).grid(row=5, column=1)
btnEquals = Button(root, padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='=',command=calculate).grid(row=5, column=2)
Division = Button(root, padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='/',command=lambda: get_operation('/')).grid(row=5, column=3)
Func_4 = Button(root, padx=10, pady=10, bd=8, fg="black", font=('arial', 20, 'bold'), text='Q',command=lambda: get_variables(7)).grid(row=5, column=4)

root.mainloop()
