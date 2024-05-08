from tkinter import *
from tkinter import messagebox
import requests


root = Tk()





class Agendamento():
    def __init__(self):
        self.root = root
        self.frames_da_tela()
        self.tela()
        self.botoes()

    def tela(self):
        self.root.title("Agendamento")
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.5)

    def botoes(self):
        ##Botão de Cadastro de Agenda
        self.bt_agendamento = Button(self.frame_1, text="Agendamento")




class Menu():
    def __init__(self):
        self.root = root
        self.frames_da_tela()
        self.tela()
        self.botoes()

    def tela(self):
        self.root.title("Menu")
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.5)

    def botoes(self):
        ##Botão de Cadastro de Agenda
        self.bt_agendamento = Button(self.frame_1, text="Agendamento", command=Agendamento)
        self.bt_agendamento.place(relx=0.3, rely=0.2, relwidth=0.1, relheight=0.15)
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
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.5)

    def botoes(self):
        def login():
            userID = self.ent_id.get()
            senha = self.ent_senha.get()

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
        self.bt_ok.place(relx=0.3, rely=0.2, relwidth=0.1, relheight=0.15)

    def labelsAndEntry(self):
        ## Label ID
        self.lb_id = Label(self.frame_1, text="ID:")
        self.lb_id.place(relx=0.00, rely=0.05, relwidth=0.25, relheight=0.15)

        ## Entrada do ID
        self.ent_id = Entry(self.frame_1)
        self.ent_id.place(relx=0.05, rely=0.15, relwidth=0.25, relheight=0.15)

        ## Label da Senha
        self.lb_senha = Label(self.frame_1)
        self.lb_senha.place(relx=0.00, rely=0.4, relwidth=0.25, relheight=0.15)

        ##Entrada da senha;
        self.ent_senha = Entry(self.frame_1, show="*")
        self.ent_senha.place(relx=0.05, rely=0.55, relwidth=0.25, relheight=0.15)


def Page(page=Application):
    page()
    root.mainloop()


Page()
