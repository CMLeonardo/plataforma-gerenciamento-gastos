import sqlite3 as lite

con= lite.connect('PGP.db')

with con:
    cur = con.cursor()
    #cat_gst_psl = Categoria dos Gastos Pessoais
    cur.execute("CREATE TABLE cat_gst_psl(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT)")

with con:
    cur = con.cursor()
    #rct_gst_psl = Receitas dos Gastos Pessoais
    cur.execute("CREATE TABLE rct_gst_psl(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, data DATE, valor DECIMAL, tipo_operacao INTEGER)")