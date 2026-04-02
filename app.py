import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ambil token dari Environment Variable
BOT_TOKEN = os.getenv("8713012544:AAFMjZQRr-Mu3OtnvQ0q3nzjKdpzANwLgEo")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing! Set it in Render Environment Variables.")

# Flask app untuk Render
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

# Command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot aktif dan berjalan di Render!")

# Jalankan bot polling
def run_bot():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

# Main
if __name__ == "__main__":
    # Jalankan bot di thread terpisah
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # Jalankan Flask server untuk Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
