PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE test_table(id int primary key not null,name text not null);
INSERT INTO test_table VALUES(1,'xsz');
INSERT INTO test_table VALUES(2,'tsh');
INSERT INTO test_table VALUES(9,'fzd');
CREATE TABLE test_table2(id int primary key not null,name text not null);
INSERT INTO test_table2 VALUES(111,'hrh');
CREATE INDEX index0 on test_table(id)
;
COMMIT;
