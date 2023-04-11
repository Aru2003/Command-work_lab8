# Количество номеров телефонов
n = int(input())

# Создаем пустой словарь
phone_book = {}

# Заполняем словарь
for i in range(n):
    phone, name = input().split(" ")
    phone_book[name] = phone

# поиск телефона
query = input()

# Ищем телефоны
if query in phone_book:
    print(phone_book[query])
else:
    print("Нет в телефонной книге")
