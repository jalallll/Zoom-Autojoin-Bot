from bot import Bot
import pandas as pd
import csv
from datetime import datetime

bot = Bot()
bot2 = Bot()

with open('file.csv') as csvfile:
    f = csv.reader(csvfile, delimiter=',')
    for i in f:
        starting = i[0]
        id = i[1]
        key = i[2]
time = datetime.now().strftime("%H:%M")

t = "9:30"

if starting == t:
    print("starting")
    o, go = bot.start(id, key)
    done = bot2.terminate("noo")
