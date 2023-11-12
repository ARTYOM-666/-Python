# TODO решите задачу
import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

        sum_of_multiplications = sum([item['score'] * item['weight'] for item in data])

    return round(sum_of_multiplications, 3)

print(task())
