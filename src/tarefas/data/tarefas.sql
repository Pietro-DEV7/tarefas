DROP DATABASES IF EXISTS `tarefas`;

CREATE DATABASES IF NOT EXISTS `tarefas`;

USE `tarefas`;

DROP TABLE IF EXISTS `tarefas`;

CREATE TABLE IF NOT EXISTS `tarefa` (
  `id_tarefa` BIGINT NOT NULL PRIMARY KEY,
  `titulo_tarefa` VARCHAR(100) NOT NULL,
  `data_tarefa` DATETIME NULL
);

