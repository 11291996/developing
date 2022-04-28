/*connecting to a database*/ 
mysql -h 'host (ip)' -u 'user' -p 'password' 

/*sourcing sql script*/
/*after connecting*/ source ~/file.sql 

/*creating a database*/
CREATE DATABASE 'NAME' CHARACTER SET 'CHARACTER SET' COLLATE 'RULE FOR COLLATION';
/*deleting a database*/ 
DROP DATABASE 'NAME';
/*checking databases*/
SHOW DATABASES;
/*selecting a database*/
USE 'NAME';

/*creating a table*/ /*the structure of the table is called 'schema'*/
CREATE TABLE 'NAME' (
      'COL_1' DATATYPE NOT NULL, /*null cannot be stored in the column*/
      'COL_2' DATATYPE DEFAULT DATA, /*set the table default value as DATA*/
UNIQUE ('COL_2') /*null fine, no duplication constraint index*/ 
/*more than one constraint*/
CONSTRAINT 'NAME' UNIQUE ('COL_1', 'COL_2')
PRIMARY KEY ('COL_1') /*works as an index, more than one columns can be used*/ /*no duplication, no null value*/
FOREIGN KEY ('MY TABLE') /*use constraint method for multiple constraints*/ REFERENCES 'TABLE_NAME' ('COLUMN_NAME') /*
ON DELETE or ON UPDATE CASCADE /*follow the change*/ SET NULL /*set the change to null*/ NO ACTION /*no action*/ SET DEFAULT /*use default value*/ RESTRICT /*no change after all*/ 
);

/*data types
CHAR( )	0 to 255 고정문자 길이
VARCHAR( )	0~65535 가변 문자 길이
TINYTEXT	최대 255 문자길이
TEXT	최대 65535 문자길이
BLOB	최대 65535 문자길이
MEDIUMTEXT	최대 16777215 문자길이
MEDIUMBLOB	최대 16777215 문자길이
LONGTEXT	최대 4294967295 문자길이
LONGBLOB	최대 4294967295 문자길이
 

TINYINT( )	-128 ~ 127 정수형, 0 ~ 255 정수형, UNSIGNED
SMALLINT( )	-32768 ~ 32767 정수형, 0 ~ 65535 정수형, UNSIGNED
MEDIUMINT( ) -8388608 ~ 8388607, 정수형, 0 to 16777215 정수형, UNSIGNED
INT( ) -2147483648 ~ 2147483647 정수형, 0 ~ 4294967295 정수형, UNSIGNED
BIGINT( )	-9223372036854775808 ~ 9223372036854775807 정수형, 0 ~ 18446744073709551615 정수형, UNSIGNED.
FLOAT	작은 부동소수점
DOUBLE( , )	큰 부동소수점
DECIMAL( , )	 

DATE	YYYY-MM-DD.
DATETIME	YYYY-MM-DD HH:MM:SS.
TIMESTAMP	YYYYMMDDHHMMSS.
TIME	HH:MM:SS.
 
ENUM ( )	정해진 값을 강제
SET */

/*list of tables*/
SHOW tables; 
/*checking schema*/
DESC 'TABLE_NAME';
/*deleting a table*/
DROP TABLE 'TABLE_NAME';

/*inserting data*/
INSERT INTO 'TABLE_NAME' VALUES ('JACK', 18, 'MALE');
INSERT INTO 'TABLE_NAME' ('COL_1', 'COL_2') VALUES ('JACK', 'MALE'); /*certain values in certain coulmns*/
/*updating data*/ 
UPDATE 'TABLE_NAME' SET 'COL_2' = 'FEMALE' WHERE 'COL_1' = 'JANE'; /*more than one change is possible for SET*/ 
/*altering schema*/
ALTER TABLE 'TABLE_NAME' CHANGE 'COL_1' 'NEW_NAME' DATATYPE; /*column name change*/ 
ALTER TABLE 'TABLE_NAME' MODIFY 'NEW_NAME' AFTER 'COL_2'; /*table order change*/ 
ALTER TABLE 'TABLE_NAME' MODIFY COLUMN OR ALTER 'COL_2' SET DEFAULT DATA; /*default data change*/
ALTER TALBE 'TABLE_NAME' ALTER 'COL_2' DROP DEFAULT DATA/*drops default data*/
ALTER TABLE 'TABLE_NAME' MODIFY 'COL_2' DATATYPE; /*column datatype change*/ 
ALTER TABLE 'TABLE_NAME' ADD COLUMN 'NEW_COL' DATATYPE DEFAULT DATA AFTER 'COL_2'; /*inserting a new column*/ 
/*FIRST after DATA will get the column in the first line*/
ALTER TABLE 'TABLE_NAME' DROP COLUMN 'COL_2'; /*deleting column*/ 
ALTER TABLE 'TABLE_NAME' ADD 'COL_2' DATATYPE PRIMARY KEY; /*adding primary key*/
ALTER TABLE 'TABLE_NAME' ADD CONSTRAINT 'NAME' PRIMARY KEY ('COL_2','NEW_COL');
ALTER TABLE 'TABLE_NAME' MODIFY COLUMN 'COL_2' DATATYPE PRIMARY KEY;/*updating column status*/
ALTER TABLE 'TABLE_NAME' MODIFY COLUMN CONSTRAINT 'NAME' (DATATYPE,) PRIMARY KEY ('COL_2','NEW_COL'); /*updating columns' status*/
ALTER TABLE 'TABLE_NAME' DROP 'COL' PRIMARY KEY; /*constraint can be used*/
ALTER TABLE 'TABLE_NAME' DROP PRIMARY KEY; 
ALTER TABLE 'TABLE NAME' ADD 'COL_2' DATATYPE UNIQUE; /*adding primary key*/
ALTER TABLE 'TABLE NAME' ADD CONSTRAINT 'NAME' (DATATYPE,) UNIQUE ('COL_2','NEW_COL');
ALTER TABLE 'TABLE NAME' MODIFY COLUMN 'COL_2' DATATYPE UNIQUE; /*updating column status*/
ALTER TABLE 'TABLE NAME' MODIFY COLUMN CONSTRAINT 'NAME' UNIQUE ('COL_2','NEW_COL'); /*updating columns' status*/
ALTER TABLE 'TABLE_NAME' DROP 'COL' UNIQUE; /*constraint can be used*/ 
ALTER TABLE 'TABLE_NAME' DROP UNIQUE;
ALTER TABLE 'TABLE_NAME' ADD FOREIGN KEY ('MY_TABLE') REFERENCES 'TABLE_NAME' ('COL'); /*constraint can be used*/ 
ALTER TABLE 'TALBE_NAME' DROP FOREIGN KEY ('MY_TABLE'); /*constraint can be used*/