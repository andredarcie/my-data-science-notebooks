# Atividade em SQL

Implementar os comandos e  consultas abaixo em SQL .

Os comandos e consultas devem ser previamente testados em MariaDb/MySQL

Esquema das  tabelas:

Cliente(cod_cliente, nom_cliente, dsc_profissao, nom_cidade)

Agencia(cod_agencia, nom_agencia, nom_cidade)

Conta(num_conta, tipo_conta, cod_cliente, cod_agencia, vlr_saldo)

Emprestimo( num_emprestimo, cod_cliente, cod_agencia, vlr_emprestimo)

Criação das tabelas: implementar um script SQL para a criação das tabelas acima. 

Inserções: criar pelo menos 3 inserções em cada uma das tabelas

Consultas:

1) Quais os clientes (cod_cliente e nom_cliente) do Banco?

2) Quais os clientes que residem em Poços de Caldas?

3) Quais os clientes (cod_cliente) com contas na agência cod_agencia = 123?

4) Quais os clientes com empréstimos de valor superior a R$ 2.000,00?

5) Quantas contas existem em todas as agências do Banco?

6) Quantos clientes possuem contas na agência cujo cod_agencia = 6?

# Respostas

## Criação das tabelas
```sql
CREATE TABLE Cliente (
    cod_cliente int NOT NULL AUTO_INCREMENT,
    nom_cliente varchar(255) NOT NULL,
    dsc_profissao varchar(255),
    nom_cidade varchar(255),
    PRIMARY KEY (cod_cliente)
);

CREATE TABLE Agencia (
    cod_agencia int NOT NULL AUTO_INCREMENT,
    nom_agencia varchar(255) NOT NULL,
    nom_cidade varchar(255),
    PRIMARY KEY (cod_agencia)
);

CREATE TABLE Conta (
    num_conta int NOT NULL AUTO_INCREMENT,
    tipo_conta varchar(255),
    cod_cliente int,
    cod_agencia int,
    vlr_saldo decimal,
    PRIMARY KEY (num_conta),
    FOREIGN KEY (cod_cliente) REFERENCES Cliente(cod_cliente),
    FOREIGN KEY (cod_agencia) REFERENCES Agencia(cod_agencia)
);

CREATE TABLE Emprestimo (
    num_emprestimo int NOT NULL AUTO_INCREMENT,
    cod_cliente int,
    cod_agencia int,
    vlr_emprestimo decimal,
    PRIMARY KEY (num_emprestimo),
    FOREIGN KEY (cod_cliente) REFERENCES Cliente(cod_cliente),
    FOREIGN KEY (cod_agencia) REFERENCES Agencia(cod_agencia)
);
```

## Inserções de dados nas tabelas
```sql
INSERT INTO Cliente (`nom_cliente`, `dsc_profissao`, `nom_cidade`) VALUES 
('Isaac Newton', 'Matematico', 'Poços de Caldas'),
('Siddartha Gautama', 'Filosofo', 'Poços de Caldas'),
('Albert Einstein', 'Fisico teorico', 'Ulm'),
('Ludwig van Beethoven', 'Compositor', 'Bonn')

INSERT INTO Agencia (`nom_agencia`, `nom_cidade`) VALUES 
('Agencia A', 'São Paulo'),
('Agencia B', 'Rio de Janeiro'),
('Agencia C', 'Brasília'),
('Agencia D', 'Salvador')

INSERT INTO Conta (`tipo_conta`, `cod_cliente`, `cod_agencia`, `vlr_saldo`) VALUES 
('Corrente', 1, 1, 10000),
('Poupança', 2, 2, 20000),
('Salário', 3, 3, 30000),
('Corrente', 4, 4, 40000)

INSERT INTO Emprestimo (`cod_cliente`, `cod_agencia`, `vlr_emprestimo`) VALUES 
(1, 1, 10000),
(2, 2, 20000),
(3, 3, 30000),
(4, 4, 40000)
```

## Consultas
1) Quais os clientes (cod_cliente e nom_cliente) do Banco?
```sql
SELECT cod_cliente, nom_cliente FROM cliente
```

2) Quais os clientes que residem em Poços de Caldas?
```sql
SELECT * FROM `cliente` WHERE nom_cidade = 'Poços de Caldas'
```

3) Quais os clientes (cod_cliente) com contas na agência cod_agencia = 123?
```sql
SELECT cliente.cod_cliente 
FROM cliente 
INNER JOIN conta ON cliente.cod_cliente = conta.cod_cliente
INNER JOIN agencia ON conta.cod_agencia = agencia.cod_agencia AND agencia.cod_agencia = 123
```

4) Quais os clientes com empréstimos de valor superior a R$ 2.000,00?
```sql
SELECT cliente.cod_cliente 
FROM cliente 
INNER JOIN emprestimo ON cliente.cod_cliente = emprestimo.cod_cliente 
WHERE emprestimo.vlr_emprestimo > 2000
```

5) Quantas contas existem em todas as agências do Banco?
```sql
SELECT COUNT(*) FROM agencia, conta WHERE conta.cod_agencia = agencia.cod_agencia
```

6) Quantos clientes possuem contas na agência cujo cod_agencia = 6?
```sql
SELECT COUNT(*) 
FROM cliente 
INNER JOIN conta ON cliente.cod_cliente = conta.cod_cliente 
INNER JOIN agencia ON conta.cod_agencia = agencia.cod_agencia AND agencia.cod_agencia = 6
```