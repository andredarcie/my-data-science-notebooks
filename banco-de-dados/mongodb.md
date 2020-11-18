# Atividade em Mongo DB

Criar no MongoDB a coleção disponível no link:
https://docs.mongodb.com/manual/reference/bios-example-collection/

## Pergunta 1 - Programar uma consulta que retorne apenas os documentos com os nomes (name) (sem o campo '_id')

## Pergunta 2 - Programar uma consulta que retorne apenas os documentos com os sobrenomes (last) (sem o campo '_id')

## Pergunta 3 - Qual o retorno da consulta abaixo:
```js
db.bios.find({contribs: {$in: ["Python"]}}, {name:1, _id:0}).count()
```

## Pergunta 4 - Complete a consulta abaixo para que retorne o documento com o nome dos que tenham um prêmio {award: "Turing Award", "year" : 1983, "by" : "ACM"}
```js
db.bios.find({awards: { espaço-em-branco: [{award: "Turing Award", "year" : 1983, "by" : "ACM"}]}}, {name:1, _id:0}
```

## Pergunta 5 - Execute os comandos abaixo que definem um índice para o campo "awards.year" e para o campo "awards.award", este último do tipo "text". 
```js
db.bios.createIndex( {"awards.year": 1})
db.bios.createIndex( {"awards.award": "text"})
```

Programe agora uma consulta que retorna os documentos com biografias que tenham um prêmio no ano de 1999 ("awards.year") e complete o código abaixo

```js
db.bios.find( espaço-em-branco )
```

## Pergunta 6 - A partir dos índices criados na consulta anterior, complete a consulta abaixo de forma que 
esta retorne os documentos com os nomes dos que tenham um prêmio "Turing Award"

```js
db.bios.find({$text: { espaço-em-branco }, {name:1, _id:0 })
```

## Pergunta 7 - Quantos documentos são de biografias que receberam um prêmio "Turing Award"?