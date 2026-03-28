import telebot
import requests
from telebot import types

# BotFather bergan token
TOKEN = '8606825506:AAE8vv8NAb8QNWd6gJpa0kkmN9VEmtvSjdA'

bot = telebot.TeleBot(TOKEN)

def get_rates():
    try:
        url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
        return requests.get(url, timeout=10).json()
    except: return None

@bot.message_handler(commands=['start'])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📊 Kurslar")
    # Bot ishga tushganda sizga ID raqamingizni o'zi aytadi
    bot.send_message(m.chat.id, f"Salom! Bot ishga tushdi. 🚀\nSizning ID raqamingiz: {m.chat.id}", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "📊 Kurslar")
def show_rates(m):
    data = get_rates()
    if data:
        usd = next(i for i in data if i['Ccy'] == 'USD')
        bot.send_message(m.chat.id, f"🇺🇸 1 USD = {usd['Rate']} so'm")

if __name__ == "__main__":
    bot.infinity_polling()
