import sqlite3
import base64
def decode(s):
    bytes=bytearray(base64.b64decode(s))
    for i in range(len(bytes)):
        bytes[i]=255^bytes[i]
    return bytes.decode("utf8")

conn=sqlite3.connect("iWord_book_word_12922.db")
result=conn.execute("SELECT word,word_phonetic,word_def FROM book_word")
for row in result:
    print(row[0],row[1],decode(row[2]),sep="\t")
conn.close()
