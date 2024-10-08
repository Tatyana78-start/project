#.........................задача................#

'''
Дано число num(значение задаете сами). Напечатать
“num>0”, если число больше 0, иначе - “num<0”
'''

x = float(input())
if (x > 0) and (x != 7):
    print('Number is positive')
elif x < 0:
    print('Number is negative')
elif x == 0:
    print('Number is equal to zero')
elif x == 7:
    print('Good bye!')

#.........................Задача.................#
'''
Вывести на экран число(может быть любым), если
последняя цифра числа равна 8
'''

x = int(input())
print (x % 10)
