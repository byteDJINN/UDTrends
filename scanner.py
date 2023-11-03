import requests, json
from threading import Thread
from multiprocessing import Pool, Manager
import tqdm

def get(i):
  global dic
  if i > 100 and i % round(i, -len(str(i))+1) == 0: # logarithmically saving - every 10, 100, 1000, 10000, etc.
    print("SAVING")
    with open(str(name)+".json", "w", encoding="utf-8") as f:
      f.write(json.dumps(list(dic), indent=4, sort_keys=True))
  try:
    dic.append(requests.get(
        f"https://api.urbandictionary.com/v0/define?defid={end-i*frequency}").json()["list"][0])
  except:
    pass


# most recent word (https://www.urbandictionary.com/yesterday.php) will contain it)
end = 17968830
frequency = 10 # every nth word is saved <-- EDIT THIS
total = int(end/frequency)
name = "all-10"

print("Saving "+str(1/frequency*100)+"% of words")
# make dictionary an array of dictionaries
dic = Manager().list()
with Pool(20) as p:
  for _ in tqdm.tqdm(p.imap_unordered(get, range(1,end//frequency)), total=total):
    pass

with open(str(name)+".json", "w", encoding="utf-8") as f:
  f.write(json.dumps(list(dic), indent=4, sort_keys=True))