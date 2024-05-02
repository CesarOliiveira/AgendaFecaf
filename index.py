from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes()
        root.mainloop()
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
        ## Label ID
        self.lb_id = Label(self.frame_1, text="ID:")
        self.lb_id.place(relx=0.00, rely=0.05, relwidth=0.25, relheight=0.15)

        ## Entrada do ID
        self.ent_id = Entry(self.frame_1)
        self.ent_id.place(relx=0.05, rely=0.15, relwidth=0.25, relheight=0.15)

        ## Label da Senha
        self.lb_senha = Label(self.frame_1, text="Senha:")
        self.lb_senha.place(relx=0.00, rely=0.4, relwidth=0.25, relheight=0.15)

        ##Entrada da senha;
        self.ent_senha = Entry(self.frame_1, show="*")
        self.ent_senha.place(relx=0.05, rely=0.55, relwidth=0.25, relheight=0.15)

        ##Botão de entrada
        self.bt_ok = Button(self.frame_1, text="Entrar")
        self.bt_ok.place(relx=0.3, rely=0.2, relwidth=0.1, relheight=0.15)

Application()