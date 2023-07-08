# Inputs de valores do úsuario

import sqlite3

nome_banco = 'Teste' # Valor de teste

########## Cria conecção com o banco de dados, caso não hajá banco de dados, cria o banco de dados. ##########

def conexao_banco():
    conect = sqlite3.connect(f'./data/{nome_banco}.db')
    
    return conect

con = conexao_banco() # Pelo que eu entendo mantem a conexão. Pelomenos é o proposito... 



# Cria a tabela, ao receber a conexão; A principio eu pensei em dar mais variação de tabelas "tb_standart" seria o tipo padrão.

########## Cria a tabela, ao receber a conexão. Nome da tabela a receber um for, ou então receber um nome personalizado pelo usuario. ##########

def criar_tabela(conexao): # Te falar que penei um pouco para entender esse valor, mas agora eu entendi parcialmente e já consigo aplicar. Só vou praticar mais.
    c = conexao.cursor()
    c.execute("CREATE TABLE tb_standart (ID INTEGER PRIMARY KEY AUTOINCREMENT, USERNAME VARCHAR(50), PASSWORD INTEGER, EMAIL VARCHAR(500), RECOVERY_MAILL VARCHAR(500))")
    

criar_tabela(con)

con.close()
