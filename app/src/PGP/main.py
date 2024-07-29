import sqlite3 as lite
import pytz
from datetime import datetime
from constants import QUERY_INSERT_CATEGORIA, QUERY_INSERT_RECEITA, QUERY_DELETE_RECEITA

con= lite.connect('PGP.db')

def inserir_categoria(categoria: str):
    with con:
        cur = con.cursor()
        cur.execute(QUERY_INSERT_CATEGORIA, [categoria])

def inserir_receitas(categoria: str, valor:float, tipo_operacao: int):
    brasil_timezone = pytz.timezone("America/Sao_Paulo")
    datetime_now = datetime.now(pytz.utc).astimezone(brasil_timezone).strftime("%d-%m-%Y %H:%M:%S")
    print(datetime_now)
    with con:
        cur = con.cursor()
        cur.execute(QUERY_INSERT_RECEITA, [categoria, datetime_now, valor, tipo_operacao])

def deletar_receitas(id: int):
    with con:
        cur = con.cursor()
        cur.execute(QUERY_DELETE_RECEITA, [id])

def ver_categorias():
    with con:
        cur = con.cursor()
        cur.execute(QUERY_DELETE_RECEITA, [id])