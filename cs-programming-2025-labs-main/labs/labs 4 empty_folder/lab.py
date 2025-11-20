# задание 1

 try:
      temperature = float(input("Введите температуру: "))
      if temperature >= 20:
        print("Кондиционер выключен")
      else:
        print("Кондиционер включен")
 except ValueError:
       print("Ошибка")

# задание 2

try:
       month = int(input("Введите номер месяца: "))
    if month in [12, 1, 2]:
         print("Это зима")
       elif month in [3, 4, 5]:
           print("Это весна")
       elif month in [6, 7, 8]:
           print("Это лето")
       elif month in [9, 10, 11]:
           print("Это осень")
      else:
            print("Ошибка")
    except ValueError:
        print("Ошибка")

# задание 3

 try:
     dog_age = float(input("Введите возраст собаки (в годах): "))
        
    if dog_age < 1:
        print("Ошибка")
       elif dog_age > 22:
           print("Ошибка")
    else:
          if dog_age <= 2:
            human_age = dog_age * 10.5
         else:
               human_age = 21 + (dog_age - 2) * 4
            
            print(f"Возраст собаки в человеческих годах: {human_age}")
    except ValueError:
        print("Ошибка")

# задание 4

 try:
     number = input("Введите число: ")
        
     last_digit = int(number[-1])
     even_last = last_digit % 2 == 0
        
      digit_sum = sum(int(digit) for digit in number if digit.isdigit())
      divisible_by_3 = digit_sum % 3 == 0
        
      if even_last and divisible_by_3:
         print(f"Число {number} делится на 6")
      else:
          print(f"Число {number} не делится на 6")
            
  except ValueError:
       print("Ошибка")

# задание 5

  password = input("Введите пароль: ")
    
  errors = []
    
if len(password) < 8:
      errors.append("длина менее 8 символов")
    
has_upper = any(char.isupper() for char in password)
 if not has_upper:
      errors.append("отсутствуют заглавные буквы")
    
 has_lower = any(char.islower() for char in password)
 if not has_lower:
  errors.append("отсутствуют строчные буквы")
    
 has_digit = any(char.isdigit() for char in password)
 if not has_digit:
       errors.append("отсутствуют цифры")
    
has_special = any(not char.isalnum() for char in password)
    if not has_special:
        errors.append("отсутствуют специальные символы")
    
    if errors:
        print(f"Пароль ненадежный: {', '.join(errors)}")
    else:
        print("Пароль надежный")

# задание 6

    try:
        year = int(input("Введите год: "))
        
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} - високосный год")
        else:
            print(f"{year} - не високосный год")
            
    except ValueError:
        print("Ошибка")

# задание 7

    try:
        numbers = input("Введите три числа: ").split()
        if len(numbers) != 3:
            print("Ошибка")
            return
            
        a, b, c = map(float, numbers)
        
        min_number = a
        if b < min_number:
            min_number = b
        if c < min_number:
            min_number = c
            
        print(f"Наименьшее число: {min_number}")
        
    except ValueError:
        print("Ошибка")

# задание 8

    try:
        purchase_amount = float(input("Введите сумму покупки: "))
        
        if purchase_amount < 1000:
            discount = 0
        elif purchase_amount <= 5000:
            discount = 5
        elif purchase_amount <= 10000:
            discount = 10
        else:
            discount = 15
        
        final_amount = purchase_amount * (1 - discount / 100)
        
        print(f"Ваша скидка: {discount}%")
        print(f"К оплате: {final_amount}")
        
    except ValueError:
        print("Ошибка")

# задание 9

    try:
        hour = int(input("Введите час (0-23): "))
        
        if 0 <= hour <= 5:
            print("Сейчас ночь")
        elif 6 <= hour <= 11:
            print("Сейчас утро")
        elif 12 <= hour <= 17:
            print("Сейчас день")
        elif 18 <= hour <= 23:
            print("Сейчас вечер")
        else:
            print("Ошибка")
            
    except ValueError:
        print("Ошибка")

# задание 10

    try:
        number = int(input("Введите число: "))
        
        if number <= 1:
            print(f"{number} - не простое число")
            return
        
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(f"{number} - простое число")
        else:
            print(f"{number} - составное число")
            
    except ValueError:
        print("Ошибка")


   
  
