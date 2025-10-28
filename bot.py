import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get your bot token from Render environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not set in environment!")

# --- LINKS ---
ADMIN_LINK = "https://t.me/Mon3yMoTime"
CHANNEL_LINK = "https://t.me/+gwpx1n_VBZJmNzc0"
GROUP_LINK = "https://t.me/+CjcVnktCaC8wMDVk"

# --- /start command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or user.username or "Friend"

    text = (
        f"*{name.upper()}, JOIN UP QUICK!* 🏪🥇\n\n"
        "🔥 *FORWARD THIS MSG TO 15+ CONTACTS & GROUPS — SUPPORT MEANS A LOT!* 👏\n\n"
        "💎 *PM @Mon3yMoTime FOR FREE FULLZ – DON’T SLEEP ON IT!* 💼📹"
    )

    keyboard = [
        [InlineKeyboardButton("💬 CONTACT MO", url=ADMIN_LINK)],
        [InlineKeyboardButton("📢 JOIN CHANNEL", url=CHANNEL_LINK)],
        [InlineKeyboardButton("💬 JOIN GROUP CHAT", url=GROUP_LINK)],
    ]

    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

# --- MAIN ---
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
