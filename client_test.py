import requests

API_URL = "http://127.0.0.1:8080/chat"

name = input("Adınız: ")
age = int(input("Yaşınız: "))

print("\nSohbet başladı. Çıkmak için 'quit' yazın")

while True:
    user_msg = input(f"{name}: ")
    if user_msg.lower() == "quit":
        print("Program sonlandırıldı.")
        break

    payload = {
        "name": name,
        "age": age,
        "message": user_msg
    }

    try:
        res = requests.post(API_URL, json=payload, timeout=30)

        if res.status_code == 200:
            print(f"Doktor Asistanı: {res.json()['response']}")
        else:
            print("Hata:", res.status_code, res.text)
    except requests.exceptions.RequestException as e:
        print("Bağlantı Hatası:", e)
