from flask import render_template, request, redirect, url_for 
from app import app 
import bd

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
	rv = bd.retornaCliente(cpf)
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
	bd.insereCliente(name,cpf,tel,rua,num,cidade,cep,estado,senha)
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
