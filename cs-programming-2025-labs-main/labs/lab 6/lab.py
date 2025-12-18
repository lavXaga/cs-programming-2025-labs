# Задание 1
def task1():
    data = input().split()
    num = float(data[0])
    from_u = data[1]
    to_u = data[2]
    
    # Конвертируем всё в секунды
    if from_u == "h":
        num = num * 3600
    elif from_u == "m":
        num = num * 60
    
    # Конвертируем из секунд в нужную единицу
    if to_u == "h":
        num = num / 3600
    elif to_u == "m":
        num = num / 60
    
    # Форматируем вывод
    if num == int(num):
        print(f"{int(num)}{to_u}")
    else:
        print(f"{num:.2f}{to_u}")


# Задание 2
def task2():
    a, n = map(int, input().split())
    
    if a < 30000:
        print("Ошибка")
        return
    
    # Бонус за сумму: каждые 10000 руб = +0.3%, максимум +5%
    bonus = (a // 10000) * 0.3
    if bonus > 5:
        bonus = 5
    
    # Базовая ставка по сроку
    if n <= 3:
        rate = 3.0
    elif n <= 6:  # 4-6 лет
        rate = 5.0
    else:  # более 6 лет
        rate = 2.0
    
    # Итоговая ставка
    rate = rate + bonus
    
    # Считаем сложный процент
    money = float(a)
    for _ in range(n):
        money = money + money * (rate / 100)
    
    # Прибыль
    profit = money - a
    print(f"{profit:.2f}")


# Задание 3
def task3():
    start, end = map(int, input().split())
    
    if start > end:
        print("Error!")
        return
    
    primes = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            primes.append(str(num))
    
    if not primes:
        print("Error!")
    else:
        print(" ".join(primes))


# Задание 4
def task4():
    n = int(input())
    
    if n <= 2:
        print("Error!")
        return
    
    matrix1 = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix1.append(row)
    
    matrix2 = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix2.append(row)
    
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    for row in result:
        print(" ".join(map(str, row)))


# Задание 5
def task5():
    text = input().lower()
    
    cleaned = ""
    for char in text:
        if char.isalpha():
            cleaned += char
    
    if cleaned == cleaned[::-1]:
        print("Да")
    else:
        print("Нет")
