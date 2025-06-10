from tkinter import *

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

# Variável para armazenar os valores digitados
todos_valores = ''

# Flag para controlar se o último texto exibido foi resultado
resultado_exibido = False

# Criando label
valor_texto = StringVar()

# criando funcao para entrar valores
def entrar_valores(event):
    global todos_valores, resultado_exibido
    if resultado_exibido:
        # Se o último exibido foi resultado e o usuário digitar número ou ponto, reinicia a tela
        if event in '0123456789.':
            todos_valores = str(event)
        else:
            # Se for operador, continua concatenando ao resultado
            todos_valores += str(event)
        resultado_exibido = False
    else:
        todos_valores += str(event)
    valor_texto.set(todos_valores)

#funcao para calcular
def calcular():
    global todos_valores, resultado_exibido
    try:
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
        resultado_exibido = True  # sinaliza que resultado está na tela
    except:
        valor_texto.set("Erro")
        todos_valores = ""
        resultado_exibido = False

#funcao limpar tela
def limpar_tela():
    global todos_valores, resultado_exibido
    todos_valores = ""
    resultado_exibido = False
    valor_texto.set("")

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7,
                  relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy', 18), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# Criando os botões
button1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy', 13, 'bold'),
                 relief=RAISED, overrelief=RIDGE)
button1.place(x=0, y=0)

button2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'),
                 relief=RAISED, overrelief=RIDGE)
button2.place(x=118, y=0)

button3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'),
                 relief=RAISED, overrelief=RIDGE)
button3.place(x=177, y=0)

button4 = Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'),
                 relief=RAISED, overrelief=RIDGE)
button4.place(x=0, y=52)

button5 = Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'),
                 relief=RAISED, overrelief=RIDGE)
button5.place(x=59, y=52)

button6 = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'),
                 relief=RAISED, overrelief=RIDGE)
button6.place(x=118, y=52)

button10 = Button(frame_corpo, command=lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'),
                  relief=RAISED, overrelief=RIDGE)
button10.place(x=177, y=52)

button7 = Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'),
                 relief=RAISED, overrelief=RIDGE)
button7.place(x=0, y=104)

button8 = Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'),
                 relief=RAISED, overrelief=RIDGE)
button8.place(x=59, y=104)

button9 = Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'),
                 relief=RAISED, overrelief=RIDGE)
button9.place(x=118, y=104)

button11 = Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'),
                  relief=RAISED, overrelief=RIDGE)
button11.place(x=177, y=104)

button12 = Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'),
                  relief=RAISED, overrelief=RIDGE)
button12.place(x=0, y=156)

button13 = Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'),
                  relief=RAISED, overrelief=RIDGE)
button13.place(x=59, y=156)

button14 = Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'),
                  relief=RAISED, overrelief=RIDGE)
button14.place(x=118, y=156)

button15 = Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'),
                  relief=RAISED, overrelief=RIDGE)
button15.place(x=177, y=156)

button16 = Button(frame_corpo, command=lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy', 13, 'bold'),
                  relief=RAISED, overrelief=RIDGE)
button16.place(x=0, y=208)

button17 = Button(frame_corpo, command=lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'),
                  relief=RAISED, overrelief=RIDGE)
button17.place(x=118, y=208)

button18 = Button(frame_corpo, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'),
                  relief=RAISED, overrelief=RIDGE, command=calcular)
button18.place(x=177, y=208)

Janela.mainloop()
