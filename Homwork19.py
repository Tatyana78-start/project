"""
Создайте класс Car с полями mass, km, power, speed, brand и реализуйте методы info()
 для вывода полной информации об автомобиле на экран
"""

class Car:
    def __init__(self, brand, power, year):
        self.brand = brand
        self.power = power
        self.year = year

    def display_info(self):
        print(self)

    def __str__(self):
        return f""" Автомобиль:
    Марка: {self.brand}
    Мощь: {self.power}
    Год: {self.year}"""


def main():
    car = Car("BMW", "631", "2024")
    car.display_info()

if __name__ == '__main__':
    main()

"""
Добавьте в класс методы lock(), unlock() 
и соответствующие параметры, необходимые для этих функций.
"""

from threading import Thread, Lock
from time import sleep


class Counter:
    def __init__(self):
        self.value = 0
        self.lock = Lock()

    def increase(self, by):
        self.lock.acquire()

        current_value = self.value
        current_value += by

        sleep(0.1)

        self.value = current_value
        print(f'Значение counter: {self.value}')

        self.lock.release()


counter = Counter()

# создаем потоки
t1 = Thread(target=counter.increase, args=(10, ))
t2 = Thread(target=counter.increase, args=(20, ))

# запускаем потоки
t1.start()
t2.start()


# ждем завершения потоков
t1.join()
t2.join()


print(f'Значение counter в итоге: {counter.value}')

"""
Добавьте в класс методы start_engine(), stop_engine()
 и соответствующие параметры, необходимые для этих функций.
"""

def create_car(color, consumption, tank_volume, mileage=0):
    return {
        "color": color,
        "consumption": consumption,
        "tank_volume": tank_volume,
        "reserve": tank_volume,
        "mileage": mileage,
        "engine_on": False
    }


def start_engine(car):
    if not car["engine_on"] and car["reserve"] > 0:
        car["engine_on"] = True
        return "Двигатель запущен."
    return "Двигатель уже был запущен."


def stop_engine(car):
    if car["engine_on"]:
        car["engine_on"] = False
        return "Двигатель остановлен."
    return "Двигатель уже был остановлен."


def drive(car, distance):
    if not car["engine_on"]:
        return "Двигатель не запущен."
    if car["reserve"] / car["consumption"] * 100 < distance:
        return "Малый запас топлива."
    car["mileage"] += distance
    car["reserve"] -= distance / 100 * car["consumption"]
    return f"Проехали {distance} км. Остаток топлива: {car['reserve']} л."


def refuel(car):
    car["reserve"] = car["tank_volume"]


def get_mileage(car):
    return f"Пробег {car['mileage']} км."


def get_reserve(car):
    return f"Запас топлива {car['reserve']} л."


car_1 = create_car(color="black", consumption=10, tank_volume=55)

print(start_engine(car_1))
print(drive(car_1, 100))
print(drive(car_1, 100))
print(drive(car_1, 100))
print(drive(car_1, 300))
print(get_mileage(car_1))
print(get_reserve(car_1))
print(stop_engine(car_1))
print(drive(car_1, 100))