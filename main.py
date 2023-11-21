import csv
import json

# Открытие CSV-файла и чтение данных
with open('test.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Конвертация в JSON
json_data = json.dumps(rows, indent=4)

# Запись в файл
with open('test.json', 'w') as f:
    f.write(json_data)