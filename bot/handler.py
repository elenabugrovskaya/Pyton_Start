from loader_bot import dp, bot
from aiogram import types
from random import randint as RD
import all_user


@dp.message_handler(commands=["start"])
async def message_start(message: types.Message):
    print(message)
    await message.answer(f"Привет, {message.from_user.first_name}, рад тебя видеть!!!")
    await message.answer(f"{message.from_user.first_name}, для запуска игры воспользуйся командой /new_game")

number = 0
step = 0
rand = True


@dp.message_handler(commands=["new_game"])
async def message_start(message: types.Message):
    global number
    global step
    global rand
    user = [message.from_user.id, message.from_user.first_name, True, number]
    if len(all_user.users)!=0:
        for i in all_user.users:
            if user[0] == i[0]:
                await message.answer(f'{message.from_user.first_name}, у  вас есть незаконченная игра')
            else:   
                await message.answer(f'{message.from_user.first_name}, давай поиграем в игру "Конфеты", вот правила: на столе лежит N колчесвто конфет,\
которое можно задать следующим сообщением, или же оно будет задано рандомно от 100 до 200, если ввести 0, первый ход выбирается жеребьевкой, за один ход\
можно брать от 1 до 28 конфет включительно, выигрывает тот кто ходит последним')
                user = [message.from_user.id, message.from_user.first_name, True, number]
                all_user.users.append(user)
    else:
        await message.answer(f'{message.from_user.first_name}, давай поиграем в игру "Конфеты", вот правила: на столе лежит N колчесвто конфет,\
которое можно задать следующим сообщением, или же оно будет задано рандомно от 100 до 200, если ввести 0, первый ход выбирается жеребьевкой, за один ход\
можно брать от 1 до 28 конфет включительно, выигрывает тот кто ходит последним')
        user = [message.from_user.id, message.from_user.first_name, True, number]
        all_user.users.append(user)
    # if user[2] == False:
    #     number = RD(100, 201)
    #     print(all_user.users)
    #     await bot.send_message(message.from_user.id, f"На столе лежит {number} конфет")
    #     if RD(0, 2) == 0:
    #         step = f"{message.from_user.first_name}"
    #         await bot.send_message(message.from_user.id, f"Жеребьевка дает право ходить {message.from_user.first_name} первым")
    #     else:
    #         step = "Я"
    #         await bot.send_message(message.from_user.id, f"Жеребьевка дает право ходить мне первым")
    #         bot_play = number % 29
    #         await bot.send_message(message.from_user.id, f"А я возьму {bot_play} конфет)))")
    #         number -= bot_play
    #         await bot.send_message(message.from_user.id, f"Конфет стало меньше - {number}")
        # async def user_value(message:types.Message):
        #     global number

        #     count=message.text.split()[1]
        #     number=int(count)
        #     await message.answer(f"Было задано новое количество конфет: {number}")
        #     await bot.send_message(message.from_user.id, f"Теперь на столе лежит {number} конфет")


# @dp.message_handler()
# async def message_game(message:types.Message):
#     for user in all_user.users:
#         if message.from_user.id == user[0]:
#             if user[2]==True:
#                 if message.text.isdigit():
#                     user[3]=int(message.text)
#                     print(all_user.users)
#                 else:
#                     await bot.delete_message(message.from_user.id, message.message_id)
#                     await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, так не пойдет, нужно ввести целое число)))")
#                 user[2]=False


@dp.message_handler()
async def message_game(message: types.Message):
    for user in all_user.users:
        if message.from_user.id == user[0]:
            if user[2] == True:
                if message.text.isdigit() and int(message.text)==0:
                    user[3]=RD(100, 200)
                    await bot.send_message(message.from_user.id, f"На столе лежит {user[3]} конфет")
                    if RD(0, 2) == 0:
                        step = f"{message.from_user.first_name}"
                        await bot.send_message(message.from_user.id, f"Жеребьевка дает право ходить {message.from_user.first_name} первым")
                    else:
                        step = "Я"
                        await bot.send_message(message.from_user.id, f"Жеребьевка дает право ходить мне первым")
                        bot_play = user[3] % 29
                        await bot.send_message(message.from_user.id, f"А я возьму {bot_play} конфет)))")
                        user[3] -= bot_play
                        await bot.send_message(message.from_user.id, f"Конфет стало меньше - {user[3]}")
                    print(all_user.users)
                    user[2]=False
                elif message.text.isdigit() and int(message.text)>29:
                    user[3]=int(message.text)
                    await bot.send_message(message.from_user.id, f"На столе лежит {user[3]} конфет")
                    if RD(0, 2) == 0:
                        step = f"{message.from_user.first_name}"
                        await bot.send_message(message.from_user.id, f"Жеребьевка дает право ходить {message.from_user.first_name} первым")
                    else:
                        step = "Я"
                        await bot.send_message(message.from_user.id, f"Жеребьевка дает право ходить мне первым")
                        bot_play = user[3] % 29
                        await bot.send_message(message.from_user.id, f"А я возьму {bot_play} конфет)))")
                        user[3] -= bot_play
                        await bot.send_message(message.from_user.id, f"Конфет стало меньше - {user[3]}")
                    user[2]=False
                else:
                    await bot.delete_message(message.from_user.id, message.message_id)
                    await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, так не пойдет, нужно ввести целое число , больше 29)))")
                
            else:
                if message.text.isdigit():
                    play=int(message.text)
                    step=f"{message.from_user.first_name}"
                    if play in range(1,29):
                        user[3]-=play
                        if user[3]==0:
                            await bot.send_message(message.from_user.id, f"{step} выиграл эту партию!!!")
                            all_user.users.remove(user)
                            break
                        await bot.send_message(message.from_user.id, f"{message.from_user.first_name} взял {play} конфет, на столе осталось {user[3]} конфет")
                        if user[3]%29!=0:
                            bot_play=user[3]%29
                            step="Я"
                            await bot.send_message(message.from_user.id, f"А я возьму {bot_play} конфет)))")
                            user[3]-=bot_play
                            await bot.send_message(message.from_user.id, f"Конфет стало меньше - {user[3]}")
                            if user[3]==0:
                                await bot.send_message(message.from_user.id, f"{step} выиграл эту партию!!!")
                                all_user.users.remove(user)
                                break
                        elif user[3]%29==0:
                            bot_play=RD(1,28)
                            await bot.send_message(message.from_user.id, f"А я возьму {bot_play} конфет)))")
                            user[3]-=bot_play
                            await bot.send_message(message.from_user.id, f"Конфет стало меньше - {user[3]}")
                    else:
                        await bot.delete_message(message.from_user.id, message.message_id)
                        await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, так не пойдет, нужно ввести целое число от 1 до 28 включительно)))") 
                else:
                    await bot.delete_message(message.from_user.id, message.message_id)
                    await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, так не пойдет, нужно ввести целое число)))")
                if user[3]==0:
                    user[3]=RD(100,201)
                    await bot.send_message(message.from_user.id, f"Теперь на столе лежит {user[3]} конфет")
                    if RD(0,2)==0:
                        step=f"{message.from_user.first_name}"
                        await bot.send_message(message.from_user.id, f"Жеребьевка дает право ходить {message.from_user.first_name} первым")
                    else:
                        step="Я"
                        await bot.send_message(message.from_user.id, f"Жеребьевка дает право ходить мне первым")
                        bot_play=user[3]%29
                        await bot.send_message(message.from_user.id, f"А я возьму {bot_play} конфет)))")
                        user[3]-=bot_play
                        await bot.send_message(message.from_user.id, f"Конфет стало меньше - {user[3]}")
    print(all_user.users)

@dp.message_handler(commands=["weather"])
async def message_weather(message:types.Message):
    await message.answer("Сейчас посмотрим...")

@dp.message_handler(text=["фига себе"])
async def message_cenz(message:types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer("Я тоже удивлен)))")
# @dp.message_handler()
# async def message_weather(message:types.Message):
#     await message.answer(f'Это ты написал: "{message.text}" ???')