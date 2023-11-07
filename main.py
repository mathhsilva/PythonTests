import tkinter as tk
import customtkinter as customtkinter
import subprocess

class MenuRetratil:
    def __init__(self, janela):
        self.janela = janela
        self.menu_expandido = False

        # Botão do menu
        self.botao_menu = tk.Button(self.janela, text="Menu", command=self.toggle_menu, bg="darkgray", fg="white")
        self.botao_menu.pack()

        # Crie o menu retrátil como um frame com fundo escuro
        self.menu_frame = tk.Frame(self.janela, bg="darkgray")

        # Botões do menu com fundo escuro e texto branco
        self.botao_menu_nova_tarefa = tk.Button(self.menu_frame, text="Nova Tarefa", command=self.nova_tarefa, bg="darkgray", fg="white")
        self.botao_menu_add_usuario = tk.Button(self.menu_frame, text="Registrar usuário", command=self.novo_usuario, bg="darkgray", fg="white")
        self.botao_menu_tarefas_concluidas = tk.Button(self.menu_frame, text="Tarefas Concluídas", command=self.tarefas_concluidas, bg="darkgray", fg="white")

        # Empacote os botões do menu no frame
        self.botao_menu_nova_tarefa.pack()
        self.botao_menu_add_usuario.pack()
        self.botao_menu_tarefas_concluidas.pack()

        # Inicialmente, o menu está oculto
        self.menu_frame.pack_forget()

    def toggle_menu(self):
        if self.menu_expandido:
            self.menu_frame.pack_forget()  # Oculta o menu
            self.menu_expandido = False
        else:
            self.menu_frame.pack()  # Exibe o menu
            self.menu_expandido = True

    def nova_tarefa(self):
        # Lógica para a ação "Nova Tarefa"
        subprocess.Popen(["python", "novatarefa.py"])

    def tarefas_concluidas(self):
        # Lógica para a ação "Tarefas Concluídas"
        pass

    def novo_usuario(self):
        # Lógica para a ação "Registrar usuário"
        subprocess.Popen(["python", "adduser.py"])

class Application():
    def __init__(self):
        self.janela = tk.Tk()
        self.criar_tela()

    def criar_tela(self):
        # Criando janela
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.janela.configure(bg='black')
        self.janela.geometry("800x600")
        self.janela.resizable(False, False)
        self.janela.iconbitmap("icon.ico")  # Ícone da janela

        # Crie o menu retrátil
        menu_retratil = MenuRetratil(self.janela)

        # Botão "Sair" fora do menu e alinhado à esquerda na parte inferior
        botao_sair = tk.Button(self.janela, text="Sair", command=self.janela.quit, bg="darkgray", fg="white")
        botao_sair.pack(side="left", anchor="sw")

        self.janela.mainloop()

app = Application()