/* Crie uma função que some todos os clientes cadastrados em uma loja durante um dia.*/

--Tomando por base que temos uma tabela com a seguinte estrutura:

Clientes

ID           INTEGER NOT NULL PRIMARY KEY,

NOME         VARCHAR(50),

NASCIMENTO   DATE,

SEXO         CHAR(1),

 

--Vamos criar a nossa SP com o seguinte código:

 

CREATE PROCEDURE UPD_INS_CLIENTES (

  ID   INTEGER,

  NOME VARCHAR(50),

  NASCIMENTO DATE,

  SEXO CHAR(1))

AS

BEGIN

  IF (EXISTS(SELECT ID FROM CLIENTES WHERE (ID = :ID))) THEN

    UPDATE CLIENTES

    SET NOME = :NOME,

        NASCIMENTO = :NASCIMENTO,

        SEXO = :SEXO

    WHERE (ID = :ID);

  ELSE

    INSERT INTO CLIENTES (

        ID,

        NOME,

        NASCIMENTO,

        SEXO)

    VALUES (

        :ID,

        :NOME,

        :NASCIMENTO,

        :SEXO);

END