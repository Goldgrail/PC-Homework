from pprint import pprint
import requests

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
resp = requests.get(url)
full_data_list = resp.json()

three_heroes_dict = {}
heroes_names = ["Hulk", "Captain America","Thanos"]
for heroes in full_data_list:
    for man in heroes_names:
        for k, v in heroes.items():
            if heroes["name"] == man:
                three_heroes_dict[man] = heroes["powerstats"]["intelligence"]

for k, v in three_heroes_dict.items():
    if v == max(three_heroes_dict.values()):
        print(f' Самый умный герой {k}')





