import requests, json
from multiprocessing import Pool
import tqdm

def get(i):
  try:
    return requests.get(f"https://api.urbandictionary.com/v0/define?defid={i}").json()["list"][0]
  except:
    pass

total = 2700000
dic = []
with Pool(100) as p:
  for _ in tqdm.tqdm(p.imap_unordered(get, range(1, total)), total=total):
    if _:
      dic.append(_)

with open("all.json", "w", encoding="utf-8") as f:
  f.write(json.dumps(dic, indent=4, sort_keys=True))