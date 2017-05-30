drop database if exists sys;
create database sys;
use sys;

create table Endereco(
	rua varchar (50),
    nro integer,
    cep integer,
    cidade varchar (30),
    estado varchar (2),
    primary key (rua)
);

create table Pessoa(
	cpf varchar (11),
    nome varchar (30),
    tel integer,
    rua varchar (50),
    primary key (cpf)
);

create table Cliente(
	cpf varchar (11),
    nome varchar (30),
    tel integer,
    primary key (cpf),
    foreign key (cpf) references Pessoa(cpf)
);

create table Veiculo(
	placa varchar (7),
    primary key (placa)
);

create table Tipo(
	id integer,
    nome varchar (20),
    modelo varchar (20),
    primary key (id)
);
	
create table Orcamento(
	id integer,
    val_total float,
    data_Orc date,
    cpf_cliente varchar (11),
    primary key (id),
    foreign key (cpf_cliente) references Cliente(cpf)
);

create table Tarefa(
	id integer,
    nome varchar (40),
    primary key (id)
);

create table Funcao(
	id integer,
    nome varchar (30),
    primary key (id)
);

create table Funcionario(
	cpf varchar (11),
    nome varchar (30),
    tel integer,
    nro_carteira integer,
    salario float,
    id_funcao integer,
    primary key (cpf),
    foreign key (cpf) references Pessoa(cpf),
    foreign key (id_funcao) references Funcao(id)
);

create table Cliente_Veiculo(
	cpf varchar (11),
    placa varchar (7),
    foreign key (cpf) references Cliente(cpf),
    foreign key (placa) references Veiculo(placa)
);

create table Estoque(
	id integer,
    nome varchar (20),
    qtde integer,
    preco float,
    primary key (id)
);

create table Orcamento_Funcionario(
	id_orcamento integer,
    cpf_funcionario varchar (11),
    foreign key (id_orcamento) references Orcamento(id),
    foreign key (cpf_funcionario) references Funcionario(cpf)
);

create table Orcamento_Tarefa(
	id_orcamento integer,
    id_tarefa integer,
    foreign key (id_orcamento) references Orcamento(id),
    foreign key (id_tarefa) references Tarefa(id)
);

create table Tarefa_Estoque(
	id_tarefa integer,
    id_estoque integer,
    foreign key (id_tarefa) references Tarefa(id),
    foreign key (id_estoque) references Estoque(id)
);
	
create table Veiculo_Tipo(
	placa_veiculo varchar(7),
    id_tipo integer,
    foreign key (placa_veiculo) references Veiculo(placa),
    foreign key (id_tipo) references Tipo(id)
);


    