tickets = int(input('Пожалуйста, укажите необходимое количество билетов:'))
price = 0
count = 0
for i in range(tickets):
    age = int(input(f'Пожалуйста, введите Ваш возраст:'))
    if 0 <= age < 18:
        print('Для Вас вход на конференцию бесплатный!')
        price += 0
        count += 1
    elif 18 <= age < 25:
        print('Стоимость билета 990 руб.')
        price += 990
        count += 1
    elif 25 <= age < 120:
        print('Стоимость билета 1390 руб.')
        price += 1390
        count += 1
    else:
        print('Пожалуйста, введите корректный возраст!')
print(f'Cтоимость {count} билетов - {price} руб.')
if tickets and count > 3:
        price = price / 100 * 90
        print(f'Cтоимость {count} билетов со скидкой 10% - {price} руб.')
