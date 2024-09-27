from telegram.ext import Application, CommandHandler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import Update
import pytz
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the bot token and chat ID from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Function to send "Good morning." message
async def scheduled_morning_message():
    application = Application.builder().token(BOT_TOKEN).build()
    await application.bot.send_message(chat_id=CHAT_ID, text="Good morning.")

# Command handler for /chatid
async def chatid(update: Update, context):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"Chat ID: {chat_id}")

def main():
    # Create the application and pass your bot's token
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handler for /chatid
    application.add_handler(CommandHandler("chatid", chatid))

    # Set up the asyncio scheduler
    scheduler = AsyncIOScheduler(timezone=pytz.timezone('America/New_York'))

    # Schedule the morning message at 7 AM
    scheduler.add_job(scheduled_morning_message, 'cron', hour=7, minute=0)

    scheduler.start()

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
