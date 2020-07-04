import sqlite3
import base64
import os
import re

def decode(s):
    bytes=bytearray(base64.b64decode(s))
    for i in range(len(bytes)):
        bytes[i]=255^bytes[i]
    return bytes.decode("utf8")

def dumpBook(s,out):
    file=open(out,"w",encoding="utf8")
    conn=sqlite3.connect(s)
    result=conn.execute("SELECT word,word_phonetic,word_def FROM book_word")
    for row in result:
        # print(row[0],row[1],decode(row[2]),sep="\t")
        file.write("%s\t%s\t%s\n"%(row[0],row[1],decode(row[2])))
    file.close()
    result.close()
    conn.close()

for item in os.listdir():
    result=re.match("(iWord_book_word.*?)\\.db",item)
    if result:
        dumpBook(item,result.group(1)+".txt")
        # print(result)
