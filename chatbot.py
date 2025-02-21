import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# API kalitlaringiz
GEMINI_API_KEY = "AIzaSyBJC2yh0fqxb0q69lU2MJEM0pPIsG0Bi04"  # Google Gemini API kalitingizni kiriting
TELEGRAM_BOT_TOKEN = "8158760101:AAGUGo2w8jF3iqTONgH_VXL2Sy1zYzi1pzk"  # Telegram bot tokenini kiriting

# Gemini API ni sozlash
genai.configure(api_key=GEMINI_API_KEY)

# AI bilan suhbat funksiyasi
def chat_with_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")  # yoki "gemini-1.5-pro" / "gemini-1.5-flash"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Xatolik: {str(e)}"

# /start komandasi
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Assalomu alaykum! Men AI chatbotman. Savollaringizni yozing.")

# Foydalanuvchi xabarlari uchun handler
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text
    response = chat_with_gemini(user_text)
    await update.message.reply_text(response)

# Botni ishga tushirish
def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))  # /start komandasi
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Xabarlarni qayta ishlash

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
