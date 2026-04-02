import os
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("8713012544:AAFMjZQRr-Mu3OtnvQ0q3nzjKdpzANwLgEo")

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot aktif!")

def run_bot():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    import threading

    # Jalankan bot di thread terpisah
    t = threading.Thread(target=run_bot)
    t.start()

    # Jalankan web server untuk Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
