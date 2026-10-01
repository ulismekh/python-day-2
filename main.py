# number = int(input("Введите число: "))

# if number % 2 == 0:
#   print("Четное число")

# else:
#   print("Нечетное число")

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))

# if a < b and a < c:
#   print("Самое маленькое число,", a)

# elif a > b and b < c:
#   print("Самое маленькое число, ", b)

# else:
#   print("Самое маленькое число, ", c)

# numbers = [5, 12, 7, 3, 20, 8]

# print(numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5])

# smallest = min(numbers)

# print("Самое маленькое число: ", smallest)

# biggest = max(numbers)

# print("Самое большое число: ", biggest)

# a = int(input("Введите число"))

# def square(a):
#   return a ** 2

# print(square(a))

# def multiply(*args):
#   result = 1

#   for number in args:
#     result *= number

#   return result

# print(multiply(2, 3, 4))

# def student(**kwargs):
#   print("Name: ", kwargs["name"])
#   print("Age: ", kwargs["age"])
#   print("Group: ", kwargs["group"])
  
# student (name="Ulugbek", age=19, group="302")

# def profile(*args, **kwargs):
#   print("Objects: ", args)
#   print("Data: ", kwargs)

# profile("Python", "Git", name="Ulugbek", age=19)

# numbers   = [i ** 2 for i in range(1, 11)]

# print(numbers)

# numbers = [i ** 3 for i in range(1, 11) if i % 2 == 1]

# print(numbers)

# squares = {i: i ** 3 for i in range(1, 11)}

# print(squares)

# numbers = [i ** 2 for i in range(1, 11) if i % 2 == 0]

# print(numbers)

# numbers = {i: i ** 2 for i in range(1, 11) if i % 2 == 0}

# print(numbers)

# def process_numbers(*args):
#   result = [i ** 2 for i in args if i % 2 == 0]
#   return result

# print(process_numbers(1, 2, 3, 4, 5, 6))

# def analyze(*args, **kwargs):
#   squares = [i ** 2 for i in args if i % 2 == 0]
#   name = kwargs["name"]

#   return f"Имя: {name}\nЧётные квадраты: {squares}"

# print(analyze(1, 2, 3, 4, 5, 6, name="Ulugbek"))

# class car:
#   def __init__(self, brand, model, year):
#     self.brand = brand
#     self.model = model
#     self.year = year

#   def info(self):
#     return f"{self.brand} {self.model}, {self.year} год"

#   def age(self, current_year):
#     return current_year - self.year

# class ElectricCar(car):
#   def __init__(self, brand, model, year, battery):
#     super().__init__(brand, model, year)
#     self.battery = battery

# car1 = car("Toyota", "Camry", 2020)
# car2 = car("Chevrolet", "cobalt", 2021)
# electrocar = ElectricCar("Tesla", "Model S", 2025, 70)

# print(car1.info())
# print(car2.info())
# print(electrocar.info())

# try:
#   a = int(input("Введите первое число: "))
#   b = int(input("Введите второе число: "))
#   print(a / b)
# except ValueError:
#   print("Введите число")
# except ZeroDivisionError:
#   print("На ноль делить нельзя!")

# age = int(input("Введите свой возраст: "))
# def set_age(age):
#   return age
# if age < 0:
#   raise ValueError("Возраст не может быть отрицательным")
# else:
#   print(age)

# try:
#    def set_age(age):
#     if age < 0:
#         raise ValueError("Возраст не может быть отрицательным")
#     return age
# except ValueError:
#    print("Введите число")

# age = int(input("Введите свой возраст: "))
# print(set_age(age))

# class BankAccount:
#   def __init__(self, owner, balance):
#     self.owner = owner
#     self.balance = balance
#   def deposit(self, amount):
#     if amount <= 0:
#         raise ValueError("Сумма должна быть больше 0")

#     self.balance += amount
#   def withdraw(self, amount):
#     if amount <= 0:
#         raise ValueError("Сумма должна быть больше 0")

#     if amount > self.balance:
#         raise ValueError("Недостаточно средств")

#     self.balance -= amount

# account = BankAccount("Ulugbek", 100000)

# account.deposit(50000)
# try:
#     account.withdraw(200000)
# except ValueError as e:
#    print(e)

# print(account.balance)

# with open("notes.txt", "r", encoding="utf-8") as file:
#     text = file.read()

# with open("notes.txt", "a", encoding="utf-8") as file:
#     file.write("\nФайлы изучены!")

# print(text)

# import json

# student = {
#     "name": "Ulugbek",
#     "age": 19,
#     "university": "TSMU",
#     "course": 3
# }

# with open("student.json", "w", encoding="utf-8") as file:
#     json.dump(student, file, ensure_ascii=False, indent=4)

# print("Name: ", student["name"])
# print("Age: ", student["age"])
# print("University: ", student["university"])
# print("Course: ", student["course"])

import greetings

print(greetings.hello("Ulugbek"))