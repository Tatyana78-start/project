# class Computer:
#     def __init__(self, cpu="intel core i7 13700k", gpu="nvidia rtx 4070", ram=16, rom=512):
#         self.cpu = cpu
#         self.gpu = gpu
#         self.ram = ram
#         self.rom = rom
#
#     def info(self):
#         print(self)
#
#     def __str__(self):
#         info = (f"cpu: {self.cpu}\n"
#                 f"gpu: {self.gpu}\n"
#                 f"ram: {self.ram}gb\n"
#                 f"rom: {self.rom}gb\n")
#         return info
#
#
# notebook = Computer(gpu="nvidia gtx 1660")
# print(notebook)
#
# comp = Computer(cpu="amd ryzen 9 7900x", gpu="nvidia rtx 4090", ram=32, rom=4096)
# print(comp)



# class Car:
#     def __init__(self, model):
#         self.model = model
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         if model < 2000:
#             self.__model = 2000
#         elif model > 2018:
#             self.__model = 2018
#         else:
#             self.__model = model
#
#     def getCarModel(self):
#         return "Год выпуска модели " + str(self.model)
#
#
# carA = Car(2088)
# print(carA.getCarModel())


