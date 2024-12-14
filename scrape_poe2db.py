import requests
from bs4 import BeautifulSoup
import json

URL = "https://poe2db.tw/us/Distilled#DistilledEmotionsPassives"
r = requests.get(URL)

distilled_emotions = {}
distilled_emotions["distilled_emotions"]  = []

soup = BeautifulSoup(r.content, 'html5lib') 
table = soup.find_all('tr')
table = table[12:]

list_of_all_emotions = set([])
 
for d_emotion in table:
    whole_line = d_emotion.get_text(' ')
    first_dist = whole_line.split(" ")[0] +" "+ whole_line.split(" ")[1]
    second_dist = whole_line.split(" ")[2] +" "+ whole_line.split(" ")[3]
    third_dist = whole_line.split(" ")[4] +" "+ whole_line.split(" ")[5]

    list_of_all_emotions.add(first_dist)
    list_of_all_emotions.add(second_dist)
    list_of_all_emotions.add(third_dist)

    remaining_text = ""
    for word in whole_line.split(" ")[6:]:
        remaining_text = remaining_text + " " + word
    distilled_emotions["distilled_emotions"].append({"emotions": [first_dist, second_dist, third_dist], "text": remaining_text[1:]})

with open("distilled_emotions.json", "w") as my_file:
    json.dump(distilled_emotions, my_file)