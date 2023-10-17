money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
i = 0
while True:
    loan = spend - salary
    budget = salary + loan
    money_capital -= loan
    spend *= 1 + increase
    if money_capital < 0:
        break
    else: i += 1

print("Количество месяцев, которое можно протянуть без долгов:", i)
