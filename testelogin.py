import psycopg2
import customtkinter
from tkinter import *
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import os

class Application():
    def __init__(self):
        self.janela = customtkinter.CTk()
        self.criar_interface()
        
    def criar_conexao(self):
        try:
            conexao = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="12345",
                host="localhost",
                port="5433"
            )
            return conexao
        except psycopg2.Error as e:
            print("Não foi possível conectar ao banco de dados.")
            print(e)
            return None

    def validar_login(self, login, senha):
        try: 
            conexao = self.criar_conexao()
            cursor = conexao.cursor()
            cursor.execute("Select * from usuario where usu_login = %s and usu_senha = %s", (login,senha))
            usuario = cursor.fetchone()
            conexao.close()
            
            if usuario is not None:
                return True 
            else: 
                return False
        except (Exception, psycopg2.DatabaseError) as error: 
            print(error)
            return False      

    def onClick(self):
        login_digitado = self.edlogin.get()
        senha_digitada = self.edsenha.get()
        
        if self.validar_login(login_digitado, senha_digitada):
            CTkMessagebox(title="Sucesso!", message="Login efetuado com sucesso!")
            self.janela.destroy()  # Fecha a janela de login
            os.system('python main.py') 
        else:
            CTkMessagebox(title="Erro", message="Credenciais Inválidas")  

    def criar_interface(self):
        # Criando janela
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.janela.geometry("700x500")
        self.janela.resizable(False, False)
        self.janela.iconbitmap("icon.ico")       #Icone da janela

        # Imagem de fundo da janela 
        img = PhotoImage(file="log.png")
        label_img = customtkinter.CTkLabel(master=self.janela, image=img, text="")
        label_img.place(x=5, y=65)

        # Frame
        frame = customtkinter.CTkFrame(master=self.janela, width=360, height=496)
        frame.pack(side=RIGHT)

        # Frame Widgets
        label3 = customtkinter.CTkLabel(master=frame, text="Sistema de Login", font=("Roboto", 20))
        label3.place(x=25, y=25)

        # Criando campo de entrada para o login
        self.edlogin = customtkinter.CTkEntry(master=frame, placeholder_text="Informe seu login", width=300, font=("Robot o", 14))
        self.edlogin.place(x=25, y=105)

        # Criando campo de entrada para a senha
        self.edsenha = customtkinter.CTkEntry(master=frame, show="*", placeholder_text="Informe sua senha", width=300, font=("Robot o", 14))
        self.edsenha.place(x=25, y=175)

        # CheckBox
        checkbox = customtkinter.CTkCheckBox(master=frame, text="Lembrar-me").place(x=25, y=235)

        # Botão de login
        botao_login = customtkinter.CTkButton(master=frame, width=300, text="Login", command=self.onClick).place(x=25, y=275)

        # Botão de sair
        botao_sair = customtkinter.CTkButton(master=frame, width=300, text="Sair", command=self.janela.quit).place(x=25, y=310)

        self.janela.mainloop()

app = Application()
