#-----------------------Задача--------------#
'''
напечатать полый ромб (заданы длина, ширина и символ) при помощи цикла for
'''
def hollow_half_diamond(N):
    for i in range( 1, N + 1):
        for j in range(1, i + 1):

            if i == j or j == 1:
                print("#", end =" ")

            else:
                print(" ", end =" ")
        print()

    for i in range(N - 1, 0, -1):

        for j in range(1, i + 1):

            if j == 1 or i == j:
                print("#", end =" ")

            else:
                print(" ", end =" ")

        print()

if __name__ == "__main__":
    N = 7
    hollow_half_diamond( N )