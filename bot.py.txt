import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

# ===== BOT SETTINGS (token from env for security) =====
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("Please set the BOT_TOKEN environment variable in your deployment environment.")
CHANNEL_LINK = "https://t.me/+gwpx1n_VBZJmNzC0"
GROUP_LINK = "https://t.me/+jcVnkwMDVk"
ADMIN_LINK = "https://t.me/Mon3yMoTime"
# ======================================================

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = (user.first_name or user.username or "there").upper()

    text = (
        f"*{name}, JOIN UP QUICK â STAY PLUGGED IN FOR EVERYDAY FRESH FULLZ & CRYPTO LEADS UPDATE!* ðªð¥\n\n"
        "ð¥ *FORWARD THIS MSG TO 15+ CONTACTS & GROUP CHATS, YOUR SUPPORT MEANS A LOT!* ð\n\n"
        "ð *PM @Mon3yMoTime FOR FREE LIST â DONâT SLEEP ON IT. LETâS GET IT BUZZING!* ð¼ð¹"
    )

    # Vertical keyboard layout (one button per row)
    keyboard = [
        [InlineKeyboardButton("ð¬ CONTACT MO", url=ADMIN_LINK)],
        [InlineKeyboardButton("ð¢ JOIN CHANNEL", url=CHANNEL_LINK)],
        [InlineKeyboardButton("ð¬ JOIN GROUP CHAT", url=GROUP_LINK)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    message_obj = update.message or update.effective_message
    if message_obj is None:
        logger.info("Start called but no message object to reply to.")
        return

    try:
        await message_obj.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    except Exception:
        logger.exception("Failed to send /start reply (error swallowed).")

# Optional: handle callback queries
async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if not query:
        return
    await query.answer()
    await query.edit_message_text("Action received. Thanks!")

# Debug handler to log every update
async def debug_update_logger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("DEBUG update received: %s", update)

# Global error handler
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.exception("Exception while handling update: %s", context.error)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.ALL, debug_update_logger))
    app.add_error_handler(error_handler)

    logger.info("Starting bot polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
