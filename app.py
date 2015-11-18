#coding: utf8

from  Tkinter import *
import sqlite3



db = sqlite3.connect("agenda.db")

cursor = db.cursor()


def gravar():
    nome = editNome.get()
    email = editEmail.get()
    telefone = editTelefone.get()

    cursor.execute("INSERT INTO CONTATO (NOME,EMAIL,TELEFONE) VALUES (?,?,?)",(nome,email,telefone))
    db.commit()

    editNome.delete(0,END)
    editEmail.delete(0,END)
    editTelefone.delete(0,END)

    addList()

def addList():
    listContatos.delete(0,END)
    contatos = cursor.execute("SELECT NOME,EMAIL,TELEFONE FROM CONTATO ORDER BY ID")
    for i in contatos:
        listContatos.insert(0,i)

janelaPrincipal = Tk()

janelaPrincipal.geometry("300x275+500+200")
janelaPrincipal.maxsize(width=300, height=275)
janelaPrincipal.maxsize(width=300, height=275)
janelaPrincipal.title("Agenda Telefonica")
janelaPrincipal["bg"] = "gray"

group = LabelFrame(janelaPrincipal, text="Dados do Contato")
group.grid()


labelNome = Label(group,text="Nome:")
labelNome.grid(row=1,column=1)

editNome = Entry(group)
editNome.grid(row=1,column=2)


labelEmail = Label(group,text="Email:")
labelEmail.grid(row=2,column=1)

editEmail = Entry(group)
editEmail.grid(row=2,column=2)

labelTelefone = Label(group,text="Telefone:")
labelTelefone.grid(row=3,column=1)

editTelefone = Entry(group)
editTelefone.grid(row=3,column=2)

btGravar = Button(group,text="Gravar" ,command = gravar)
btGravar.grid(row = 3,column=3)

btMostrar = Button(group,text="Mostrar" ,command = addList)
btMostrar.grid(row = 2,column=3)

yScroll = Scrollbar(group, orient=VERTICAL)
yScroll.grid(row=4, column = 4,sticky = N+S)

listContatos = Listbox(group,activestyle = "underline",yscrollcommand=yScroll.set)
listContatos.grid(row =4,column =1,sticky = N+S+E+W, columnspan = 3)
yScroll['command'] = listContatos.yview



janelaPrincipal.mainloop()
db.close()