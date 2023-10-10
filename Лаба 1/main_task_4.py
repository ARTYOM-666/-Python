users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статистикой посещений
about_sites = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

about_sites["Общее количество"] = len(users)
about_sites["Уникальные посещения"] = len(set(users))

print(about_sites)