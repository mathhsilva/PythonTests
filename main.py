import psycopg2
import customtkinter
from tkinter import *
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import os

# Criando janela
self.janela = customtkinter.Ctk()

class Application():
    def __init__(self):
        #self.janela = customtkinter.CTk()
        self.criar_tela()

    def criar_tela(self):
        # Criando janela
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.janela.geometry("800x600")
        self.janela.resizable(False, False)
        self.janela.iconbitmap("icon.ico")       #Icone da janela

        # Frame
        # frame = customtkinter.CTkFrame(master=self.janela, width=360, height=496)
        # frame.pack(side=RIGHT)

        # Frame Widgets
        # label3 = customtkinter.CTkLabel(master=frame, text="Sistema de Controle de Estoque", font=("Roboto", 20))
        # label3.place(x=25, y=25)

        # Botão de sair
        botao_sair = customtkinter.CTkButton(master=janela, width=300, text="Sair", command=self.janela.quit).place(relx=0, rely=0.05, anchor="w")

        self.janela.mainloop()

app = Application()