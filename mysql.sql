CREATE TABLE test_table(auto_inc_id int primary key NOT NULL AUTO_INCREMENT, id int   not null,name text not null);
INSERT INTO test_table VALUES(null,1,'xsz');
INSERT INTO test_table VALUES(null,2,'tsh');
INSERT INTO test_table VALUES(null,9,'fzd');
CREATE TABLE test_table2(auto_inc_id int primary key NOT NULL AUTO_INCREMENT, id int   not null,name text not null);
INSERT INTO test_table2 VALUES(null,111,'hrh');
CREATE INDEX index0 on test_table(id)
;
