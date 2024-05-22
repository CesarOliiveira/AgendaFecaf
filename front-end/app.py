from tkinter import *
import tkinter as tk
from tkinter import messagebox
import requests


root = Tk()





class Agendamento():
    def __init__(self):
        self.root = root
        self.frames_da_tela()
        self.tela()
        self.botoes()
        self.labelsAndEntrys()


    def tela(self):
        self.root.title("Agendamento")
        self.root.geometry("1440x1020")
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.95)

        self.frame_2 = Frame(self.frame_1)
        self.frame_2.place(relx=0.25, rely=0.25, relwidth=0.7, relheight=0.6)
        self.frame_2.configure(bg="red")

    def botoes(self):
        # Botão de Voltar
        self.bt_voltar = Button(self.frame_1, text="Voltar", command=lambda: Page(Menu))
        self.bt_voltar.place(relx=0.01, rely=0.02, width=50, height=35)


    def labelsAndEntrys(self):

        options = [
            "Análise e Desenvolvimento de Sistemas",
            "Psicologia",
            "Direito",
            "Financeiro"
        ]
        clicked = StringVar()

        clicked.set("Curso")

        ##Entry nome do professor
        ## Entrada do ID
        self.ent_professor = Entry(self.frame_2)

        self.ent_professor.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.drop_disciplina = OptionMenu(self.frame_2, clicked, *options)
        self.drop_disciplina.grid(row=1, column=0)







class Menu():
    def __init__(self):
        self.root = root
        self.frames_da_tela()
        self.tela()
        self.botoes()

    def tela(self):
        self.root.title("Menu")
        self.root.geometry("1440x1020")
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.95)


    def botoes(self):

        ##Botão de Cadastro de Agenda
        self.bt_agendamento = Button(self.frame_1, text="Agendamento", command=lambda: {self.frame_1.destroy(), Page(Agendamento)})
        self.bt_agendamento.place(relx=0.1, rely=0.2, relwidth=0.1, relheight=0.15)
        self.bt_agendamento.grid(row=0, column=0)

        ##Botão de Cadastro de Agenda
        self.bt_consulta = Button(self.frame_1, text="Consulta")
        self.bt_consulta.place(relx=0.3, rely=0.2, relwidth=0.1, relheight=0.15)
        self.bt_consulta.grid(row=0, column=1, padx=20)







class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes()
        self.labelsAndEntry()

    def tela(self):
        self.root.title("Login")
        self.root.configure(background='#1e3743')
        self.root.geometry("788x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=1440, height=720)
        self.root.minsize(width=400, height=300)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.95)

    def botoes(self):
        def login():
            userID = self.ent_id.get()
            senha = self.ent_senha.get()

            if userID == '':
                return messagebox.showerror(title="Login", message="Usuario não pode estar vázio!")
            elif senha == '':
                return messagebox.showerror(title="Login", message="Senha não pode estar vázio!")


            userID = int(userID)


            data = {"id": userID, "senha": senha}

            link = 'http://127.0.0.1:5000/authentic'

            requestResponse = requests.post(link, json=data)
            request_json = requestResponse.json()

            print(requestResponse)
            print(requestResponse.json())

            bdUser = request_json['Authenticate']['code']

            if bdUser == 0:
                messagebox.showerror(title="Login", message="Usuario ou Senha incorretos.")
            elif bdUser == 1:
                messagebox.showinfo(title="Login", message="Logado com Sucesso.")

                Page(Menu)
            else:
                messagebox.showwarning(title="Login", message="Algo de Errado aconteceu.")


        ##Botão de entrada
        self.bt_ok = Button(self.frame_1, text="Entrar", command=login)
        self.bt_ok.place(relx=0.3, rely=0.2, width=85, height=35)

    def labelsAndEntry(self):
        ## Label ID
        self.lb_id = Label(self.frame_1, text="ID:")
        self.lb_id.place(relx=0.00, rely=0.05, relwidth=0.25, relheight=0.15)
        self.lb_id.grid(row=0, column=0)

        ## Entrada do ID
        self.ent_id = Entry(self.frame_1)
        self.ent_id.place(relx=0.05, rely=0.15, relwidth=0.25, height=35)
        self.lb_id.grid(row=0, column=1)

        ## Label da Senha
        self.lb_senha = Label(self.frame_1)
        self.lb_senha.place(relx=0.00, rely=0.4, relwidth=0.25, relheight=0.15)
        self.lb_id.grid(row=0, column=2)

        ##Entrada da senha;
        self.ent_senha = Entry(self.frame_1, show="*")
        self.ent_senha.place(relx=0.05, rely=0.55, relwidth=0.25, height=35)
        self.lb_id.grid(row=0, column=3)



def Page(page):
    page()
    root.mainloop()


Page(Application)
