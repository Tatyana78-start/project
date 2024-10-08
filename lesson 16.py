# f = open('data.txt', 'r', encoding='utf-8')  # Относительный путь
# # open('C:\\Users\\Artem\\Desktop\\Top academy\\projects\\pythonProject22\\data.txt')
#
# data = f.read()
# f.close()
#
# print(data)
#
# f = open('data2.txt', 'w', encoding='utf-8')
# f.write(data + "!!")
# f.close()
#
# f = open('data2.txt', 'a', encoding='utf-8')
# f.write(" | " + "Hello")
# f.close()

# with open('data.txt', 'r', encoding='utf-8') as file:
#     line = file.readline().rstrip('\n')
#     while line:
#         print(line)
#         line = file.readline().rstrip('\n')

# with open('data.txt', 'r', encoding='utf-8') as file:
#     lines = list(map(lambda x: x.rstrip('\n'), file.readlines()))
# print(lines)

# with open('data2.txt', 'w', encoding='utf-8') as file:
#     file.writelines(['Всем\n', 'Привет\n'])


import csv

# peoples = []
# with open('data.csv', newline='', encoding='utf-8') as file:
#     reader = csv.reader(file, delimiter=';')
#     header = []
#     for row in reader:
#         if header == []:
#             header = row
#             continue
#         d = {}
#         for index, key in enumerate(header):
#             d[key] = row[index]
#         peoples.append(d)
#
# print(peoples)

# with open('data.csv', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file, delimiter=';')
#     for row in reader:
#         print(row)
#         print(f'Зовут {row['Имя']}, {row['Возраст']} лет')

#
# import json
#
# data = {
#     "name": "John",
#     "surname": "Snow",
#     "age": 26,
#     "test": True
# }
# with open('data.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)
#
# with open('data.json') as json_file:
#     data = json.load(json_file)
#
# print(data)
