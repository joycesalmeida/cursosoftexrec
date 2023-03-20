/*Uma empresa precisa criar um relatório que faça um levantamento diário da quantidade de produtos comprados no dia.
Para isso, crie um procedure que será usado para agilizar todos os processos.*/

-- Criando a tabela de produtos
PRODUTOS

ID           INTEGER NOT NULL PRIMARY KEY,

NOME         VARCHAR(50),

QUANTIDADE   INT(4),


-- Criando o Procedure

CREATE PROCEDURE UPD_INS_PRODUTOS (

  ID   INTEGER,

  NOME VARCHAR(50),

  QUANTIDADE INT(4))

AS

BEGIN

  IF (EXISTS(SELECT ID FROM PRODUTOS WHERE (ID = :ID))) THEN

    UPDATE PRODUTOS

    SET NOME = :NOME,

        QUANTIDADE = :QUANTIDADE

    WHERE (ID = :ID);

  ELSE

    INSERT INTO PRODUTOS (

        ID,

        NOME,

        QUANTIDADE)

    VALUES (

        :ID,

        :NOME,
		
		:QUANTIDADE);

END
