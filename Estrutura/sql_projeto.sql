drop database if exists sys;
create database sys;
use sys;

create table Pessoa(
	cpf varchar (11),
    nome varchar (40),
    tel integer,
    senha varchar(20),
    primary key (cpf)
);

create table Endereco(
	rua varchar (50),
    nro integer,
    cep integer,
    cidade varchar (30),
    estado varchar (2),
	cpf_pessoa varchar (11),
    foreign key (cpf_pessoa)references Pessoa(cpf),
    primary key (rua,cpf_pessoa)
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

create table Servico(
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

create table Orcamento(
	id integer NOT NULL AUTO_INCREMENT,
    data_Orc date,
    cpf_cliente varchar (11),
    cpf_funcionario varchar(11),
    primary key (id),
    foreign key (cpf_cliente) references Cliente(cpf),
    foreign key (cpf_funcionario) references Funcionario(cpf)
);

create table Cliente_Veiculo(
	cpf_cliente varchar (11),
    placa_veiculo varchar (7),
    foreign key (cpf_cliente) references Cliente(cpf),
    foreign key (placa_veiculo) references Veiculo(placa)
);

create table Peca(
	id integer NOT NULL AUTO_INCREMENT,
    nome varchar (20),
    preco float,
    primary key (id)
);

create table Orcamento_Servico(
	id_orcamento integer,
    id_servico integer,
    foreign key (id_orcamento) references Orcamento(id),
    foreign key (id_servico) references Servico(id)
);

create table Orcamento_Peca(
	id_orcamento integer,
    id_peca integer,
	qtde integer,
    foreign key (id_orcamento) references Orcamento(id),
    foreign key (id_peca) references Peca(id)
);

insert into Pessoa
values ("22570989517","Ryan Paulo Vinicius Lima",38223790,"123456");
insert into Pessoa
values ("56027372192","Iago Renato Monteiro",36477694,"123456");
insert into Pessoa
values ("00415965870","Matheus Giovanni Nathan Carvalho",38791387,"123456");
insert into Pessoa
values ("87449101424","Débora Julia Bárbara da Silva",27196380,"123456");
insert into Pessoa
values ("18740148920","Elisa Nicole Nascimento",988018452,"123456");
insert into Pessoa
values ("86014403981","Isaac Elias Rodrigues",25284227,"123456");

insert into Endereco
values ("Rua A",581,87308074,"Campo Mourão","PR","22570989517");
insert into Endereco
values ("Rua Jango Menezes",137,87301276,"Campo Mourão","PR","56027372192");
insert into Endereco
values ("Avenida dos Andradas",234,87310680,"Campo Mourão","PR","00415965870");
insert into Endereco
values ("Conjunto Benevides",918,87308155,"Campo Mourão","PR","87449101424");
insert into Endereco
values ("Rua Avelina Sanson Cooper",115,82220144,"Curitiba","PR","18740148920");
insert into Endereco
values("Travessa Luiz Tomazi",733,85605351,"Campo Mourão","PR","86014403981");

insert into Cliente
values ("22570989517");
insert into Cliente
values ("56027372192");
insert into Cliente
values ("18740148920");

insert into Tipo
values (DEFAULT,"Carro","Gol");
insert into Tipo
values (DEFAULT,"Moto","Ybr");
insert into Tipo
values(DEFAULT,"Carro","Camaro");

insert into Funcao
values (DEFAULT,"Mecanico");
insert into Funcao
values (DEFAULT,"Atendente");

insert into Veiculo
values ("APY9974",DEFAULT);
insert into Veiculo
values ("KEO7537",DEFAULT);
insert into Veiculo
values ("ARP6834",DEFAULT);

insert into Servico
values (DEFAULT,"Trocar pneu",300);
insert into Servico
values (DEFAULT,"Trocar bateria",200);
insert into Servico
values (DEFAULT,"Trocar radiador",450);

insert into Funcionario
values ("00415965870",111111,2200,1);
insert into Funcionario
values ("87449101424",222222,1800,2);
insert into Funcionario
values ("86014403981",333333,2000,1);

insert into Orcamento
values (DEFAULT,STR_TO_DATE('01-01-2017', '%d-%m-%Y'),"22570989517","00415965870");
insert into Orcamento
values (DEFAULT,STR_TO_DATE('02-01-2017', '%d-%m-%Y'),"56027372192","00415965870");
insert into Orcamento
values (DEFAULT,STR_TO_DATE('02-01-2017', '%d-%m-%Y'),"18740148920","00415965870");

insert into Peca
values (DEFAULT,"Bateria 1",150);
insert into Peca
values (DEFAULT,"Pneu 1",200);
insert into Peca
values (DEFAULT,"Radiador 1",250);

insert into Orcamento_Peca
values (1,2,10);
insert into Orcamento_Peca
values (2,1,22);
insert into Orcamento_Peca
values (3,3,10);

insert into Orcamento_Servico
values (1,1);
insert into Orcamento_Servico
values (1,2);
insert into Orcamento_Servico
values (2,1);
insert into Orcamento_Servico
values (3,3);

insert into Cliente_Veiculo
values ("22570989517","APY9974");
insert into Cliente_Veiculo
values ("56027372192","KEO7537");
insert into Cliente_Veiculo
values ("18740148920","ARP6834");
