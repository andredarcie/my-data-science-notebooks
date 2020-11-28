# Atividade em Cassandra

1. Construir um diagrama de Chebotko para as seguintes consultas:
C1: Quais usuários desembarcaram em uma viagem em uma determinada parada?


Usuarios_desembarcaram_em_uma_determinada_parada
id_Usuario   K
id_parada    C
id_embarque  C
id_viagem
hora_desembarque
nome_Usuario
~~~

C2: Para cada usuário em uma determinada viagem, determinar a parada de
embarque e a parada de desembarque

Usuario_parada_de_embarque_e_desembarque
id_usuario  K
id_viagem   C
id_parada
id_embarque

2. Crie as tabelas para as consultas C1 e C2 em CQL

Tabela C1:
CREATE TABLE Usuarios_desembarcaram_parada
(id_usuario int, id_parada int, id_embarque int, id_vaigem int, hora_embarque
timestamp, nome varchar(255)
PRIMARY KEY ((id_ usuario), id_parada, id_embarque))

Tabela C2:
CREATE TABLE Usuario_parada_embarcaram_desembarque
(id_usuario int, id_viagem int, id_parada int, id_embarque int, nome varchar(255)
PRIMARY KEY ((id_ usuario), id_viagem)) 

3. Defina as consultas C1 e C2 em CQL

Consulta c1:
SELECT u.id_usuario, u.nome, d.id_embarque, v.id_viagem, p.id_parada
FROM Usuarios as u
NATURAL JOIN Desembarque d
NATURAL JOIN Viagem as v
NATURAL JOIN Tem_horario_em_parada as h
NATURAL JOIN Parada p
WHERE p.id_parada IN (x) //onde x é a parada desejada

Consulta c2:
SELECT u.id_usuario, u.nome, d.id_embarque, p.id_parada
FROM Usuarios as u
NATURAL JOIN Desembarque d
NATURAL JOIN Viagem as v
NATURAL JOIN Parada p
WHERE v.id_viagem IN (x) //onde x é a viagem desejada
