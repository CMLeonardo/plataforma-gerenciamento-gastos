from tkinter import NSEW, Frame, Tk, ttk
from constants import cores

# Criando Janela
janela = Tk()
janela.title("PGP")
janela.geometry('900x650')
janela.configure(background=cores[1])
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use("clam")

# Header
header = Frame(janela, width=898, height=50, bg=cores[0], relief="flat")
header.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

body_graficos = Frame(janela, width=898, height=361, bg=cores[0], relief="raised")
body_graficos.grid(row=1, column=0, pady=0, padx=1, sticky=NSEW)

body_tabela = Frame(janela, width=898, height=235, bg=cores[0], relief="flat")
body_tabela.grid(row=2, column=0, pady=1, padx=1, sticky=NSEW)

janela.mainloop()