import re
import fileinput
import sys


def replacer(str0):
    str1 = 'replace('
    str2 = ",\'\\n\',char(10))"
    str3 = ",\'\\r\',char(13))"
    begin_idx = str0.find(str1)
    end_idx = str0.find(str2)
    if end_idx == -1:
        end_idx = str0.find(str3)
    if begin_idx == -1 or end_idx == -1:
        return str0
    return str0[:begin_idx] + str0[begin_idx + 8:end_idx] + str0[end_idx + 15:]


def main(sql_address: str):
    fo = open("./mysql.sql", "w+")
    for line in fileinput.input(sql_address):
        process = False
        for nope in ('BEGIN TRANSACTION', 'COMMIT',
                     'sqlite_sequence', 'CREATE UNIQUE INDEX', 'PRAGMA'):
            if nope in line:
                break
        else:
            process = True
        if not process:
            continue
        if line.find("CREATE TABLE") >= 0:
            # name, sub = m.groups()
            # line = '''DROP TABLE IF EXISTS %(name)s;
            #         CREATE TABLE IF NOT EXISTS %(name)s%(sub)s
            #         '''
            # line = line % dict(name=name, sub=sub)
            line = line.replace("primary key", ' ')
            line = line.replace('(', "(auto_inc_id int primary key NOT NULL AUTO_INCREMENT, ")
        else:
            m = re.search('INSERT INTO "([a-z_]*)"(.*)', line)
            if m:
                line = 'INSERT INTO %s%s\n' % m.groups()
                line = line.replace('"', r'\"')
                line = line.replace('"', "'")
            else:
                m = re.search('CREATE INDEX "([a-z_]*)"(.*)', line)
                if m:
                    line = line.replace('"', ' ')
                    line = line.replace('\'', ' ')
        line = re.sub(r"([^'])'t'(.)", r"\1THIS_IS_TRUE\2", line)
        line = line.replace('THIS_IS_TRUE', '1')
        line = re.sub(r"([^'])'f'(.)", r"\1THIS_IS_FALSE\2", line)
        line = replacer(line)
        line = line.replace('THIS_IS_FALSE', '0')
        line = line.replace('AUTOINCREMENT', 'AUTO_INCREMENT')
        line = line.replace('TEXT', 'VARCHAR(45)')
        line = line.replace('VALUES(', 'VALUES(null,')
        line = line.replace('\\r', '\\n')
        # line = line.replace('user_note', 'kol_note')

        # print(line)
        fo.write(line)


main(sys.argv[1])
