import sqlite3
import base64
import os
import re


def decode(s: str):
    bytes = bytearray(base64.b64decode(s))
    for i in range(len(bytes)):
        bytes[i] = 255 ^ bytes[i]
    return bytes.decode("utf8")


def dumpBook(dbfile: str, out: str):
    with open(out, "w", encoding="utf8") as file, sqlite3.connect(dbfile) as conn:
        result = conn.execute(
            "SELECT word, word_phonetic, word_def FROM book_word")
        for row in result:
            file.write("{}\t{}\t{}\n".format(row[0], row[1], decode(row[2])))
        result.close()


for item in os.listdir():
    result = re.match("(iWord_book_word.*?)\\.db", item)
    if result:
        dumpBook(item, result.group(1)+".txt")
        # print(result)
