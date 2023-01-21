import random, json

with open('2023Hackathon\src\data\settings.json') as file: 
    file = json.load(file)

screensize = "1000x700"
title = "Hackathon App"

font = file['font']
fontSize = file['fontSize']

rgb =  (0, 255, 204)# (random.randint(0,255), random.randint(0,255), random.randint(0,255))
