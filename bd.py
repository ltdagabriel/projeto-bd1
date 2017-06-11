from flask_mysqldb import MySQL
from app import app
import bdconfig

mysql = MySQL(app)

def connect():
	conn = mysql.connection
	return conn

def insereCliente(name,cpf,tel,rua,num,cidade,cep,estado,senha):
	conn = mysql.connection
	cur = conn.cursor()
	cur.execute('''INSERT INTO Endereco VALUES (%s,%s,%s,%s,%s)''',(rua,num,cep,cidade,estado))
	cur.execute('''INSERT INTO Cliente VALUES (%s)''',(cpf))
	conn.commit()
	conn.close()
	return

def retornaCliente(cpf):
	conn = mysql.connection
	cur = conn.cursor()
	query = """SELECT * FROM Cliente c WHERE c.cpf = %s"""
	cur.execute(query, [cpf])
	rv = cur.fetchall()
	return rv