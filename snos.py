import urllib.request
import json
import os
import random  # Importing the random module
import threading
import requests

snos = """
Провоцируем жертву на угрозы, оски, буллинг и тд. Дальше пишем на почту DMCA@telegram.org. В письме указывем скриншоты булинга, угроз и тд. "Здраствуйте, хочу подать жалобу на (юзер и айди типа).  уважением, пользователь" и все, главное скриншоты - доказательства .
"""
print(snos)
back = input("[?] Вернуться в главное меню? Yes/No -> ")
if back == "Yes":
   os.system("clear")
   os.system("python main.py")
if back == "No":
   print("[!] Хорошо, вы не вернетесь в главное меню")