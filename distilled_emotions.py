import json
from collections import OrderedDict
import copy

with open('distilled_emotions.json') as json_data:
    d = json.load(json_data)
    json_data.close()

tier_list = OrderedDict({
    'Distilled Ire': 1,
    'Distilled Guilt': 3,
    'Distilled Greed': 9,
    'Distilled Paranoia': 27,
    'Distilled Envy': 81,
    'Distilled Disgust': 243,
    'Distilled Despair': 729,
    'Distilled Fear': 2187,
    'Distilled Suffering': 6561,
    'Distilled Isolation': 19683,
})

emotions_have = {}

emotions_have["Distilled Ire"] = input("Amount of Distilled Ire ")
emotions_have["Distilled Guilt"] = input("Amount of Distilled Guilt ")
emotions_have["Distilled Greed"] = input("Amount of Distilled Greed ")
emotions_have["Distilled Paranoia"] = input("Amount of Distilled Paranoia ")
emotions_have["Distilled Envy"] = input("Amount of Distilled Envy ")
emotions_have["Distilled Disgust"] = input("Amount of Distilled Disgust ")
emotions_have["Distilled Despair"] = input("Amount of Distilled Despair ")
emotions_have["Distilled Fear"] = input("Amount of Distilled Fear ")
emotions_have["Distilled Suffering"] = input("Amount of Distilled Suffering ")
emotions_have["Distilled Isolation"] = input("Amount of Distilled Isolation ")

def calculate_cost(provisional_emotions_have, tier_list, current_emotion):
    cost = tier_list[current_emotion]
    start_counting = False
    can_make = False
    saved_provisional_emotions_have = provisional_emotions_have
    for emotion in reversed(provisional_emotions_have):
        if emotion == current_emotion:
            start_counting = True
            continue
        if start_counting:
            if cost > int(provisional_emotions_have[emotion]) * tier_list[emotion]:
                cost = cost - int(provisional_emotions_have[emotion])
                provisional_emotions_have[emotion] = 0
            else:
                value_of_emotion_have = int(provisional_emotions_have[emotion]) * tier_list[emotion]
                value_of_emotion_have = value_of_emotion_have - cost
                ammount_of_emotion = value_of_emotion_have / tier_list[emotion]
                provisional_emotions_have[emotion] = ammount_of_emotion
                can_make = True
        if can_make:
            return can_make, provisional_emotions_have
    return can_make, saved_provisional_emotions_have

for distilled_emotion in d["distilled_emotions"]:
    can_anoint = True
    provisional_emotions_have = copy.copy(emotions_have)
    emotions_check = 0
    for emotion in distilled_emotion["emotions"]:
        if emotions_check == 3:
            break
        current_emotion = emotion
        if distilled_emotion["emotions"].count(current_emotion) == 1:
            emotions_check +=1
            if int(provisional_emotions_have[current_emotion]) < 1:
                can_make, provisional_emotions_have = calculate_cost(provisional_emotions_have, tier_list, current_emotion)
                if not can_make:
                    can_anoint = False
            else:
                provisional_emotions_have[emotion] = int(provisional_emotions_have[emotion]) - 1
        if distilled_emotion["emotions"].count(current_emotion) == 2:
            emotions_check +=2
            if int(provisional_emotions_have[current_emotion]) == 1:
                can_make, provisional_emotions_have = calculate_cost(provisional_emotions_have, tier_list, current_emotion)
                if not can_make:
                    can_anoint = False
                provisional_emotions_have[emotion] = int(provisional_emotions_have[emotion]) - 1
            if int(provisional_emotions_have[current_emotion]) == 0:
                can_make, provisional_emotions_have = calculate_cost(provisional_emotions_have, tier_list, current_emotion)
                if not can_make:
                    can_anoint = False
                can_make, provisional_emotions_have = calculate_cost(provisional_emotions_have, tier_list, current_emotion)
                if not can_make:
                    can_anoint = False
            else:
                provisional_emotions_have[emotion] = int(provisional_emotions_have[emotion]) - 2

        if distilled_emotion["emotions"].count(current_emotion) == 3:
            emotions_check +=3
            if int(provisional_emotions_have[current_emotion]) == 2:
                can_make, provisional_emotions_have = calculate_cost(provisional_emotions_have, tier_list, current_emotion)
                if not can_make:
                    can_anoint = False
                provisional_emotions_have[emotion] = int(provisional_emotions_have[emotion]) - 2
            if int(provisional_emotions_have[current_emotion]) == 1:
                can_make, provisional_emotions_have = calculate_cost(provisional_emotions_have, tier_list, current_emotion)
                if not can_make:
                    can_anoint = False
                can_make, provisional_emotions_have = calculate_cost(provisional_emotions_have, tier_list, current_emotion)
                if not can_make:
                    can_anoint = False
                provisional_emotions_have[emotion] = int(provisional_emotions_have[emotion]) - 1
            if int(provisional_emotions_have[current_emotion]) == 0:
                can_make, provisional_emotions_have = calculate_cost(provisional_emotions_have, tier_list, current_emotion)
                if not can_make:
                    can_anoint = False
                can_make, provisional_emotions_have = calculate_cost(provisional_emotions_have, tier_list, current_emotion)
                if not can_make:
                    can_anoint = False
                can_make, provisional_emotions_have = calculate_cost(provisional_emotions_have, tier_list, current_emotion)
                if not can_make:
                    can_anoint = False
            else:
                provisional_emotions_have[emotion] = int(provisional_emotions_have[emotion]) - 3
    if can_anoint:
        print (distilled_emotion)