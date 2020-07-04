# HuJiang app word book export

Export the word lists in the 沪江开心词场 app.

## How to use

1. Copy database from `/data/data/com.hjwordgames`, root required.
2. Put the database in this folder, then run `dump.py`.
3. Get the words in the generated txt file.

## How the data are stored in the database
* _Plain text_
* _Bitnot_ then _base64_
