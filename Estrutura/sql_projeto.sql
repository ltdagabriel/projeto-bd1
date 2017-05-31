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
    nome varchar (40),
    tel integer,
    rua_endereco varchar (50),
    primary key (cpf),
    foreign key (rua_endereco) references Endereco(rua)
);

create table Cliente(
	cpf varchar (11),
    primary key (cpf),
    foreign key (cpf) references Pessoa(cpf)
);

create table Tipo(
	id integer NOT NULL AUTO_INCREMENT,
    nome varchar (20),
    modelo varchar (20),
    primary key (id)
);

create table Veiculo(
	placa varchar (7),
    veiculo_tipo integer NOT NULL AUTO_INCREMENT,
    primary key (placa),
    foreign key (veiculo_tipo) references Tipo(id)
);
	
create table Orcamento(
	id integer NOT NULL AUTO_INCREMENT,
    data_Orc date,
    cpf_cliente varchar (11),
    primary key (id),
    foreign key (cpf_cliente) references Cliente(cpf)
);

create table Tarefa(
	id integer NOT NULL AUTO_INCREMENT,
    nome varchar (40),
    preco float,
    primary key (id)
);

create table Funcao(
	id integer NOT NULL AUTO_INCREMENT,
    nome varchar (30),
    primary key (id)
);

create table Funcionario(
	cpf varchar (11),
    nro_carteira integer,
    salario float,
    id_funcao integer,
    primary key (cpf),
    foreign key (cpf) references Pessoa(cpf),
    foreign key (id_funcao) references Funcao(id)
);

create table Cliente_Veiculo(
	cpf_cliente varchar (11),
    placa_veiculo varchar (7),
    foreign key (cpf_cliente) references Cliente(cpf),
    foreign key (placa_veiculo) references Veiculo(placa)
);

create table Estoque(
	id integer NOT NULL AUTO_INCREMENT,
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

insert into Endereco
values ("Rua A",581,87308074,"Campo Mourão","PR");
insert into Endereco
values ("Rua Jango Menezes",137,87301276,"Campo Mourão","PR");
insert into Endereco
values ("Avenida dos Andradas",234,87310680,"Campo Mourão","PR");
insert into Endereco
values ("Conjunto Benevides",918,87308155,"Campo Mourão","PR");

insert into Pessoa
values ("22570989517","Ryan Paulo Vinicius Lima",38223790,"Rua A");
insert into Pessoa
values ("56027372192","Iago Renato Monteiro",36477694,"Rua Jango Menezes");
insert into Pessoa
values ("00415965870","Matheus Giovanni Nathan Carvalho",38791387,"Avenida dos Andradas");
insert into Pessoa
values ("87449101424","Débora Julia Bárbara da Silva",27196380,"Conjunto Benevides");

insert into Cliente
values ("22570989517");
insert into Cliente
values ("56027372192");

insert into Tipo
values (DEFAULT,"Carro","Gol");
insert into Tipo
values (DEFAULT,"Moto","Ybr");

insert into Funcao
values (DEFAULT,"Mecanico");
insert into Funcao
values (DEFAULT,"Atendente");

insert into Veiculo
values ("APY9974",DEFAULT);
insert into Veiculo
values ("KEO7537",DEFAULT);

insert into Orcamento
values (DEFAULT,STR_TO_DATE('01-01-2017', '%d-%m-%Y'),22570989517);
insert into Orcamento
values (DEFAULT,STR_TO_DATE('02-01-2017', '%d-%m-%Y'),56027372192);

insert into Tarefa
values (DEFAULT,"Trocar pneu",300);
insert into Tarefa
values (DEFAULT,"Trocar bateria",200);

insert into Estoque
values (DEFAULT,"Bateria 1",20,150);
insert into Estoque
values (DEFAULT,"Pneu 1",16,200);

insert into Tarefa_Estoque
values (1,2);
insert into Tarefa_Estoque
values (2,1);

insert into Orcamento_Tarefa
values (1,1);
insert into Orcamento_Tarefa
values (1,2);
insert into Orcamento_Tarefa
values (2,1);


insert into Funcionario
values ("00415965870",111111,2200,1);
insert into Funcionario
values ("87449101424",222222,1800,2);

insert into Cliente_Veiculo
values ("22570989517","APY9974");
insert into Cliente_Veiculo
values ("56027372192","KEO7537");
