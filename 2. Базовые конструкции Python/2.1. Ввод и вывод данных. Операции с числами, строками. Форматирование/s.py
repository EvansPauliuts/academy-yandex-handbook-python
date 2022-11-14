fruit, price_product, weight_product, amount_user = [
    input() for _ in range(4)
]

weight_price_total = int(weight_product) * int(price_product)
price = f'{weight_product}кг * {price_product}руб/кг'
total = f'{weight_price_total}руб'
entered = f'{amount_user}руб'
delivery = f'{int(amount_user) - weight_price_total}руб'

a = ' ' * (35 - len(fruit + 'Товар:'))
b = ' ' * (35 - len(price + 'Цена:'))
c = ' ' * (35 - len(total + 'Итого:'))
d = ' ' * (35 - len(entered + 'Внесено:'))
e = ' ' * (35 - len(delivery + 'Сдача:'))

print('================Чек================')
print(f'Товар:{a}{fruit}')
print(f'Цена:{b}{price}')
print(f'Итого:{c}{total}')
print(f'Внесено:{d}{entered}')
print(f'Сдача:{e}{delivery}')
print('===================================')
