from tkinter import *
from tkinter import ttk, Tk

tk = Tk()
tk.title('Calcutor py')
tk.geometry('400x600+720+200')
tk.resizable(False, False)

label = Label(text = 'OnePailas', font = ('Arial', 14))
label.pack()

def active_entry(entry_widget):
    entry_widget.focus_set()

def finish():
    tk.destroy()
    print('Завершение сеанса')
tk.protocol('WM_DELETE_WINDOW', finish)

def pl_and_mn():
    en = str(entry.get())
    if en == '1 / ' or en == '0.' or en == ' - ' or en.count(' - ') > 1:
        entry.insert(END, '')
    else:
        entry.insert(END, ' - ')

def null():
    if str(entry.get()) == '1 / ':
        entry.insert(END, '')
    else:
        entry.insert(END, '0')

def tochka():
    en = str(entry.get())
    if en == '':
        entry.insert(END, '0.')
    elif en == ' - ' or en == '1 / ' or en.count('.') > 2 or en == '0.':
        entry.insert(END, '')
    else:
        entry.insert(END, '.')

def btn_res():
    result = eval(entry.get())
    print(result)
    entry.delete(0, END)
    entry.insert(0, result)

def button_1():
    entry.insert(END, '1')
    en = str(entry.get())
    if en[0] == '0' and en[1] != '.':
        entry.delete(0, END)
        entry.insert(END, '1')
    
def btn_2():
    entry.insert(END, '2')
    en = str(entry.get())
    if en[0] == '0' and en[1] != '.':
        entry.delete(0, END)
        entry.insert(END, '2')

def btn_3():
    entry.insert(END, '3')
    en = str(entry.get())
    if en[0] == '0' and en[1] != '.':
        entry.delete(0, END)
        entry.insert(END, '3')

def btn_plus():
    en = str(entry.get())
    if en[1] == '+' or en.count('+') > 1 or en == '1 / ' or en == ' - ' or en == '0.':
        entry.insert(END, '')
    else:
        entry.insert(END, ' + ')

def btn_4():
    entry.insert(END, '4')
    en = str(entry.get())
    if en[0] == '0' and en[1] != '.':
        entry.delete(0, END)
        entry.insert(END, '4')

def btn_5():
    entry.insert(END, '5')
    en = str(entry.get())
    if en[0] == '0' and en[1] != '.':
        entry.delete(0, END)
        entry.insert(END, '5')

def btn_6():
    entry.insert(END, '6')
    en = str(entry.get())
    if en[0] == '0' and en[1] != '.':
        entry.delete(0, END)
        entry.insert(END, '6')

def btn_minus():
    en = str(entry.get())
    if en == ' - ' or en.count('-') >= 2 or en == '1 / ' or en == '0.':
        entry.insert(END, '')
    else:
        entry.insert(END, ' - ')

def btn_7():
    entry.insert(END, '7')
    en = str(entry.get())
    if en[0] == '0' and en[1] != '.':
        entry.delete(0, END)
        entry.insert(END, '7')

def btn_8():
    entry.insert(END, '8')
    en = str(entry.get())
    if en[0] == '0' and en[1] != '.':
        entry.delete(0, END)
        entry.insert(END, '8')

def btn_9():
    entry.insert(END, '9')
    en = str(entry.get())
    if en[0] == '0' and en[1] != '.':
        entry.delete(0, END)
        entry.insert(END, '9')

def btn_multipy():
    en = str(entry.get())
    if en == '' or en.count('*') >= 1 or en == '1 / ' or en == ' - ' or en == '0.':
        entry.insert(END, '')
    else:
        entry.insert(END, ' * ')

def one_and_x():
    en = str(entry.get())
    if en == '':
        entry.insert(END, '1 / ')
    elif en != '' or en.count('1 / ') > 0:
        entry.delete(0, END)
        entry.insert(END, '1 / ')
    else:
        entry.insert(END, '1 / ')

def x_stepen():
    en = str(entry.get())
    if en == '' or en.count(' ** ') > 0 or en == '1 / ' or en == ' - ' or en == '0.':
        entry.insert(END, '')
    else: 
        entry.insert(END, ' ** ')


def koren():
    en = str(entry.get())
    if en == '1 / ' or en == '' or en == ' - ' or en == '0.':
        entry.insert(END, '')
    else:
        entry.insert(END, ' ** 0.5')
        if en.count(' ** 0.5') > 0:
            entry.delete(END, '')

def div():
    en = str(entry.get())
    if en == '' or en.count(' / ') > 0 or en == '1 / ' or en == ' - ' or en == '0.':
        entry.insert(END, '')
    else:
        entry.insert(END, ' / ')

def btn_ce():
    entry.delete(0, END)

def button_clear():
    entry.delete(0, END)

def btn_backs():
    en = str(entry.get())
    entry.delete(0, END)
    entry.insert(END, en[0:-1])

entry = ttk.Entry(text = '0', font = ('Arial', 20), justify = RIGHT)
entry.pack(anchor = W, fill = X, ipady = 42)
active_entry(entry)

button = ttk.Button(text = '+/-', command = pl_and_mn)
button.place(x = 0, y = 525, width = 100, height = 75)

button0 = ttk.Button(text = '0', command = null)
button0.place(x = 100, y = 525, width = 100, height = 75)

button_comma = ttk.Button(text = '.', command = tochka)
button_comma.place(x = 200, y = 525, width = 100, height = 75)

button_result = ttk.Button(text = '=', command = btn_res)
button_result.place(x = 300, y = 525, width = 100, height = 75)

button1 = ttk.Button(text = '1', command = button_1)
button1.place(x = 0, y = 450, width = 100, height = 75)

button2 = ttk.Button(text = '2', command = btn_2)
button2.place(x = 100, y = 450, width = 100, height = 75)

button3 = ttk.Button(text = '3', command = btn_3)
button3.place(x = 200, y = 450, width = 100, height = 75)

button_plus = ttk.Button(text = '+', command = btn_plus)
button_plus.place(x = 300, y = 450, width = 100, height = 75)

button4 = ttk.Button(text = '4', command = btn_4)
button4.place(x = 0, y = 375, width = 100, height = 75)

button5 = ttk.Button(text = '5', command = btn_5)
button5.place(x = 100, y = 375, width = 100, height = 75)

button6 = ttk.Button(text = '6', command = btn_6)
button6.place(x = 200, y = 375, width = 100, height = 75)

button_minus = ttk.Button(text = '-', command = btn_minus)
button_minus.place(x = 300, y = 375, width = 100, height = 75)

button7 = ttk.Button(text = '7', command = btn_7)
button7.place(x = 0, y = 300, width = 100, height = 75)

button8 = ttk.Button(text = '8', command = btn_8)
button8.place(x = 100, y = 300, width = 100, height = 75)

button9 = ttk.Button(text = '9', command = btn_9)
button9.place(x = 200, y = 300, width = 100, height = 75)
    
button_multiply = ttk.Button(text = '*', command = btn_multipy)
button_multiply.place(x = 300, y = 300, width = 100, height = 75)

button_1_and_x = ttk.Button(text = '1/x', command = one_and_x)
button_1_and_x.place(x = 0, y = 225, width = 100, height = 75)

button_x_kvadrat = ttk.Button(text = 'x^x', command = x_stepen)
button_x_kvadrat.place(x = 100, y = 225, width = 100, height = 75)

button_x_koren = ttk.Button(text = '√x', command = koren)
button_x_koren.place(x = 200, y = 225, width = 100, height = 75)

button_divide = ttk.Button(text = '/', command = div)
button_divide.place(x = 300, y = 225, width = 100, height = 75)

button_ce = ttk.Button(text = 'CE', command = btn_ce)
button_ce.place(x = 0, y = 150, width = 100, height = 75)

button_c = ttk.Button(text = 'C', command = button_clear)
button_c.place(x = 100, y = 150, width = 100, height = 75)

button_delete = ttk.Button(text = '⌫', command = btn_backs)
button_delete.place(x = 200, y = 150, width = 200, height = 75)

ttk.Style().configure('.', font = ('Arial', 16), foreground = 'black')

tk.mainloop()
