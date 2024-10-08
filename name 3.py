#---------------------------Задача----------------------------#
'''
Дано два числа. Найдите наибольшее четное число среди них.
Если оно не существует, выведите фразу "not found"
'''
a = int (input(('Введите первое число ')))
b = int (input(('Введите второе число ')))
c = int (input(('Введите третье число ')))
d = int (input(('Введите четвертое число ')))
if a%2!=0 and b%2!=0 and c%2!=0 and d%2!=0:
    print ('not found')
else:
    while max(a,b,c,d)%2 !=0:
        if max(a,b,c,d) == a and a%2!=0:
            a = 0
            continue
        if max(a,b,c,d) == b and b%2!=0:
            b = 0
            continue
        if max(a,b,c,d) == c and c%2!=0:
            c = 0
            continue
        if max(a,b,c,d) == d and d%2!=0:
            d = 0
            continue
    else:
        print ( max(a,b,c,d) )
