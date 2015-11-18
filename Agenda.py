#coding: utf8



from  Tkinter import *
import sqlite3



db = sqlite3.connect("agenda.db")

cursor = db.cursor()

class Agenda ():
    def __init__(self):
        self.janelaPrincipal = Tk()

        self.janelaPrincipal.geometry("300x275+500+200")
        self.janelaPrincipal.maxsize(width=300, height=275)
        self.janelaPrincipal.maxsize(width=300, height=275)
        self.janelaPrincipal.title("Agenda Telefonica")
        self.janelaPrincipal["bg"] = "gray"

        self.group = LabelFrame(self.janelaPrincipal, text="Dados do Contato")
        self.group.grid()


        self.labelNome = Label(self.group,text="Nome:")
        self.labelNome.grid(row=1,column=1)

        self.editNome = Entry(self.group)
        self.editNome.grid(row=1,column=2)


        self.labelEmail = Label(self.group,text="Email:")
        self.labelEmail.grid(row=2,column=1)

        self.editEmail = Entry(self.group)
        self.editEmail.grid(row=2,column=2)

        self.labelTelefone = Label(self.group,text="Telefone:")
        self.labelTelefone.grid(row=3,column=1)

        self.editTelefone = Entry(self.group)
        self.editTelefone.grid(row=3,column=2)

        self.btGravar = Button(self.group,text="Gravar" ,command = self.gravar)
        self.btGravar.grid(row = 3,column=3)

        self.btMostrar = Button(self.group,text="Mostrar" ,command = self.addList)
        self.btMostrar.grid(row = 2,column=3)

        self.yScroll = Scrollbar(self.group, orient=VERTICAL)
        self.yScroll.grid(row=4, column = 4,sticky = N+S)

        self.listContatos = Listbox(self.group,activestyle = "underline",yscrollcommand=self.yScroll.set)
        self.listContatos.grid(row =4,column =1,sticky = N+S+E+W, columnspan = 3)
        self.yScroll['command'] = self.listContatos.yview



        self.janelaPrincipal.mainloop()
        db.close()



    def gravar(self):
        nome = self.editNome.get()
        email = self.editEmail.get()
        telefone = self.editTelefone.get()

        cursor.execute("INSERT INTO CONTATO (NOME,EMAIL,TELEFONE) VALUES (?,?,?)",(nome,email,telefone))
        db.commit()

        self.editNome.delete(0,END)
        self.editEmail.delete(0,END)
        self.editTelefone.delete(0,END)

        self.addList()

    def addList(self):
        self.listContatos.delete(0,END)
        contatos = cursor.execute("SELECT NOME,EMAIL,TELEFONE FROM CONTATO ORDER BY ID")
        for i in contatos:
            self.listContatos.insert(0,i)
