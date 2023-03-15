/* Para desenvolver um banco de dados com tabelas relacionadas, precisamos primeiro identificar as entidades 
que queremos armazenar e as relações entre elas. Para este exemplo, vamos supor que estamos construindo um
banco de dados para uma loja online que vende produtos e possui clientes. */

-- TABELA PRODUTOS*/

CREATE TABLE produtos (
  id_produto INT PRIMARY KEY,
  nome_produto VARCHAR(255),
  preco_produto FLOAT
);


-- TABELA CLIENTES

CREATE TABLE clientes (
  id_cliente INT PRIMARY KEY,
  nome_cliente VARCHAR(255),
  email_cliente VARCHAR(255)
);


-- RELACIONANDO AS TABELAS, CRIANDO PEDIDOS DOS CLIENTES

CREATE TABLE pedidos (
  id_pedido INT PRIMARY KEY,
  id_produto INT,
  id_cliente INT,
  quantidade INT,
  FOREIGN KEY (id_produto) REFERENCES produtos(id_produto),
  FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);


-- UTILIZANDO OS COMANDOS JOINS

-- INNER JOIN (INTERSEÇÃO)

SELECT clientes.nome_cliente, produtos.nome_produto, pedidos.quantidade
FROM clientes
INNER JOIN pedidos ON clientes.id_cliente = pedidos.id_cliente
INNER JOIN produtos ON pedidos.id_produto = produtos.id_produto;


-- LEFT JOIN (ESQUERDA) 

SELECT clientes.nome_cliente, produtos.nome_produto, pedidos.quantidade
FROM clientes
LEFT JOIN pedidos ON clientes.id_cliente = pedidos.id_cliente
LEFT JOIN produtos ON pedidos.id_produto = produtos.id_produto;


-- RIGHT JOIN (DIREITA)

SELECT clientes.nome_cliente, produtos.nome_produto, pedidos.quantidade
FROM clientes
RIGHT JOIN pedidos ON clientes.id_cliente = pedidos.id_cliente
RIGHT JOIN produtos ON pedidos.id_produto = produtos.id_produto;


-- FULL OUTER JOIN (TODOS)

SELECT clientes.nome_cliente, produtos.nome_produto, pedidos.quantidade
FROM clientes
FULL OUTER JOIN pedidos ON clientes.id_cliente = pedidos.id_cliente
FULL OUTER JOIN produtos ON pedidos.id_produto = produtos.id_produto;
