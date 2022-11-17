name, mood = [input() for _ in range(2)]

print('Как Вас зовут?')
print(f'Здравствуйте, {name}!')
print('Как дела?')
print('Я за вас рада!' if mood == 'хорошо' else 'Всё наладится!')
