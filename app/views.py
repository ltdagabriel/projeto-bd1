from flask import render_template, request, redirect, url_for 
from app import app 
import bd

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

#CLIENTE

@app.route('/cliente')
def cliente():
	return render_template('cliente.html')

@app.route('/buscarcliente')
def buscarcliente():
	return render_template('buscarcliente.html')

@app.route('/buscarcliente/bd', methods=['POST'])
def buscarclientebd():
	cpf = request.form['cpf_busca']
	rv = bd.buscarcliente(cpf)
	return render_template('resultbusca.html',results=rv,tipo="cliente")

@app.route('/cadastrarcliente')
def cadastrarcliente():
	return render_template('cadastrarcliente.html')

@app.route('/cadastrarcliente/bd' , methods=['POST'])
def cadastrarclientebd():
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
	bd.cadastrarcliente(name,cpf,tel,rua,num,cidade,cep,estado,senha)
	return render_template('index.html')

@app.route('/alterarcliente')
def alterarcliente():
	return render_template('alterarcliente.html')

@app.route('/alterarcliente/2', methods=['GET'])
def alterarcliente2():
	nomei = request.args.get('nomei')
	return render_template('alterarcliente2.html',nomei=nomei)

@app.route('/alterarcliente/bd', methods=['POST'])
def alterarclientebd():
	nomei = request.form['in_nome']
	nome = request.form['in_nome']	
	cpf = request.form['in_cpf']
	tel = request.form['in_tel']
	rua = request.form['in_rua']
	num = request.form['in_n']
	cidade = request.form['in_cidade']
	cep = request.form['in_cep']
	estado = request.form['in_estado']
	senha = request.form['in_senha']
	bd.alterarcliente(nomei,nome,cpf,tel,rua,num,cidade,cep,estado,senha)
	return render_template('index.html')

@app.route('/removercliente/')
def removercliente():
	return render_template('removercliente.html')

@app.route('/removercliente/db', methods=['POST'])
def removerclientebd():
	cpf = request.form['cpf_remove']
	bd.removercliente(cpf)
	return render_template('resultremover.html',nome=cpf)

#VEICULO

@app.route('/veiculo')
def veiculo():
	return render_template('veiculo.html')

@app.route('/funcionario')
def funcionario():
	return render_template('funcionario.html')

@app.route('/servicos')
def servicos():
	return render_template('servicos.html')

#PECAS

@app.route('/estoque')
def estoque():
	return render_template('estoque.html')

@app.route('/buscarpeca')
def buscarpeca():
	return render_template('buscarpeca.html')

@app.route('/buscarpeca/bd', methods=['POST'])
def buscarpecabd():
	nome = request.form['nome']
	rv = bd.buscarpeca(nome)
	return render_template('resultbusca.html',results=rv,tipo="peca")

@app.route('/cadastrarpeca')
def cadastrarpeca():
	return render_template('cadastrarpeca.html')

@app.route('/cadastrarpeca/bd', methods=['POST'])
def cadastrarpecabd():
	nome = request.form['nome']
	preco = request.form['preco']
	bd.cadastrarpeca(nome,preco)
	return render_template('index.html')

@app.route('/alterarpeca')
def alterarpeca():
	return render_template('alterarpeca1.html')

@app.route('/alterarpeca2', methods=['GET','POST'])
def alterarpeca2():
	n = request.args.get('nomei')
	return render_template('alterarpeca2.html',nomei=n)

@app.route('/alterarpeca/bd',methods=['POST'])
def alterarpecabd():
	nomei = request.form['nomei']	
	nome = request.form['nome']
	preco = request.form['preco']
	bd.alterarpeca(nomei,nome,preco)
	return render_template('index.html')

@app.route('/removerpeca')
def removerpeca():
	return render_template('removerpeca.html')

@app.route('/removerpeca/bd', methods =['POST'])
def removerpecabd():
	nome = request.form['nome']
	bd.removerpeca(nome)
	return render_template('resultremover.html',nome=nome)

#ORCAMENTO

@app.route('/orcamento')
def orcamento():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM Tarefa''')
	rv = cur.fetchall();
	return render_template('orcamento.html',result=rv)
