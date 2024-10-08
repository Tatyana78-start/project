"""
Создайте базовый класс Dog, который будет иметь атрибуты name и age.
 Затем создайте подклассы WorkingDog (с атрибутом job) и PetDog.
 Реализуйте методы, которые выводят информацию о
 работе собаки или о том, как она ведет себя как домашний питомец.
"""

# class Dog():
#     def __init__(self, name: str, age: int, weight: int):
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     def __repr__(self):
#         return '{}, Возраст: {}, Вес {} кг'.format(
#             self.name,
#             self.age,
#             self.weight
#         )
#
#
# class DogsList():
#     def __init__(self):
#         self.dogs = []
#
#     def add_dog(self, dog: Dog) -> None:
#         self.dogs.append(dog)
#
#     def count(self) -> int:
#         return len(self.dogs)
#
#     def average_age(self) -> float:
#         return sum((dog.age for dog in self.dogs)) / self.count
#
#     def min_age(self) -> Dog:
#         return min(self.dogs, key=lambda dog: dog.age)
#
#     def max_weight(self) -> Dog:
#         return max(self.dogs, key=lambda dog: dog.weight)
#
#
# def load_dog(path: str) -> Dog:
#     with open(path, 'r', encoding='utf-8') as file:
#         for line in file.readlines():
#             name, age, weight = line.split()
#             yield Dog(name, int(age), int(weight))
#
#
# dogs_list = DogsList()
# for dog in load_dog('dog.txt'):
#     dogs_list.add_dog(dog)
#
# for dog in dogs_list.dogs:
#     print(dog)
#
# print(f'Общее количество собак: {dogs_list.count()}')
# print(f'Самый маленький возраст у собаки {dogs_list.min_age()}')
# print(f'Самый большой вес у собаки {dogs_list.max_weight()}')


"""
2)	Создайте базовый класс Vehicle, который будет иметь атрибуты make, model и year. 
Затем создайте подклассы Car и Truck, добавив атрибуты, специфичные для 
каждого типа (например, passenger_capacity для автомобиля и payload_capacity для грузовика). 
Реализуйте метод для отображения информации о транспортном средстве.
"""

# class Vehicle:
#     def __init__(self, make, model, year, price):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.price = price
#
#     def display_info(self):
#         print(f"Марка: {self.make}"
#         f"\nМодель: {self.model}"
#         f"\nГод выпуска: {self.year}"
#         f"\nСтоимость: {self.price} руб")
#
# class Car(Vehicle):
#     def __init__(self, make, model, year, price, num_doors, body_style):
#         super().__init__(make, model, year, price)
#         self.num_doors = num_doors
#         self.body_style = body_style
#
# class Truck(Vehicle):
#     def __init__(self, make, model, year, price, bed_length, towing_capacity):
#         super().__init__(make, model, year, price)
#         self.bed_length = bed_length
#         self.towing_capacity = towing_capacity
#
#
# car = Car("Toyota", "Camry", 2022, 2900000, 4, "седан")
#
#
# truck = Truck("Ford", "F-MAX", 2023, 6000000, "6162", "13 т")
#
# car.display_info()
# truck.display_info()


"""
3)	Создайте базовый класс Animal, 
который будет иметь атрибуты name и species.
 Затем создайте подклассы Mammal и Bird, добавив методы,
  специфичные для каждого класса (например, метод make_sound() 
для млекопитающих и метод fly() для птиц).
"""

# class Animal:
#     def __init__(self, name, species, legs):
#         self.name = name
#         self.species = species
#         self.legs = legs
#
#     def voice(self):
#         print(f"{self.name} подает голос")
#
#     def move(self):
#         print(f"{self.name} дергает хвостом")
#
# class Dog(Animal):
#     def __init__(self, name, breed, legs):
#         super().__init__(name, breed, legs)
#         self.breed = breed
#
#     def bark(self):
#         print(f"{self.breed} {self.name} лает")
#
# class Bird(Animal):
#     def __init__(self, name, species, wingspan):
#         super().__init__(name, species, 2)
#         self.wingspan = wingspan
#
#     def fly(self):
#         print(f"{self.species} {self.name} летaeт")
#
# dog = Dog("Геральт", "доберман", 4)
# bird = Bird("Вася", "попугай", 2)
# dog.voice()
# bird.voice()
# dog.move()
# bird.move()
# dog.bark()
# bird.fly()




