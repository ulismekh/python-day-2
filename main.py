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

def analyze(*args, **kwargs):
  squares = [i ** 2 for i in args if i % 2 == 0]
  name = kwargs["name"]

  return f"Имя: {name}\nЧётные квадраты: {squares}"

print(analyze(1, 2, 3, 4, 5, 6, name="Ulugbek"))