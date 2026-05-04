source = "van_ban"
name = "quy_che_vnu"
time = "2022-10-21"
metadata = {}


import json

with open("raw_data_mining\docs_data\chapters_quy_che.json", 'r', encoding='utf-8') as f:
    chapter = json.load(f)
   

chunks = []

for i in chapter:
    for j in i:
        chunks.append(j)

data = {
    "source": source,
    "name": name,
    "time": time,
    "metadata": metadata,
    "chunks": chunks
}
