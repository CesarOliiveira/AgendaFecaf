from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from menu import Menu

import requests

root = Tk()




class Consulta():
    def __init__(self):
        self.root = root
        self.frames_da_tela()
        self.tela()
        self.botoes()
        self.lista_frame()

        self.listaCli.delete(*self.listaCli.get_children())

        link = 'http://127.0.0.1:5000/agendamento'

        requestResponse = requests.get(link)
        lista = requestResponse.json()

        resultado = lista['Agendamento']

        for i in resultado:
            self.listaCli.insert("", END, values=(i['id'], i['professor'], i['materia'], i['laboratorio'], i['data']))


    def tela(self):
        self.root.geometry("1440x1020")
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.95)

    def lista_frame(self):
        self.listaCli = ttk.Treeview(self.frame_1, height=3, column=("col1", "col2", "col3", "col4", "col5"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="ID")
        self.listaCli.heading("#2", text="Professor")
        self.listaCli.heading("#3", text="Disciplina")
        self.listaCli.heading("#4", text="Laboratorio")
        self.listaCli.heading("#5", text="Data")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=2)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)
        self.listaCli.column("#5", width=125)

        self.scroolLista = Scrollbar(self.frame_1, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

    def botoes(self):
        # Botão de Voltar
        self.bt_voltar = Button(self.frame_1, text="Voltar", command=lambda: {self.frame_1.destroy(), Page(Menu)})
        self.bt_voltar.place(relx=0.01, rely=0.02, width=50, height=35)




class Agendamento():
    def __init__(self):
        self.root = root
        self.frames_da_tela()
        self.tela()
        self.botoes()
        self.labelsAndEntrys()

    def tela(self):
        self.root.geometry("1440x1020")
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.95)

    def botoes(self):
        # Botão de Voltar
        self.bt_voltar = Button(self.frame_1, text="Voltar", command=lambda: {self.frame_1.destroy(), Page(Menu)})
        self.bt_voltar.place(relx=0.01, rely=0.02, width=50, height=35)




    def labelsAndEntrys(self):
        def professor_focus_in(event):
            if self.ent_professor.get() == "Professor":
                self.ent_professor.delete(0, 'end')
                self.ent_professor.config(fg="Black")

        def professor_focus_out(event):
            if self.ent_professor.get() == "":
                self.ent_professor.insert(0, "Professor")

        def data_focus_in(event):
            if self.ent_data.get() == "00/00/00":
                self.ent_data.delete(0, 'end')
                self.ent_data.config(fg="Black")

        def data_focus_out(event):
            if self.ent_data.get() == "":
                self.ent_data.insert(0, "00/00/00")


        disciplinas = [
            "Análise e Desenvolvimento de Sistemas",
            "Psicologia",
            "Direito",
            "Financeiro"
        ]

        laboratorios = [
            "Laboratório 1",
            "Laboratório 2",
            "Laboratório Quimica",
            "Sala 12"
        ]

        clickedDisciplinas = StringVar()
        clickedDisciplinas.set("Curso")

        clickedLaboratorios = StringVar()
        clickedLaboratorios.set("Laboratorios")

        ##Entry nome do professor
        ## Entrada do ID
        self.ent_professor = Entry(self.frame_1, font=("Helvetica", 13), fg="Gray")


        self.ent_professor.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.ent_professor.place(relx=0.1, rely=0.15, relwidth=0.2, height=40)
        self.ent_professor.insert(0, "Professor")
        self.ent_professor.bind("<FocusIn>", professor_focus_in)
        self.ent_professor.bind("<FocusOut>", professor_focus_out)



        ## Disciplinas
        self.drop_disciplina = OptionMenu(self.frame_1, clickedDisciplinas, *disciplinas)
        self.drop_disciplina.place(relx=0.4, rely=0.15, relwidth=0.2, height=50)

        ## Laboratorios
        self.drop_laboratorios = OptionMenu(self.frame_1, clickedLaboratorios, *laboratorios)
        self.drop_laboratorios.place(relx=0.1, rely=0.23, relwidth=0.2, height=50)

        self.ent_data = Entry(self.frame_1, font=("Helvetica", 13), fg="Gray")
        self.ent_data.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.ent_data.place(relx=0.4, rely=0.23, relwidth=0.2, height=40)
        self.ent_data.insert(0, "00/00/00")
        self.ent_data.bind("<FocusIn>", data_focus_in)
        self.ent_data.bind("<FocusOut>", data_focus_out)

        def agendardia():
            professor = self.ent_professor.get()
            disciplina = clickedDisciplinas.get()
            laboratorio = clickedLaboratorios.get()
            agendamentodata = self.ent_data.get()

            if professor == '':
                return messagebox.showerror(title="Agendamento", message="Professor não pode estar vázio!")
            elif disciplina == '':
                return messagebox.showerror(title="Agendamento", message="Disciplina não pode estar vázio!")
            elif laboratorio == '':
                return messagebox.showerror(title="Agendamento", message="Laboratorio não pode estar vázio!")
            elif agendamentodata == '':
                return messagebox.showerror(title="Agendamento", message="Data não pode estar vázio!")


            data = {"professor": professor, "materia": disciplina, "laboratorio": laboratorio, "data": agendamentodata}

            link = 'http://127.0.0.1:5000/agendamento'

            requestResponse = requests.post(link, json=data)
            request_json = requestResponse.json()

            code = request_json['Agendamento']['code']

            mensagem = request_json['mensagem']

            if code == 1:
                messagebox.showinfo(title="Agendamento", message=mensagem)
            else:
                messagebox.showerror(title="Agendamento", message="Algo de errado aconteceu.")



        # Botão Enviar
        self.bt_ok = Button(self.frame_1, text="Enviar", command=lambda: agendardia())
        self.bt_ok.place(relx=0.55, rely=0.5, width=70, height=40)



class Menu():
    def __init__(self):
        self.root = root
        self.frames_da_tela()
        self.tela()
        self.botoes()

    def tela(self):
        self.root.geometry("1440x1020")
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.95)


    def botoes(self):

        ##Botão de Cadastro de Agenda
        self.bt_agendamento = Button(self.frame_1, text="Agendamento", command=lambda: {self.frame_1.destroy(), Page(Agendamento)})
        self.bt_agendamento.place(relx=0.35, rely=0.4, relwidth=0.1, relheight=0.15)


        ##Botão de Cadastro de Agenda
        self.bt_consulta = Button(self.frame_1, text="Consulta", command=lambda: {self.frame_1.destroy(), Page(Consulta)})
        self.bt_consulta.place(relx=0.55, rely=0.4, relwidth=0.1, relheight=0.15)








class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes()
        self.labelsAndEntry()



    def tela(self):
        self.root.title("LabPlanner")
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
        self.bt_ok.place(relx=0.41, rely=0.65, width=85, height=35)

    def labelsAndEntry(self):

        def id_focus_in(event):
            if self.ent_id.get() == "ID":
                self.ent_id.delete(0, 'end')
                self.ent_id.config(fg="Black")

        def id_focus_out(event):
            if self.ent_id.get() == "":
                self.ent_id.insert(0, "ID")

        def password_focus_in(event):
            if self.ent_senha.get() == "Senha":
                self.ent_senha.delete(0, 'end')
                self.ent_senha.config(fg="Black", show="*")

        def password_focus_out(event):
            if self.ent_senha.get() == "":
                self.ent_senha.insert(0, "Senha")
                self.ent_senha.config(show="")



        ## Label ID
        self.lb_id = Label(self.frame_1, font=("Helvetica", 24, "bold"), fg="Blue", text="FePlani")
        self.lb_id.place(relx=0.40, rely=0.15)



        ## Entrada do ID
        self.ent_id = Entry(self.frame_1, font=("Helvetica", 13), fg="Gray")
        self.ent_id.place(relx=0.35, rely=0.35, relwidth=0.25, height=35)
        self.ent_id.insert(0, "ID")
        self.ent_id.bind("<FocusIn>", id_focus_in)
        self.ent_id.bind("<FocusOut>", id_focus_out)


        ## Label da Senha
        self.lb_senha = Label(self.frame_1)
        self.lb_senha.place(relx=0.00, rely=0.4, relwidth=0.25, relheight=0.15)


        ##Entrada da senha;
        self.ent_senha = Entry(self.frame_1, font=("Helvetica", 13), fg="Gray")
        self.ent_senha.place(relx=0.35, rely=0.5, relwidth=0.25, height=35)
        self.ent_senha.insert(0, "Senha")
        self.ent_senha.bind("<FocusIn>", password_focus_in)
        self.ent_senha.bind("<FocusOut>", password_focus_out)








def Page(page):
    page()
    root.mainloop()


Page(Application)
