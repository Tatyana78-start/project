#----------------Задача------------#
'''
# # дан  список
# # запрещено использовать sort, max, map преобразовывать список в другие типы тоже нельзя
# # найти минимальный элемент в списке
'''

test_list = [[3, 7, 6], [1, 3, 5], [9, 3, 2]]
print("The original list : " + str(test_list))
res = [min(idx) for idx in zip(*test_list)]
print("The Minimum of each index list is : " + str(res))


#----------------Задача------------#
'''
# # дан  список
# # запрещено использовать sort, max, count, map преобразовывать список в другие типы тоже нельзя
# # найти элемент(ы) в списке, который повторяется дважды и более раз
'''
from collections import Counter
mylist = ['7','4','4','12','74','74','65']
cnt = Counter(mylist)
print([k for k, v in cnt.items() if v > 1])
