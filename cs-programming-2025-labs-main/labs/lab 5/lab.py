# Задание 1
s='1 2 3 4 5 6 7 8 9 10'
while '3' in s :
    if '3' in s :s=s.replace('3','30',1)
    print(s)
    break

# Задание 2
b = [2, 4, 6, 8, 10]
c = []
for i in range(5):
    c.append(b[i] * b[i])
print(b)
print(c)
print()

# Задание 3
d = [12, 45, 23, 67, 34]
max_num = d[0]
for num in d:
    if num > max_num:
        max_num = num
result = max_num / 5
print(d)
print(max_num)
print(result)
print()

# Задание 4
t = (5, 2, 8, 1)
all_ok = True
for x in t:
    if not type(x) == int:
        all_ok = False

if all_ok:
    lst = list(t)
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    print(tuple(lst))
else:
    print(t)
print()

# Задание 5
shop = {"молоко": 50, "хлеб": 30, "сыр": 200}
min_price = 999
max_price = 0
for item in shop:
    price = shop[item]
    if price < min_price:
        min_price = price
        min_item = item
    if price > max_price:
        max_price = price
        max_item = item
print(min_item, min_price)
print(max_item, max_price)
print()

# Задание 6
lst = ["a", "b", "c"]
d = {}
for x in lst:
    d[x] = x
print(d)
print()

# Задание 7
words = {"apple": "яблоко", "dog": "собака"}
r_words = {}
for eng in words:
    rus = words[eng]
    r_words[rus] = eng

w = input("Введите слово: ")
if w in r_words:
    print(r_words[w])
else:
    print("Нет")
print()

# Задание 8
import random
options = ["камень", "ножницы", "бумага", "ящерица", "спок"]
player = input("Выбери: ")
comp = random.choice(options)
print("Компьютер:", comp)

if player == comp:
    print("Ничья")
elif player == "камень" and comp in ["ножницы", "ящерица"]:
    print("Ты выиграл")
elif player == "ножницы" and comp in ["бумага", "ящерица"]:
    print("Ты выиграл")
elif player == "бумага" and comp in ["камень", "спок"]:
    print("Ты выиграл")
elif player == "ящерица" and comp in ["бумага", "спок"]:
    print("Ты выиграл")
elif player == "спок" and comp in ["камень", "ножницы"]:
    print("Ты выиграл")
else:
    print("Компьютер выиграл")
print()

# Задание 9
fruits = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]
res = {}
for fruit in fruits:
    letter = fruit[0]
    if letter not in res:
        res[letter] = []
    res[letter].append(fruit)
print(res)
print()

# Задание 10
students = [("Анна", [5,4,5]), ("Иван", [3,4,4]), ("Мария", [5,5,5])]
best_name = ""
best_avg = 0

for name, marks in students:
    total = 0
    for mark in marks:
        total += mark
    avg = total / 3
    if avg > best_avg:
        best_avg = avg
        best_name = name

print(best_name, best_avg)
