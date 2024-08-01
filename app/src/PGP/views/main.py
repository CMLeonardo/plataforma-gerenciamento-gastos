from tkinter import LEFT, NSEW, NW, RAISED, Frame, Label, Tk, ttk
from constants import cores_fundo, cores_txt, cores_destaque
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import os

# Construir o caminho completo para a imagem
image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'util', 'logo_PGP.png'))

# Criando Janela
janela = Tk()
janela.title("PGP")
janela.geometry('900x650')
janela.configure(background=cores_fundo[0])
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use("clam")

header = Frame(janela, width=898, height=50, bg=cores_fundo[0], relief="flat")
header.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

body_graficos = Frame(janela, width=898, height=361, bg=cores_fundo[0], relief="raised")
body_graficos.grid(row=1, column=0, pady=0, padx=1, sticky=NSEW)

body_tabela = Frame(janela, width=898, height=235, bg=cores_fundo[0], relief="flat")
body_tabela.grid(row=2, column=0, pady=1, padx=1, sticky=NSEW)

# Header
logo_pgp = Image.open(image_path)
logo_pgp = logo_pgp.resize((45, 45))
logo_pgp = ImageTk.PhotoImage(logo_pgp)

logo_app = Label(header, image=logo_pgp, text="                    Gerenciamento de Gastos Pessoais", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Arial 20 bold'), bg=cores_txt[0])
logo_app.place(x=0, y=0)

def porcentagem():
    titulo_barra_progresso = Label(body_graficos, text="Porcentagem da Receita Gasta", height=1, anchor=NW, font=('Arial 12 bold'), bg=cores_fundo[0], fg=cores_txt[0])
    titulo_barra_progresso.place(x=330, y=5)

    style_barra_progresso = ttk.Style()
    style_barra_progresso.theme_use('default')
    style_barra_progresso.configure("black.Horizontal.TProgressbar",troughcolor= cores_fundo[2], background=cores_destaque[3])
    barra_progresso = Progressbar(body_graficos, length=180, style='black.Horizontal.TProgressbar')
    barra_progresso.place(x=333, y=35)
    barra_progresso['value'] = 50

    porcentagem_barra_progresso = Label(body_graficos, text="{:,.2f}%".format(barra_progresso['value']), anchor=NW, font=('Arial 11 bold'), bg=cores_fundo[0], fg=cores_txt[0])
    porcentagem_barra_progresso.place(x=518, y=32)
porcentagem()
janela.mainloop()