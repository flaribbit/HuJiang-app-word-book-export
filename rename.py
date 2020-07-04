import os
for item in os.listdir():
    if item.find("word")>-1:
        os.rename(item,item+".db")
