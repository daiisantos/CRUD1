DROP DATABASE `biblioteca_pp2`;
CREATE SCHEMA `biblioteca_pp2` ;
USE `biblioteca_pp2` ;

CREATE TABLE `biblioteca_pp2`.`autor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `biblioteca_pp2`.`livro` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `autor_id` INT NULL,
  `titulo` VARCHAR(45) NOT NULL,
  `data_lancamento` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `autor_id_idx` (`autor_id` ASC) VISIBLE,
  CONSTRAINT `fk_autor_id`
    FOREIGN KEY (`autor_id`)
    REFERENCES `biblioteca_pp2`.`autor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

    CREATE TABLE `biblioteca_pp2`.`estoque` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `livro_id` INT NOT NULL,
  `quantidade` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_livro_id_idx` (`livro_id` ASC) VISIBLE,
  CONSTRAINT `fk_livro_id`
    FOREIGN KEY (`livro_id`)
    REFERENCES `biblioteca_pp2`.`livro` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

    CREATE TABLE `biblioteca_pp2`.`cliente` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC) VISIBLE);

CREATE TABLE `biblioteca_pp2`.`emprestimo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `livro_id` INT NULL,
  `cliente_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_livro_id_emprestimo_idx` (`livro_id` ASC) VISIBLE,
  INDEX `fk_cliente_id_idx` (`cliente_id` ASC) VISIBLE,
  UNIQUE INDEX `uk_livro_cliente` (`livro_id` ASC, `cliente_id` ASC) VISIBLE,
  CONSTRAINT `fk_livro_emprestimo_id`
    FOREIGN KEY (`livro_id`)
    REFERENCES `biblioteca_pp2`.`livro` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cliente_id`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `biblioteca_pp2`.`cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

INSERT INTO `biblioteca_pp2`.`autor` (`nome`) VALUES ('Rick Riordan');
INSERT INTO `biblioteca_pp2`.`autor` (`nome`) VALUES ('Suzanne Collins');

INSERT INTO `biblioteca_pp2`.`livro` (`autor_id`, `titulo`, `data_lancamento`) VALUES ('1', 'O Ladrão de Raios', '2005-06-28');
INSERT INTO `biblioteca_pp2`.`livro` (`autor_id`, `titulo`, `data_lancamento`) VALUES ('1', 'O Mar de Monstros', '2006-04-01');
INSERT INTO `biblioteca_pp2`.`livro` (`autor_id`, `titulo`, `data_lancamento`) VALUES ('2', 'Jogos Vorazes', '2008-09-14');
INSERT INTO `biblioteca_pp2`.`livro` (`autor_id`, `titulo`, `data_lancamento`) VALUES ('2', 'Em Chamas', '2009-09-01');

INSERT INTO `biblioteca_pp2`.`cliente` (`nome`, `cpf`) VALUES ('Maria Luiza', '12347897912');
INSERT INTO `biblioteca_pp2`.`cliente` (`nome`, `cpf`) VALUES ('Thiago luis', '56784907821');
INSERT INTO `biblioteca_pp2`.`cliente` (`nome`, `cpf`) VALUES ('Paula Silva', '18956790316');
INSERT INTO `biblioteca_pp2`.`cliente` (`nome`, `cpf`) VALUES ('Mariana Souza', '69087347667');


INSERT INTO `biblioteca_pp2`.`estoque` (`livro_id`, `quantidade`) VALUES ('1', '3');
INSERT INTO `biblioteca_pp2`.`estoque` (`livro_id`, `quantidade`) VALUES ('2', '2');
INSERT INTO `biblioteca_pp2`.`estoque` (`livro_id`, `quantidade`) VALUES ('3', '6');
INSERT INTO `biblioteca_pp2`.`estoque` (`livro_id`, `quantidade`) VALUES ('4', '5');

INSERT INTO `biblioteca_pp2`.`emprestimo` (`livro_id`, `cliente_id`) VALUES ('2', '1');
INSERT INTO `biblioteca_pp2`.`emprestimo` (`livro_id`, `cliente_id`) VALUES ('1', '2');
INSERT INTO `biblioteca_pp2`.`emprestimo` (`livro_id`, `cliente_id`) VALUES ('4', '4');
