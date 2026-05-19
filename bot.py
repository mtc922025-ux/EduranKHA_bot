import telebot
import google.generativeai as genai

# আপনার টেলিগ্রাম বট টোকেন ও জেমিনি API Key এখানে সম্পূর্ণ সেট করা আছে
BOT_TOKEN = "8639735579:AAE1fpiS7QGcUbBO1G1uZm_eD4p-oBaGJQE"
GEMINI_KEY = "AIzaSyCVflDL9Jr5zzpEkY-oHCu-yJ5LsV0v420"

genai.configure(api_key=GEMINI_KEY)
bot = telebot.TeleBot(BOT_TOKEN)
model = genai.GenerativeModel('gemini-1.5-flash')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = "হ্যালো! আমি Eduran AI Bot। আমাকে যেকোনো প্রশ্ন করতে পারেন, আমি উত্তর দেওয়ার চেষ্টা করব! 🤖"
    bot.reply_to(message, welcome_text)

@bot.message_handler(func=lambda message: True)
def reply_to_user(message):
    try:
        user_input = message.text
        response = model.generate_content(user_input)
        ai_reply = response.text
        bot.reply_to(message, ai_reply)
    except Exception as e:
        bot.reply_to(message, "দুঃখিত, একটু সমস্যা হয়েছে। দয়া করে আবার চেষ্টা করুন।")
        print(f"Error: {e}")

print("বট সফলভাবে চালু হয়েছে...")
bot.infinity_polling()
