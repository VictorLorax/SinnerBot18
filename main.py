import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

ADMIN_USERNAME = "YOUR_USERNAME"

CONNECT_GROUP = "https://t.me/yourconnectgroup"
REDROOM_GROUP = "https://t.me/yourredroom"
TV_GROUP = "https://t.me/yourtvgroup"
CHANNEL_LINK = "https://t.me/yourchannel"


# START COMMAND
@bot.message_handler(commands=['start'])
def start(message):

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton("💘 Connect Group", url=CONNECT_GROUP)
    )

    markup.add(
        InlineKeyboardButton("🌶️ Red Room", url=REDROOM_GROUP)
    )

    markup.add(
        InlineKeyboardButton("📺 TV Group", url=TV_GROUP)
    )

    markup.add(
        InlineKeyboardButton("📢 Channel", url=CHANNEL_LINK)
    )

    bot.send_message(
        message.chat.id,
        """
🔥 Welcome to Sinner City 🔥

Choose where you want to enter 👇
""",
        reply_markup=markup
    )


# RULES COMMAND
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


# ADMIN CONNECT
@bot.message_handler(commands=['adminconnect'])
def adminconnect(message):

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(
            "💘 CONTACT ADMIN",
            url=f"https://t.me/{ADMIN_USERNAME}"
        )
    )

    bot.send_message(
        message.chat.id,
        """
💘 Ready for a connect?

Admin helps with:
• FWB connects
• Serious relationships
• Verified ladies

Click below 👇
""",
        reply_markup=markup
    )


# MORNING MESSAGE
@bot.message_handler(commands=['morningaibroadcast'])
def morning(message):

    bot.send_message(
        message.chat.id,
        """
🌅 Good Morning Sinners 👀

Someone woke up hoping to find their perfect match today 💘

Need a connect?
Use:
/adminconnect
"""
    )


# NIGHT MESSAGE
@bot.message_handler(commands=['naughtygoodnightaiquote'])
def night(message):

    bot.send_message(
        message.chat.id,
        """
🌙 Naughty Night Thought 😈

Someone in this group is secretly hoping for a late-night connect 👀

Ready to find your vibe?

Use:
/adminconnect
"""
    )


# NAUGHTY TRUTH
@bot.message_handler(commands=['naughtytruth'])
def truth(message):

    bot.send_message(
        message.chat.id,
        """
😈 Naughty Truth:

What’s the boldest thing you’ve ever texted someone at midnight?
"""
    )


# EXTREME DARE
@bot.message_handler(commands=['extremedare'])
def dare(message):

    bot.send_message(
        message.chat.id,
        """
🔥 Extreme Dare:

Reply to someone in the group using only emojis for 5 minutes 👀
"""
    )


bot.infinity_polling()