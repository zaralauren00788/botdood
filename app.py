import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN belum diset di Render Environment Variables!")

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot aktif dan berjalan!")

def run_bot():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    # Jalankan bot di thread terpisah
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # Jalankan Flask di port Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
