# задание 1
name = input(" имя: ")
age = input("возраст: ")

for i in range(10):
    print(f"Меня зовут {name} и мне {age} лет")

# задание 2
num = int(input(" число от 1 до 9: "))

print(f"Таблица умножения  {num}:")
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

# задание 3

for i in range(0, 101, 3):
    print(i, end=" ")
print()

# задание 4
n = int(input(" число для вычисления факториала: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Факториал числа {n} равен {factorial}")

# задание 5
print("Числа от 20 до 0:")
i = 20
while i >= 0:
    print(i, end=" ")
    i -= 1
print()

# задание 6
limit = int(input(" предел для чисел Фибоначчи: "))
a, b = 0, 1

print(f"Числа Фибоначчи до {limit}:")
while a <= limit:
    print(a, end=" ")
    a, b = b, a + b
print()

# задание 7
text = input("Введите строку: ")
result = ""

for i, char in enumerate(text, 1):
    result += char + str(i)

print(f"Результат: {result}")

# задание 8
while True:
    numbers = input(" два числа через пробел: ").split()
    if len(numbers) == 2:
        try:
            num1 = float(numbers[0])
            num2 = float(numbers[1])
            print(f"Сумма равна: {num1 + num2}")
        except ValueError:
            print("Ошибка: введите числа!")
