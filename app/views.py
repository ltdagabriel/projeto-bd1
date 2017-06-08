from flask import render_template 
from app import app 
from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ra10fa20'
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
