import requests, json
from threading import Thread
from multiprocessing import Pool, Manager
import tqdm

def get(i):
  global dic
  if i % round(i, -len(str(i))+1) == 0: # logarithmically saving - every 10, 100, 1000, 10000, etc.
    print("SAVING")
    with open(str(name)+".json", "w", encoding="utf-8") as f:
      f.write(json.dumps(list(dic), indent=4, sort_keys=True))
  try:
    dic.append(requests.get(
        f"https://api.urbandictionary.com/v0/define?defid={end-i}").json()["list"][0])
  except:
    pass


# most recent word (https://www.urbandictionary.com/yesterday.php) will contain it)
end = 17968830
total = 2000000 # the number of words to check (it counts backwards)

name = "recent"
# make dictionary an array of dictionaries
dic = Manager().list()
with Pool(20) as p:
  for _ in tqdm.tqdm(p.imap_unordered(get, range(1, total)), total=total):
    pass

with open(str(name)+".json", "w", encoding="utf-8") as f:
  f.write(json.dumps(list(dic), indent=4, sort_keys=True))