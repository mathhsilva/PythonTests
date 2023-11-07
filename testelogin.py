import psycopg2
import customtkinter
from tkinter import *
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import os

class Application:
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
            cursor.execute("SELECT * FROM usuario WHERE usu_login = %s AND usu_senha = %s", (login, senha))
            usuario = cursor.fetchone()
            conexao.close()

            if usuario is not None:
                return usuario
            else:
                return None
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def validar_senha(self):
        senha = self.edsenha.get()
        senha2 = self.edsenha2.get()

        if senha == senha2:
            return True
        else:
            CTkMessagebox(title="Erro", message="As senhas não conferem!")
            return False

    def usuario_existe(self, login):
        try:
            conexao = self.criar_conexao()
            cursor = conexao.cursor()
            cursor.execute("SELECT 1 FROM usuario WHERE usu_login = %s", (login,))
            existe = cursor.fetchone() is not None
            conexao.close()
            return existe
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False

    def onClick(self):
        login_digitado = self.edlogin.get()
        senha_digitada = self.edsenha.get()

        user_data = self.validar_login(login_digitado, senha_digitada)

        if user_data:
            CTkMessagebox(title="Sucesso!", message="Login efetuado com sucesso!")
            self.janela.destroy()  # Fecha a janela de login
            os.system('python main.py')
        else:
            CTkMessagebox(title="Erro", message="Credenciais Inválidas")

    def cadastrar_usuario(self):
        login_digitado = self.edlogin.get()
        senha_digitada = self.edsenha.get()
        senha2_digitada = self.edsenha2.get()

        if not self.usuario_existe(login_digitado):
            if self.validar_senha() and senha_digitada:
                try:
                    conexao = self.criar_conexao()
                    cursor = conexao.cursor()

                    # Utilize a sequência para gerar o valor de usu_id
                    cursor.execute("INSERT INTO usuario (usu_id, usu_login, usu_senha) VALUES (nextval('seq_usuario_id'), %s, %s)", (login_digitado, senha_digitada))
                    conexao.commit()
                    CTkMessagebox(title="Sucesso!", message="Usuário cadastrado com sucesso!")
                except (Exception, psycopg2.DatabaseError) as error:
                    print("Erro ao cadastrar usuário:", error)
                finally:
                    if conexao:
                        conexao.close()
            else:
                CTkMessagebox(title="Erro", message="As senhas não conferem!")
        else:
            CTkMessagebox(title="Erro", message="O nome de usuário já existe!")


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
        label3 = customtkinter.CTkLabel(master=self.janela, text="Cadastro de Usuários", font=("Roboto", 25, "bold"))
        label3.place(relx=0.5, rely=0.05, anchor="center")

        # Criando campo de entrada para o nome
        self.ednome = customtkinter.CTkEntry(master=frame, placeholder_text="Informe seu nome", width=300, font=("Robot o", 14))
        self.ednome.place(x=25, y=65)

        # Criando campo de entrada para o login
        self.edlogin = customtkinter.CTkEntry(master=frame, placeholder_text="Informe seu login", width=300, font=("Robot o", 14))
        self.edlogin.place(x=25, y=105)

        # Criando campo de entrada para a senha
        self.edsenha = customtkinter.CTkEntry(master=frame, show="*", placeholder_text="Informe sua senha", width=300, font=("Roboto", 14))
        self.edsenha.place(x=25, y=145)
        
        # Confirmando a senha
        self.edsenha2 = customtkinter.CTkEntry(master=frame, show="*", placeholder_text="Repita sua senha", width=300, font=("Roboto", 14))
        self.edsenha2.place(x=25, y=185)

        # Botão de login
        # botao_login = customtkinter.CTkButton(master=frame, width=300, text="Login", command=self.onClick).place(x=25, y=275)
        
        # Botão de cadastro
        botao_cadastro = customtkinter.CTkButton(master=frame, width=300, text="Cadastrar", command=self.cadastrar_usuario)
        botao_cadastro.place(x=25, y=345)  # Posicione o botão onde desejar
        
        # Botão de sair
        botao_sair = customtkinter.CTkButton(master=frame, width=300, text="Sair", command=self.janela.quit).place(x=25, y=310)

        self.janela.mainloop()

app = Application()
