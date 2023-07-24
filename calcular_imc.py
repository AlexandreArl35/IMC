from tkinter import *
import re

class Application:

    def __init__(self, master=None):

        self.fontePadrao = ("Arial", "10")
        self.Container_titulo = Frame(master)
        self.Container_titulo["pady"] = 10
        self.Container_titulo.pack()
        self.Container_titulo.configure(bg="blue")

        self.titulo = Label(self.Container_titulo, foreground="white", bg="blue", text="CALCULADORA DE IMC")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        self.Container_titulo.configure(bg="blue")

        self.Container_nome = Frame(master)
        self.Container_nome["padx"] = 25
        self.Container_nome.pack()
        self.Container_nome.configure(bg="blue")

        self.nomeLabel = Label(self.Container_nome, bg="blue",text="Nome             ",foreground="white", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        self.Container_nome.configure(bg="blue")

        self.nome = Entry(self.Container_nome, foreground="black")
        self.nome.focus()
        self.nome["width"] = 35
        self.nome["font"] = ("Arial", "10")
        self.nome.pack(side=LEFT)

        self.Container_altura = Frame(master)
        self.Container_altura["padx"] = 20
        self.Container_altura.pack()
        self.Container_altura.configure(bg="blue")

        self.alturaLabel = Label(self.Container_altura, bg="blue",text="Altura             ",foreground="white", font=self.fontePadrao)
        self.alturaLabel.pack(side=LEFT)
        self.Container_altura.configure(bg="blue")

        self.altura = Entry(self.Container_altura, foreground="black")
        self.altura.focus()
        self.altura["width"] = 35
        self.altura["font"] = ("Arial", "10")
        self.altura.pack(side=LEFT)

        self.Container_peso = Frame(master)
        self.Container_peso["padx"] = 20
        self.Container_peso.pack()
        self.Container_peso.configure(bg="blue")

        self.pesoLabel = Label(self.Container_peso, bg="blue",text="Peso              ",foreground="white", font=self.fontePadrao)
        self.pesoLabel.pack(side=LEFT)
        self.Container_peso.configure(bg="blue")

        self.peso = Entry(self.Container_peso, foreground="black")
        self.peso.focus()
        self.peso["width"] = 35
        self.peso["font"] = ("Arial", "10")
        self.peso.pack(side=LEFT)

        self.Container_botao = Frame(master)
        self.Container_botao["pady"] = 20
        self.Container_botao.pack()
        self.Container_botao.configure(bg="blue")

        self.autenticar = Button(self.Container_botao)
        self.autenticar["text"] = "Calcular"
        self.autenticar["font"] = ("Arial", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.exibir
        self.autenticar.pack()
        #self.Container_botao.configure(bg="blue")

        self.Container_msg = Frame(master)
        self.Container_msg["pady"] = 0
        self.Container_msg.pack()
        self.Container_msg.configure(bg="blue")
        
        self.mensagem = Label(self.Container_msg, bg="blue", foreground="white", font=self.fontePadrao)
        self.mensagem.pack()
        self.Container_msg.configure(bg="blue")

        self.Container_msg1 = Frame(master)
        self.Container_msg1["pady"] = 0
        self.Container_msg1.pack()
        self.Container_msg1.configure(bg="blue")

        self.mensagem1 = Label(self.Container_msg, bg="blue", foreground="white", font=self.fontePadrao)
        self.mensagem1.pack()
        self.Container_msg1.configure(bg="blue")

    def exibir(self):
        nome = self.nome.get()
        altura = self.altura.get()
        peso = self.peso.get()
    
        if nome == "" or float(peso) == "" or float(altura) == "":
            self.mensagem["text"] = "Campos não podem ficar em branco!!"
        else:    
            
         imc = float(peso) / float(altura)**2
         msg = "{:.2f}"

        if  imc <= 18.5:
                self.mensagem["text"] = "IMC : " + str(msg.format(imc))
                self.mensagem1["text"] = nome + " : Você está abaixo do peso !!\n" 
                #self.mensagem1["text"] = ("nome {}, seu {}, imc é {} ".format(nome, imc, texto))

        if  imc >= 18.6 <= 24.9:  
                self.mensagem["text"] = "IMC : " + str(msg.format(imc))
                self.mensagem1["text"] = nome + ": Seu Peso está normal !!\n"

        if  imc >= 25 <= 29.9:
                self.mensagem["text"] = "IMC : " + str(msg.format(imc))
                self.mensagem1["text"] = nome + ": Você está com Sobrepeso !!\n"

        if  imc >= 30 <= 34.9:
                self.mensagem["text"] = "IMC : " + str(msg.format(imc))
                self.mensagem1["text"] = nome + ": Você está com obsidade Grau 1\n"

        if  imc >= 35 <= 39.9:
                self.mensagem["text"] = "IMC : " + str(msg.format(imc))
                self.mensagem1["text"] = nome + ": Você está com obesidade Grau 2 (Severa) !!\n"

        if  imc >= 40:  
                self.mensagem["text"] = "IMC : " + str(msg.format(imc))
                self.mensagem1["text"] = nome + ": Você está com obesidade Grau 3 (Morbida) !!"


interface_imc = Tk()
interface_imc.title("")
Application()
interface_imc.geometry("500x250+200+200")
#interface_imc.wm_iconbitmap("favicon(1).ico")
interface_imc.configure(bg="blue")
interface_imc.mainloop()



