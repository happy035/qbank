CREATE TABLE `qbank`.`tbl_user` (
  `user_id` SMALLINT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NULL,
  `user_username` VARCHAR(45) NULL,
  `user_password` VARCHAR(150) NULL,
  PRIMARY KEY (`user_id`));

CREATE TABLE `qbank`.`tbl_question` (
  `q_id` smallint NOT NULL AUTO_INCREMENT,
  `q_severity` varchar(8) NULL,
  `q_catBig` varchar(20) NOT NULL,
  `q_catMid` varchar(20) NOT NULL,
  `q_sentence` text NOT NULL,
  `q_answer` text NOT NULL,
  `q_comment` text NOT NULL,
  `q_regdate` date NOT NULL,
  PRIMARY KEY (`q_id`));
  
  CREATE TABLE `qbank`.`tbl_answersheet` (
  `user_id` SMALLINT NOT NULL AUTO_INCREMENT,
  `user_tid` VARCHAR(45) NULL,
  `user_tscore` VARCHAR(45) NULL,
  `user_` VARCHAR(45) NULL,
  `user_` VARCHAR(150) NULL,
  PRIMARY KEY (`user_id`));

CREATE TABLE `qbank`.`tbl_catBig` (
  big_name varchar(20) default NULL
);

CREATE TABLE `qbank`.`tbl_catMid` (
  mid_name varchar(20) default NULL
);