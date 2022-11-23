from tkinter import *
from tkinter import messagebox
def clica_botao():
    messagebox.showinfo("Parabéns",'Bem vindo de volta')

janela = Tk()
frame1 = Frame(janela)
frame1.pack()
botao = Button(frame1,text="Aceitar", command=clica_botao)
botao['width'] = 5
botao['height'] = 5
botao.pack(side=LEFT)
botao2 = Button(frame1, text="Desistir")
botao2.pack(side=RIGHT)
botao2['width'] = 5
botao2['height'] = 5
janela.mainloop()