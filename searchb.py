import os
path = input("\n[?] Введите путь к БД -> ")
search_text = input("\n[?] Введите текст:  ")
print()
try:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if search_text in line:
                print("[+] Результат: " + line.strip())
                print()
            break
        else:
            print("[!] Текст не найден.\n")
except:
    try:
        with open(path, "r", encoding="cp1251") as f:
            for line in f:
                if search_text in line:
                    print("[+] Результат: " + line.strip())
                    print()
                    break
            else:
                print("[!] Текст не найден.\n")
    except:
        try:
            with open(path, "r", encoding="cp1252") as f:
                for line in f:
                    if search_text in line:
                        print("[+] Результат: " + line.strip())
                        print()
                        break
                else:
                    print("[!] Текст не найден.\n")
        except:
            print("[!] Произошла ошибка, проверьте ввод данных\n")


back = input("[?] Вернуться в главное меню? Yes/No -> ")
if back == "Yes":
   os.system("clear")
   os.system("python main.py")
if back == "No":
   print("[!] Хорошо, вы не вернетесь в главное меню")
