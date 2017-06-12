from flask_mysqldb import MySQL
from app import app
import bdconfig

mysql = MySQL(app)

def connect():
	conn = mysql.connection
	return conn

def cadastrarcliente(nome,cpf,tel,rua,num,cidade,cep,estado,senha):
	conn = connect()
	cur = conn.cursor()
	cur.execute('''INSERT INTO Endereco VALUES (%s,%s,%s,%s,%s)''',(rua,num,cep,cidade,estado))
	cur.execute('''INSERT INTO Cliente VALUES (%s)''',(cpf))
	cut.execute('''INSERT INTO Pessoa VALUES (%s,%s,%s,%s,%s)'''),(cpf,nome,tel,rua,senha)
	conn.commit()
	return

def buscarcliente(cpf):
	conn = connect()
	cur = conn.cursor()
	query = """SELECT p.nome,p.cpf,p.tel,p.rua_endereco FROM Cliente c,Pessoa p WHERE c.cpf = p.cpf AND c.cpf = %s"""
	cur.execute(query, [cpf])
	rv = cur.fetchall()

	return rv

def removercliente(cpf):
	conn = connect()
	cur = conn.cursor()
	query = """SELECT p.cpf FROM Cliente c,Pessoa p WHERE c.cpf = p.cpf AND c.cpf = %s"""
	cur.execute(query,[cpf])
	rv = cur.fetchall()
	if not rv:
		return 1
	query = """DELETE FROM Cliente_Veiculo WHERE cpf_cliente = %s"""
	cur.execute(query,[cpf])
	query = """SELECT id FROM Orcamento WHERE cpf_cliente = %s"""
	cur.execute(query,[cpf])
	orcamento = cur.fetchall()
	query = """DELETE FROM Orcamento_Servico WHERE id_orcamento = %s"""
	for x in range(len(orcamento)):
		orcamentoid = orcamento[x]
		cur.execute(query,[orcamentoid])
		query = """DELETE FROM Orcamento_Peca WHERE id_orcamento = %s"""
	for y in range(len(orcamento)):
		orcamentoid = orcamento[y]
		cur.execute(query,[orcamentoid])
		query = """DELETE FROM Orcamento WHERE id = %s"""
	for z in range(len(orcamento)):
		orcamentoid = orcamento[x]
		cur.execute(query,[orcamentoid])
	query = """DELETE FROM Cliente WHERE cpf = %s"""
	cur.execute(query,[cpf])
	query = """DELETE FROM Endereco WHERE cpf_pessoa = %s"""
	cur.execute(query,[cpf])
	query = """DELETE FROM Pessoa where cpf = %s"""
	cur.execute(query,[cpf])
	conn.commit()
	return 0

#PEÇA

def buscarpeca(nome):
	conn = connect()
	cur = conn.cursor()
	query = """SELECT * FROM Peca WHERE nome RLIKE %s"""
	cur.execute(query,[nome])
	rv = cur.fetchall()
	return rv

def cadastrarpeca(nome,preco):
	conn = connect()
	cur = conn.cursor()
	query = """INSERT INTO Peca VALUES (DEFAULT,%s,%s)"""
	cur.execute(query,[nome,preco])
	conn.commit()
	return

def alterarpeca(nomei,nome,preco):
	conn = connect()
	cur = conn.cursor()
	query = """UPDATE Peca SET nome = %s,preco = %s WHERE nome = %s"""
	cur.execute(query,[nome,preco,nomei])
	conn.commit()
	return

def removerpeca(nome):
	conn = connect()
	cur = conn.cursor()
	query = """SELECT id FROM Peca WHERE nome = %s"""
	cur.execute(query,[nome])
	rv = cur.fetchall()
	query = """DELETE FROM Orcamento_Peca WHERE id_peca = %s"""
	cur.execute(query,[rv[0][0]])
	query = """DELETE FROM Peca WHERE id = %s"""
	cur.execute(query,[rv[0][0]])
	conn.commit()
	return rv