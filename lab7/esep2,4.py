n = int(input()) # количество работников
vacations = {} # словарь для хранения графика
# заполнение словаря
for i in range(n):
    name, day, month = input().split(" ")
    if month not in vacations:
        vacations[month] = [name]
    else:
        vacations[month].append(name)

# обработка запроса
query_month = input()
if query_month in vacations:
    print(" ".join(vacations[query_month]))
else:
    print()