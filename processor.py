import json
import math

data = open("all.json", "r", encoding="utf-8").read()
data = json.loads(data)



rank = {}
# loop through words in curr 
for i in data:
  if i["word"] not in rank.keys():
    if int(i["written_on"][0:4]) > 2022:
      rank[i["word"]] = 1
    else:
      rank[i["word"]] = 0
  else:
    if int(i["written_on"][0:4]) > 2022:
      rank[i["word"]] += 1
    else:
      rank[i["word"]] -= 0


# get the top 10 words
top10 = sorted(rank.items(), key=lambda x: x[1], reverse=True)[:10]
print(top10)
