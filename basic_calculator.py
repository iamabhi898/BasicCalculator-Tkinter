from tkinter import *

# initialization
root = Tk()
# caption (window title)
root.title("BASIC CALCULATOR")

# ENTRY
entry = Entry(root, borderwidth=4, width=35)
entry.grid(row=0, column=0, columnspan=4, pady=20)
entry.insert(0, '0')

# button padding
btn_padx = 7
btn_pady = 20

######### FUNCITONS ###########

def btn_click(num):
	previous_num = entry.get()
	entry.delete(0, END)
	entry.insert(0, previous_num + num)

def add():
	f_num = entry.get()
	global first_num
	first_num = float(f_num)
	entry.delete(0, END)
	global sign_switch
	sign_switch = 'add'

def sub():
	f_num = entry.get()
	global first_num
	first_num = float(f_num)
	entry.delete(0, END)
	global sign_switch 
	sign_switch = 'sub'

def mul():
	f_num = entry.get()
	global first_num
	first_num = float(f_num)
	entry.delete(0, END)
	global sign_switch
	sign_switch = 'mul'

def div():
	f_num = entry.get()
	global first_num
	first_num = float(f_num)
	entry.delete(0, END)
	global sign_switch
	sign_switch = 'div'	

def bck_spc():
	current_num = entry.get()
	str_len = len(current_num)
	if str_len >= 1:
		current_num = current_num[0 : -1]
		entry.delete(0, END)
		entry.insert(0, current_num) 

def clr():
	entry.delete(0, END)

def clr_all():
	entry.delete(0, END)
	global first_num
	first_num = 0

def eql():
	
	if sign_switch == 'add':
		result = first_num + float(entry.get())
		entry.delete(0, END)
		entry.insert(0, result)
	elif sign_switch == 'sub':
		result = first_num - float(entry.get())
		entry.delete(0, END)
		entry.insert(0, result)
	elif sign_switch == 'mul':
		result = first_num * float(entry.get())
		entry.delete(0, END)
		entry.insert(0, result)
	elif sign_switch == 'div':
		result = first_num / float(entry.get())
		entry.delete(0, END)
		entry.insert(0, result) 

###############################

########## BUTTONS ############

# Row $1
button_CE = Button(root, text="CE", width=btn_padx, pady=btn_pady, bg='#ff5e5e', command=clr_all)
button_C = Button(root, text="C", width=btn_padx, pady=btn_pady, bg='#99b8ff', command=clr)
button_bksp = Button(root, text="<x", width=btn_padx, pady=btn_pady, bg='#99b8ff', command=bck_spc)
button_div = Button(root, text="%", width=btn_padx, pady=btn_pady, bg='#47ed6e', command=div)

# Row $2
button_7 = Button(root, text="7", width=btn_padx, pady=btn_pady, bg='#fab97f', command=lambda: btn_click('7'))
button_8 = Button(root, text="8", width=btn_padx, pady=btn_pady, bg='#fab97f', command=lambda: btn_click('8'))
button_9 = Button(root, text="9", width=btn_padx, pady=btn_pady, bg='#fab97f', command=lambda: btn_click('9'))
button_mul = Button(root, text= "x", width=btn_padx, pady=btn_pady, bg='#47ed6e', command=mul)

# Row $3
button_4 = Button(root, text="4", width=btn_padx, pady=btn_pady, bg='#fab97f', command=lambda: btn_click('4'))
button_5 = Button(root, text="5", width=btn_padx, pady=btn_pady, bg='#fab97f', command=lambda: btn_click('5'))
button_6 = Button(root, text="6", width=btn_padx, pady=btn_pady, bg='#fab97f', command=lambda: btn_click('6'))
button_sub = Button(root, text="-", width=btn_padx, pady=btn_pady, bg='#47ed6e', command=sub)

# Row $4
button_1 = Button(root, text="1", width=btn_padx, pady=btn_pady, bg='#fab97f', command=lambda: btn_click('1'))
button_2 = Button(root, text="2", width=btn_padx, pady=btn_pady, bg='#fab97f', command=lambda: btn_click('2'))
button_3 = Button(root, text="3", width=btn_padx, pady=btn_pady, bg='#fab97f', command=lambda: btn_click('3'))
button_add = Button(root, text="+", width=btn_padx, pady=btn_pady, bg='#47ed6e', command=add)

# Row $5
button_0 = Button(root, text="0", width=btn_padx*2+1, pady=btn_pady, bg='#becc56', command=lambda: btn_click('0'))
button_dot = Button(root, text=".", width=btn_padx, pady=btn_pady, bg='#99b8ff', command=lambda: btn_click('.'))
button_eql = Button(root, text="=", width=btn_padx, pady=btn_pady, bg='#3b3b3b', fg='#ffffff', command=eql)

####################################

######## putting on screen  ########

# row 1
button_CE.grid(row=1, column=0)
button_C.grid(row=1, column=1)
button_bksp.grid(row=1, column=2)
button_div.grid(row=1, column=3)

# row 2
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

# row 3
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

# row 4
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

# row 5
button_0.grid(row=5, column=0, columnspan=2)
button_dot.grid(row=5, column=2)
button_eql.grid(row=5, column=3)

####################################

# looping
root.mainloop()