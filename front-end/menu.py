from tkinter import *



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
