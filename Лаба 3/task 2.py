# TODO Напишите функцию find_common_participants

def find_common_participants(first_group, second_group, sign=','):
    a = first_group.split(sign)
    b = second_group.split(sign)
    c = list(set(a).intersection(b))
    return c

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, sign= '|')
print(f'Общие участники: ', result)

# TODO Провеьте работу функции с разделителем отличным от запятой


