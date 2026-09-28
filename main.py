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

numbers = [5, 12, 7, 3, 20, 8]

print(numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5])

smallest = min(numbers)

print("Самое маленькое число: ", smallest)

biggest = max(numbers)

print("Самое большое число: ", biggest)