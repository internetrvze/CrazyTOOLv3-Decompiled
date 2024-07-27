import urllib.request
import json
import os
import random  # Importing the random module
import threading
import requests

banner = """

░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄
░███████████████████████
░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓
░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░
▒░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░
░░█▓▓▓▓▓▌░▒▒▒▒▒▒▒▒
░▐█▓▓▓▓▓░░▒▒▒▒▒▒▒
░▐██████▌░▒▒▒▒▒▒

╔═╦═╦══╦══╦═╦╗ ╔══╦═╦═╦╗
║╔╣╬║╔╗╠══╠╗║║ ╚╗╔╣║║║║║
║╚╣╗╣╠╣║══╬╩╗║  ║║║║║║║╚╗
╚═╩╩╩╝╚╩══╩══╝  ╚╝╚═╩═╩═╝

┌───────────────────────────────────────────┐
│Разработчик: @Fr31zep ТГК: @crazytoolsoft  │
│───────────────────────────────────────────│
│                  FREE                     │
└───────────────────────────────────────────┘
┌────────────────────────────────────┬─────┬┐
│[1] Поиса по номеру                 │ v.3 ││    
│[2] Поиск по IP                     └─────┘│
│[3] Поиск по нику                          │
│[4] DDOS                                   │
│[5] Мануал по доксу                        │
│[6] Мануал по свату                        │
│[7] Мануал по сносу ТГ                     │
│[8] Генератор личности                     │
│[9] Генератор карты                        │
│[10] Поиск по базе данных                  │
│[11] Св@t б@нв0рD                          │
│[12] Информация                            │
│[13] Выход                                 │
└───────────────────────────────────────────┘

"""

print(banner)

choice = input("[?] Введите номер желаемой функции -> ")
if choice == "1":
    os.system("clear")
    os.system("python phone.py")

if choice == "2":
    os.system("clear")
    os.sytem("python ip.py")
    
if choice == "3":
    os.system("clear")
    os.system("python nick.py")

if choice == "4":
    os.system("clear")
    os.system("python ddos.py")

if choice == "5":
    os.system("clear")
    os.system("python doks.py")

if choice == "6":
    os.system("clear")
    os.system("python swat.py")

if choice == "7":
    os.system("clear")
    os.system("python snos.py")

if choice == "8":
    os.system("clear")
    os.system("python generate.py")

if choice == "9":
    os.system("clear")
    os.system("python card.py")
    
if choice == "10":
    os.system("clear")
    os.system("python searchb.py")

if choice == "11":
    os.system("clear")
    os.system("python antispam.py")
    
if choice == "12":
    os.system("clear")
    os.system("python info.py")

if choice == "13":
    os.system("clear")
    os.system("quit.py")
    
    
