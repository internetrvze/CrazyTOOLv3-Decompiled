import urllib.request
import json
import os
import random  # Importing the random module
import threading
import requests

phone = input("[?] Введите номер телефона -> ")
getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone

try:
    infoPhone = urllib.request.urlopen(getInfo)
    infoPhone = json.load(infoPhone)  # Move this line inside the try block
except:
    print("\n[!] - Ошибка номер недействительный - [!]\n")

print(u"Number: ", "+" + phone)
print(u"Country: ", infoPhone["country"]["name"])
print(u"Region: ", infoPhone["region"]["name"])
print(u"District: ", infoPhone["region"]["okrug"])
print(u"Operator: ", infoPhone["0"]["oper"])
print(u"Continent: ", infoPhone["country"]["location"])
print(u"Telegram: t.me/" + phone)

back = input("\n[?] Вернуться в главное меню? Yes/No -> ")

if back == "Yes":
    os.system("clear")
    os.system("python main.py")
if back == "No":
    print("[!] Хорошо вы не вернетесь в главное меню")