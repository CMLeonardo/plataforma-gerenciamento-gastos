QUERY_INSERT_CATEGORIA = "INSERT INTO cat_gst_psl (categoria) VALUES (?)"
QUERY_SELECT_CATEGORIA = "SELECT * FROM cat_gst_psl"
QUERY_INSERT_RECEITA = "INSERT INTO rct_gst_psl (categoria, data, valor, tipo_operacao) VALUES (?, ?, ?, ?)"
QUERY_DELETE_RECEITA = "DELETE FROM rct_gst_psl WHERE id=?"
QUERY_SELECT_RECEITA = "SELECT * FROM rct_gst_psl"