import random
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, ConversationHandler
from telegram import ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from config import BOT_TOKEN


# Your Telegram Bot Token
API = BOT_TOKEN

# States for conversation handler
CHOOSING, TRANSLATING = range(2)

# Diplomatic Tips (mock list)
TIPS = [
    "Do not comment on their glowing eyes—it's a sensitive topic. 👀❌",
    "Don't touch glowing buttons, unless you enjoy space roulette. 🔴🟢🎲",
    "Avoid talking about Earth's politics—it confuses them. 🌍🤔🚫",
    "Compliment their spaceship's design—it builds goodwill. 🚀✨👍"
]


# Command: Start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    menu_text = (
        "Welcome to the **Hackathon Alien Project!** 🚀👽\n\n"
        "Choose an option by entering the corresponding number:\n\n"
        "1️⃣ Start 🛸\n"
        "2️⃣ Diplomatic Tips 🌌\n"
        "3️⃣ UFO Data 🛸\n"
        "4️⃣ Klingon Translator 🖖\n"
        "5️⃣ ISS Info 🚀\n"
        "6️⃣ Exit ❌"
    )

    await update.message.reply_text(menu_text)


# Handle numeric responses for the menu
async def handle_numeric_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text

    if text == "1":
        await start(update, context)
        return CHOOSING
    elif text == "2":
        await diplomatic_tips(update, context)
        return CHOOSING
    elif text == "3":
        await ufo_data(update, context)
        return CHOOSING
    elif text == "4":
        # Prompt for Klingon translation
        await update.message.reply_text("Enter text to translate into Klingon:")
        return TRANSLATING
    elif text == "5":
        await iss_info(update, context)
        return CHOOSING
    elif text == "6":
        await exit_bot(update, context)
        return CHOOSING
    else:
        await update.message.reply_text("Please choose a valid option by number (1-5).")
        return CHOOSING


# Handle Klingon translation
async def klingon_translation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_input = update.message.text
    translated = user_input[::-1]  # Mock translation (reverse text for fun)
    await update.message.reply_text(f"Klingon Translation:\n{translated}")

    # After translation, show the main menu again
    await start(update, context)
    return CHOOSING


# Command: Diplomatic Tips
async def diplomatic_tips(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tip = random.choice(TIPS)
    await update.message.reply_text(f"Diplomatic Tip:\n{tip}")


# Command: UFO Data
async def ufo_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Mock data since no specific UFO API was mentioned
    mock_data = [
        "Location: Nevada, USA - Date: 2025-01-20 - Description: Bright light moving erratically.",
        "Location: Siberia, Russia - Date: 2025-01-21 - Description: Disk-shaped object hovering for 10 minutes."
    ]
    ufo_info = random.choice(mock_data)
    await update.message.reply_text(f"UFO Sighting:\n{ufo_info}")


# Command: ISS Information
async def iss_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        data = response.json()
        position = data['iss_position']
        await update.message.reply_text(
            f"The ISS is currently at:\nLatitude: {position['latitude']}, Longitude: {position['longitude']}"
        )
    except Exception as e:
        await update.message.reply_text("Error fetching ISS data. Please try again later.")


# Command: Exit
async def exit_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Thank you for using the Alien Project Bot. Goodbye!")


# Conversation handler for Klingon Translator
conversation_handler = ConversationHandler(
    entry_points=[MessageHandler(filters.TEXT & ~filters.COMMAND, handle_numeric_choice)],
    states={
        CHOOSING: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_numeric_choice)],
        TRANSLATING: [MessageHandler(filters.TEXT & ~filters.COMMAND, klingon_translation)],
    },
    fallbacks=[CommandHandler('start', start)],
)


# Main function to set up the bot
def main():
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers for commands
    application.add_handler(conversation_handler)

    # Start the bot
    application.run_polling()


if __name__ == "__main__":
    main()
