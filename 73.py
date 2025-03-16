import random
import time 

print('Привет. Это игра "Камень, ножницы, бумага".')
time.sleep(2)
print('Игра закончится, когда у одного из пользователей будет три очка.')
time.sleep(3)

user_score = 0
bot_score = 0
game = 1
bot_list = ['камень', 'ножницы', 'бумага']

while user_score != 3 and bot_score != 3:
    print(f'Раунд {game}')
    game += 1
    user_choice = input('Выбери: камень, ножницы или бумага: ').lower()
    bot_choice = random.choice(bot_list)
    print(f'Выбор пользователя: {user_choice}')
    print(f'Выбор бота: {bot_choice}')

    if user_choice == bot_choice:
        print('Ничья')
    elif user_choice == 'камень' and bot_choice == 'ножницы' or user_choice == 'бумага' and bot_choice == 'камень' or \
                             user_choice == 'ножницы' and bot_choice == 'бумага':
        print('Победил игрок')
        user_score += 1
    elif user_choice == 'камень' and bot_choice == 'бумага' or user_choice == 'бумага' and bot_choice == 'ножницы' or \
                             user_choice == 'ножницы' and bot_choice == 'камень':
        print('Бот выйграл')
        bot_score += 1
    else:
        print('Ошибка ввода')

    print(f'Текущий счет: бот: {bot_score} / игрок: {user_score}')

if bot_score > user_score:
    print('Бот выйграл!')
else:
    print('Ты выйграл!')
