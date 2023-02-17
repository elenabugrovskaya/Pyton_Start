from aiogram import Bot, Dispatcher
data = open('bot/token.txt', 'r')
tok = str(data.read())
bot=Bot(tok)
dp=Dispatcher(bot)