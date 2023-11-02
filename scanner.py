import requests, json
from threading import Thread
from multiprocessing import Pool, Manager
import tqdm

def get(i):
  global dic
  try:
    dic.append(requests.get(
        f"https://api.urbandictionary.com/v0/define?defid={i}").json()["list"][0])
  except:
    pass


end = 17967225
start = end - 100000

name = "recent"
# make dictionary an array of dictionaries
dic = Manager().list()
with Pool(20) as p:
  for _ in tqdm.tqdm(p.imap_unordered(get, range(start, end)), total=end - start):
    pass

with open(str(name)+".json", "w", encoding="utf-8") as f:
  f.write(json.dumps(list(dic), indent=4, sort_keys=True))