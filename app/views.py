from flask import render_template, request, redirect, url_for 
from app import app 
from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'sys'

mysql = MySQL(app)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/cliente')
def cliente():
	return render_template('cliente.html')

@app.route('/buscarcliente')
def buscarcliente():
	return render_template('buscarcliente.html')

@app.route('/cadastrarcliente')
def cadastrarcliente():
	return render_template('cadastrarcliente.html')

@app.route('/buscarcliente/bd', methods=['POST'])
def retornarcliente():
	cpf = request.form['cpf_busca']
	conn = mysql.connection
	cur = conn.cursor()
	query = """SELECT * FROM Cliente c WHERE c.cpf = %s"""
	cur.execute(query, [cpf])
	rv = cur.fetchall();
	return redirect(url_for('index'))

@app.route('/cadastrarcliente/bd' , methods=['POST'])
def inserircliente():
	name = request.form['in_nome']	
	cpf = request.form['in_cpf']
	tel = request.form['in_tel']
	rua = request.form['in_rua']
	num = request.form['in_n']
	cidade = request.form['in_cidade']
	cep = request.form['in_cep']
	estado = request.form['in_estado']
	senha = request.form['in_senha']
	print(name,cpf)
	conn = mysql.connection
	cur = conn.cursor()
	cur.execute('''INSERT INTO Endereco VALUES (%s,%s,%s,%s,%s)''',(rua,num,cep,cidade,estado))
	cur.execute('''INSERT INTO Cliente VALUES (%s)''',(cpf))
	conn.commit()
	return render_template('index.html')


@app.route('/veiculo')
def veiculo():
	return render_template('veiculo.html')

@app.route('/funcionario')
def funcionario():
	return render_template('funcionario.html')

@app.route('/servicos')
def servicos():
	return render_template('servicos.html')

@app.route('/estoque')
def estoque():
	return render_template('estoque.html')

@app.route('/orcamento')
def orcamento():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM Tarefa''')
	rv = cur.fetchall();
	return render_template('orcamento.html',result=rv)
