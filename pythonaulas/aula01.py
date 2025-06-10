

from tkinter import *
from tkinter import ttk

# Definindo cores
cor1 = "#020203"  # preto
cor2 = "#e4e4eb"  # branco
cor3 = "#252f5c"  # azul
cor4 = "#797985"  # cinza
cor5 = "#eb6010"  # laranja

Janela = Tk()
Janela.title("Calculadora")
Janela.geometry("235x310")
Janela.config(bg=cor1)

# Criando a tela
frame_tela = Frame(Janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(Janela, width=235, height=265)
frame_corpo.grid(row=1, column=0)







# Criando label
app_label = Label (frame_tela, text='123456789', width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'))
app_label.place(x=0,y=0)







# Criando os botões
button1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button1.place(x=0, y=0)

button2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button2.place(x=118, y=0)

button3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button3.place(x=177, y=0)

button4 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button4.place(x=0, y=52)

button5 = Button(frame_corpo, text="8", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button5.place(x=59, y=52)

button6 = Button(frame_corpo, text="9", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button6.place(x=118, y=52)

button7 = Button(frame_corpo, text="4", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button7.place(x=0, y=104)

button8 = Button(frame_corpo, text="5", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button8.place(x=59, y=104)

button9 = Button(frame_corpo, text="6", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button9.place(x=118, y=104)

button10 = Button(frame_corpo, text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button10.place(x=177, y=52)

button11 = Button(frame_corpo, text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button11.place(x=177, y=104)

button12 = Button(frame_corpo, text="1", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button12.place(x=0, y=156)

button13 = Button(frame_corpo, text="2", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button13.place(x=59, y=156)

button14 = Button(frame_corpo, text="3", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button14.place(x=118, y=156)

button15 = Button(frame_corpo, text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button15.place(x=177, y=156)

button16 = Button(frame_corpo, text="0", width=11, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button16.place(x=0, y=208)

button17 = Button(frame_corpo, text=".", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button17.place(x=118, y=208)

button18 = Button(frame_corpo, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'), relief=RAISED, overrelief=RIDGE)
button18.place(x=177, y=208)




















Janela.mainloop()