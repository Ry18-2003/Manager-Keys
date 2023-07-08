# Inputs de valores do úsuario

import sqlite3

nome_banco = 'Teste' # Valor de teste

########## Cria conecção com o banco de dados, caso não hajá banco de dados, cria o banco de dados. ##########

def conexao_banco():
    conect = sqlite3.connect(f'./data/{nome_banco}.db')
    
    return conect

con = conexao_banco()

def criar_tabela(conexao):
    c=conexao.cursor()
    c.execute("CREATE TABLE tb_standart (ID INTEGER PRIMARY KEY AUTOINCREMENT, USERNAME VARCHAR(50), PASSWORD INTEGER, EMAIL VARCHAR(500), RECOVERY_MAILL VARCHAR(500))")
    

criar_tabela(con)

con.close()

# conexaobanco()
