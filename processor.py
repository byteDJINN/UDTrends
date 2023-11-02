import json
import math

start = open("2003-1.json", "r", encoding="utf-8").read()
start = json.loads(start)
end = open("2003-2.json", "r", encoding="utf-8").read()
end = json.loads(end)

rank0 = {}
rank1 = {}
# loop through words in curr 
for i in start:
  if i["word"] not in rank0.keys():
    rank0[i["word"]] = i["thumbs_up"] - i["thumbs_down"]
  elif i["thumbs_up"] - i["thumbs_down"] > rank0[i["word"]]:
    rank0[i["word"]] = i["thumbs_up"] - i["thumbs_down"]

for i in end:
  if i["word"] not in rank1.keys():
    rank1[i["word"]] = i["thumbs_up"] - i["thumbs_down"]
  elif i["thumbs_up"] > rank1[i["word"]]:
    rank1[i["word"]] = i["thumbs_up"] - i["thumbs_down"]

final = {}
#w give each word a final score based on its rank2 - rank 1 / (rank 1 - rank 0)
for i in rank0:
  if i in rank1 and (rank1[i] > 1000):
    final[i] = rank1[i] / rank0[i] + math.log(rank1[i])

# get the top 10 words
top10 = sorted(final.items(), key=lambda x: x[1], reverse=True)[:10]
print(top10)
