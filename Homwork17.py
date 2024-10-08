"""
1.Напишите функцию подсчета периметра прямоугольника
с двумя аргументами width и height.
Функция должна возвращать значение.
"""

sideA = int(input("Width: "))
sideB = int(input("Height: "))

perimeter = (sideA + sideB) * 2;

print("Периметр прямоугольника: ", perimeter)

"""
2.	Напишите функцию возведения числа в степень
 с двумя аргументами number и degree.
Функция должна возвращать значение.
"""
def exponentiation_by_squaring(number,degree ):
    result = 1
    while degree > 0:
        if degree % 2 == 1:
            result *= number
        degree= degree >> 1
        number *= number
    return result


print(exponentiation_by_squaring(2, 3))  # 2^3 = 8


"""
3.	Напишите функцию, подсчитывающую количество слов 
 в введенном тексте с одним аргументом text.
 Функция должна вернуть количество слов.
"""
import os
def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n","")
    text = text.replace(",", "").replace(".","").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words

def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if words in words_dict:
            words_dict[word] = words_dict[dict] + 1
        else:
            words_dict[word] = 1
        return  words_dict

def main():
    filename = input("Введите путь к файлу: ")
    if not os.path.exists(filename):
        print("Указаный файл не существует")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print(f"Кол-во слов: {len(words)}")
        print(f"Кол-во уникальных слов {len(words_dict)}")
        print("Все использованные слова ")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == "__main__":
    main()
