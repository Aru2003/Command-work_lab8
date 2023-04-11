categories = ['транспортные расходы', 'обед', 'продукты', 'развлечения', 'одежда', 'коммунальные услуги', 'другие расходы']
expenses = [[] for _ in range(7)] 
for i in range(7):
    print(f'Введите расходы за {i+1}-й день недели')
    for j, cat in enumerate(categories):
        expense = float(input(f'{cat}: '))
        expenses[i].append(expense)

total_expenses = sum(sum(daily_expenses) for daily_expenses in expenses)

print('\nРасходы за неделю:')
for i in range(7):
    print(f'{i+1}-й день: {sum(expenses[i])} тг')
print(f'Общий объем расходов за неделю: {total_expenses} тг')