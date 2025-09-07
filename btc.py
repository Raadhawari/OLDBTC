import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your actual bot token
TOKEN = "8181040630:AAF4r-ECUHJOgg6VpClcncq9jQrH1spS1us"
DOMAIN_LINK = "https://t.me/bitcmiin_bot?startapp"  # Replace with your actual domain

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.from_user.first_name  # Get user's first name
    welcome_text = f"""
👋 مرحباً {first_name}!

🚀 بوت تعدين البيتكوين الأول من نوعه!

💰 اربح أكثر من 2000$ يومياً من خلال نظام التعدين المتطور  
⏱️ يعمل تلقائياً بدون مجهود منك - 24 ساعة يومياً  
💎 تقنية تعدين سحابية متطورة بأعلى سرعة وكفاءة  
✅ سحب فوري للأرباح عبر محفظتك الخاصة  

⚡ اضغط على الزر أدناه لبدء الربح الآن!
    """

    # Create a button that opens the mining website
    keyboard = InlineKeyboardMarkup()
    mining_button = InlineKeyboardButton("💰 ابدأ التعدين الآن", url=DOMAIN_LINK)
    keyboard.add(mining_button)

    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)

# Keep the bot running
print("Bot is running...")
bot.infinity_polling()
