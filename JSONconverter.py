import json
with open("complete_seinfeld_scripts.txt", "rb") as fin:
    content = json.load(fin)
with open("complete_seinfeld_scriptsJson.txt", "wb") as fout:
    json.dump(content, fout, indent=1)