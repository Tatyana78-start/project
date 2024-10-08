"""
Вам дан список продуктов. Нужно определить общее количество повторяющихся продуктов в этом списке
"""

from collections import Counter
counts = Counter(['яблоко', 'банан', 'яблоко', 'апельсин', 'банан', 'яблоко'])
print(counts)  # Counter({'яблоко': 3, 'банан': 2, 'апельсин': 1})



"""
Вам дан список строк. Нужно найти строку, которая встречается в списке наиболее часто.
"""


# Program to find most frequent
# element in a list

def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num


List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))