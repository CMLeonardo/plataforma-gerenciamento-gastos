import sqlite3 as lite
import pandas as pd
import pytz
from datetime import datetime
from constants import QUERY_INSERT_CATEGORIA, QUERY_INSERT_RECEITA, QUERY_DELETE_RECEITA, QUERY_SELECT_CATEGORIA, QUERY_SELECT_RECEITA

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

def listar_categorias() -> pd.DataFrame:
    with con:
        cur = con.cursor()
        cur.execute(QUERY_SELECT_CATEGORIA)
        linhas = cur.fetchall()
    return pd.DataFrame(linhas, columns=['categorias'])

def listar_receitas(tipo_operacao: int) -> pd.DataFrame:
    with con:
        cur = con.cursor()
        cur.execute(QUERY_SELECT_RECEITA)
        linhas = cur.fetchall()
        data_receitas = pd.DataFrame(linhas, columns=['categorias', 'data', 'valor', 'tipo_operacao'])
    try:
        filtro_receitas = data_receitas['tipo_operacao'] == tipo_operacao
        data_filtrada = data_receitas[filtro_receitas] if tipo_operacao != 1 and tipo_operacao != 2 else data_receitas
        return data_filtrada
    except Exception:
        print(Exception)
        return pd.DataFrame()