from tkinter import*
from tkinter import messagebox
from datetime import datetime

import pyshorteners


janela = Tk()
janela.title('qualquer coisa')
janela.geometry('600x450')
janela['bg'] = 'white'

def encurtarURL():
    if url.get() == '':
        messagebox.showerror('erro','preencha o campo!')

    else:
        urlOriginal = url.get()
        encurtador = pyshorteners.Shortener()
        novaUrl = encurtador.tinyurl.short(urlOriginal)

        resultado.delete(0, END)
        resultado.insert(0, novaUrl)






titulo = Label(janela, text='shortener', font='Verdana 15 bold', bg='white', fg='purple')
titulo.place(x=200, y=5)

data = Label(janela, text=datetime.now().date(), fg='purple', font='Verdana 15 bold')
data.place(x=365, y=5)

texto = Label(janela, text='Insira a URL....', font='Verdana 12 bold', fg='purple')
texto.place(x=50, y=50)

url = Entry(janela,width=40, bg='lightgrey', font='Verdana 12 bold', relief=GROOVE, borderwidth=2, border=2)
url.place(x=50, y=80)

botao = Button(janela, relief=GROOVE, text='criar', font='Verdana 10 bold',bg='purple', fg='white', command=encurtarURL)
botao.place(x=500, y=77)


resultado = Entry(janela,font='Verdana 10 bold', fg='purple', width=30, relief=GROOVE, borderwidth=2, border=2)
resultado.place(x=130, y=120)

janela.mainloop()

