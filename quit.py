import urllib.request
import json
import os
import random  # Importing the random module
import threading
import requests

quit = input("[?] Вы действительно хотите выйти? Yes/No -> ")
if quit == "Yes":
  print("[!] Досвидания")
if quit == "No":
  os.system("clear")
  os.system("python main.py")
