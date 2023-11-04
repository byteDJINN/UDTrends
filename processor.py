import json
import math

data = open("all-10/all-v1000000.json", "r", encoding="utf-8").read()
data = json.loads(data)



rank = {}
authors = set()
threshold = 2021
# loop through words in curr 
for i in data:
  if i["word"] not in rank.keys() and i["author"] not in authors:
    authors.add(i["author"])
    if int(i["written_on"][0:4]) > threshold:
      rank[i["word"]] = 1
    else:
      rank[i["word"]] = -1
  elif i["author"] not in authors:
    authors.add(i["author"])
    if int(i["written_on"][0:4]) > threshold:
      rank[i["word"]] += 1
    else:
      rank[i["word"]] -= 1


# get the top 10 words
top10 = sorted(rank.items(), key=lambda x: x[1], reverse=True)[:20]
print("\n".join([i[0] for i in top10]))