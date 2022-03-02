while True:
    quant = int(input("Введите количество участников конференции "))
    if quant <= 0:
        print("Введено неверное количество участников")
        continue
    else:
        break
price = 0
price_sum = 0
age_list = []

for i in range(quant):
    while True:
        age = int(input(f'Введите возраст участника {i+1} '))
        if age > 100 or age <= 0:
            print("Недействительный возраст")
            continue
        else:
            break
    age_list.append(age)

for i in age_list:
    if 18 <= i <= 25:
        price += 990
    elif i > 25:
        price += 1390
print(f"Сумма без скидки {price} рублей")
if quant > 3:
    price_sum = 0.9 * price
else:
    price_sum = price
print(f'Сумма к оплате {price_sum} рублей')