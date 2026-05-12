import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# =========================
# ADMIN USERNAME
# =========================
ADMIN_USERNAME = "@SinnerKing"

# =========================
# GROUP & CHANNEL LINKS
# =========================
CONNECT_GROUP = "https://t.me/+IsnkwS7RZRU3YTNk"
REDROOM_GROUP = "https://t.me/+Cb1uEABDl34xZmE8"
TV_CHANNEL = "https://t.me/SINNERTV"

# =========================
# AUTO WELCOME MESSAGE
# =========================
@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton("🔞 Connect Group", url=CONNECT_GROUP)
    )

    markup.add(
        InlineKeyboardButton("🥵💦 Red Room", url=REDROOM_GROUP)
    )

    markup.add(
        InlineKeyboardButton("📺 TV Channel", url=TV_CHANNEL)
    )

    for user in message.new_chat_members:

        bot.send_message(
            message.chat.id,
            f"""
🔥 Welcome {user.first_name} to Sinner City 🔥

To enjoy the FULL Sinner City experience 👀

✅ Join all Sinner City platforms below
✅ Then send /start to activate your experience

⚠️ Members who fail to engage may be removed.
""",
            reply_markup=markup
        )

# =========================
# START COMMAND
# =========================
@bot.message_handler(commands=['start'])
def start(message):

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton("🔞 Connect Group", url=CONNECT_GROUP)
    )

    markup.add(
        InlineKeyboardButton("🥵💦 Red Room", url=REDROOM_GROUP)
    )

    markup.add(
        InlineKeyboardButton("📺 TV Channel", url=TV_CHANNEL)
    )

    markup.add(
        InlineKeyboardButton(
            "🔞 CONTACT ADMIN",
            url=f"https://t.me/{ADMIN_USERNAME}"
        )
    )

    bot.send_message(
        message.chat.id,
        """
🔥 Welcome to Sinner City 🔥

Choose where you want to enter 👇
""",
        reply_markup=markup
    )

# =========================
# RULES COMMAND
# =========================
@bot.message_handler(commands=['rules'])
def rules(message):

    bot.send_message(
        message.chat.id,
        """
🔥 SINNER CITY RULES 🔥

1. Respect all members.
2. No spam.
3. Verification is ONLY for ladies.
4. Guys use connect commands/admin connect.
5. React to at least 5 admin posts weekly.
6. Ghost members may be removed.
7. No leaking private connects.
"""
    )

# =========================
# ADMIN CONNECT
# =========================
@bot.message_handler(commands=['adminconnect'])
def adminconnect(message):

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(
            "🔞 CONTACT ADMIN",
            url=f"https://t.me/{ADMIN_USERNAME}"
        )
    )

    bot.send_message(
        message.chat.id,
        """
🔞 Ready for a connect?

Admin helps with:
• FWB connects
• Serious relationships
• Verified ladies

Click below 👇
""",
        reply_markup=markup
    )

# =========================
# MORNING MESSAGE
# =========================
@bot.message_handler(commands=['morningaibroadcast'])
def morning(message):

    bot.send_message(
        message.chat.id,
        """
🌅 Good Morning Sinners 👀

Someone woke up hoping to find their perfect match to turn up the heat today 🥵🔞

Need a connect?
Use:
/adminconnect
"""
    )

# =========================
# NIGHT MESSAGE
# =========================
@bot.message_handler(commands=['naughtygoodnightaiquote'])
def night(message):

    bot.send_message(
        message.chat.id,
        """
🌙 Naughty Night Thought 😈

Someone in this group is secretly hoping you can make her wet and can you cum💦 this night!

Ready to find your vibe?

Use:
/adminconnect
"""
    )

# =========================
# NAUGHTY TRUTH
# =========================
@bot.message_handler(commands=['naughtytruth'])
def truth(message):

    bot.send_message(
        message.chat.id,
        """
😈 Naughty Truth:

If you were to send your naughtiest video on your phone would you, if yes, then show us!
"""
    )

# =========================
# EXTREME DARE
# =========================
@bot.message_handler(commands=['extremedare'])
def dare(message):

    bot.send_message(
        message.chat.id,
        """
🔥 Extreme Dare:

Reply to someone in the group using only emojis of your fav styles for 2 minutes 👀
"""
    )

# =========================
# BOT RUN
# =========================
bot.infinity_polling()