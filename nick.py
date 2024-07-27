import os
nick = input("[?] Введите никнейм -> ")
print("\n[!] Instagram -> https://www.instagram.com/" + nick)
print("[!] TikTok -> https://www.tiktok.com/@" + nick)
print("[!] Twitter -> https://twitter.com/" + nick)
print("[!] Facebook -> https://www.facebook.com/" + nick)
print("[!] Youtube -> https://www.youtube.com/@" + nick)
print("[!] Telegram -> https://t.me/" + nick)
print("[!] Roblox -> https://www.roblox.com/user.aspx?username=" + nick)
print("[!] Twitch -> https://www.twitch.tv/" + nick)

back = input("\n[?]Вернуться в главное меню? Yes/No -> ")
if back == "Yes":
    os.system("clear")
    os.system("python main.py")

if back == "No":
    print("[!] Хорошо, вы не вернетесь в главное меню")

