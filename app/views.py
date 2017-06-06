from flask import render_template 
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
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM Orcamento''')
	rv = cur.fetchall()
	print(str(rv))
	return render_template('index.html',title='home')

@app.route('/orcamento')
def orcamento():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM Tarefa''')
	rv = cur.fetchall();
	return render_template('orcamento.html',result=rv)
