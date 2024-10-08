#-------------------Задача---------------------#
""""
Дано: Информация о заказах (название блюда, количество, цена).
Найти: Общую стоимость заказа, список уникальных блюд в меню.
Пример:
Входные данные:
{“Заказ 1”: ("Пицца", 2, 250),
“Заказ 2”: ("Салат", 1, 150),
“Заказ 3”: ("Пицца", 1, 250)}

Выходные данные:
Общая стоимость заказа: 900
Уникальные блюда в меню: {"Пицца", "Салат"}

"""
class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price =price

class Order:
    def __init__(self, table):
        self.table = table
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)
    def remove_dish(self,dish):
        if dish in self.dishes:
            self.dishes.remove(dish)
        else:
            print(f"{dish.name} Не найден в заказе.")

    def calculate_total(self):
        total_prise = sum(dish.price for dish in self.dishes)
        return total_prise

def print_order(order):
    print(f"Заказ для столика: {order.table}\n")
    print("Блюда в заказе:")
    for dish in order.dishes:
        print(f"{dish.name}: {dish.price} руб.")
        total_price =order.calculate_total()
        print(f"Общая стоимость заказа: {total_price} руб.\n")
#Создание блюда
dish1 = Dish("Пицца", 250)
dish2 = Dish("Салат", 150)
dish3 = Dish("Пицца", 250)

#Создание заказа
order1 = Order("Столик 1")
order2 = Order("Столик 2")
order3 = Order("Столик 3")

#Удаление блюда из заказа
order1.remove_dish(dish2)

#Добавление блюда в заказ
order1.add_dish(dish1)
order1.add_dish(dish3)
order2.add_dish(dish2)

#Вывод информации о заказе
print_order(order1)
print_order(order2)