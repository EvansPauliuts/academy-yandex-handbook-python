name_val = [input() for _ in range(4)]
name_product, money, weight, account_money = name_val

print('Чек')
print(f'{name_product} - {weight}кг - {money}руб/кг')

product_money_weight_total = int(money) * int(weight)
account_product_total = int(account_money) - product_money_weight_total

print(f'Итого: {product_money_weight_total}руб')
print(f'Внесено: {account_money}руб')
print(f'Сдача: {account_product_total}руб')
