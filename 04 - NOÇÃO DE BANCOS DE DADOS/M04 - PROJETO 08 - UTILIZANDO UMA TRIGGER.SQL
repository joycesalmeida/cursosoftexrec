-- M04 - PROJETO 08 - UTILIZANDO UMA TRIGGER

-- Você deve criar uma tabela para executar uma trigger que relacione algum comando, como: insert, select, delete ou update.

/* CRIEI UMA TABELA DE UM ALARME QUE AVISA AO USUÁRIO, OS HORÁRIOS DOS MÉDICAMENTOS QUE PRECISA TOMAR DURANTE O DIA
NESSE CÓDIGO, A TRIGGER PODE SER MODIFICADA PARA EXECUTAR OUTRAS AÇÕES, COMO ENVIAR E-MAIL OU UMA NOTIFICAÇÃO PARA O USUÁRIO*/

-- Cria a tabela 'alarme_medicamentos'

CREATE TABLE alarme_medicamentos (
  id SERIAL PRIMARY KEY,
  nome_medicamento VARCHAR(50) NOT NULL,
  horario_1 TIME NOT NULL,
  horario_2 TIME NOT NULL,
  horario_3 TIME NOT NULL
);

-- Cria a trigger que executa quando uma nova linha é inserida na tabela 'alarme_medicamentos'

CREATE TRIGGER lembrar_usuario AFTER INSERT ON alarme_medicamentos
FOR EACH ROW
BEGIN


  -- Atribui o valor da coluna 'nome_medicamento' à variável 'medicamento'
  SET @medicamento = NEW.nome_medicamento;
  

  -- Atribui o valor da coluna 'horario_1' à variável 'horario1'
  SET @horario1 = NEW.horario_1;
  

  -- Atribui o valor da coluna 'horario_2' à variável 'horario2'
  SET @horario2 = NEW.horario_2;
  

  -- Atribui o valor da coluna 'horario_3' à variável 'horario3'
  SET @horario3 = NEW.horario_3;
  
  -- Exibe uma mensagem informando ao usuário os horários de tomar o medicamento

  SELECT CONCAT('Não esqueça de tomar o medicamento "', @medicamento, '" nos horários ', @horario1, ', ', @horario2, ' e ', @horario3, '.') AS mensagem;

END;
