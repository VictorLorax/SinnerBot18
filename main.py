import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# =========================
# ADMIN USERNAME
# =========================
ADMIN_USERNAME = "https://t.me/SinnerKing"

# =========================
# GROUP & CHANNEL LINKS
# =========================
CONNECT_GROUP = "https://t.me/+IsnkwS7RZRU3YTNk"
REDROOM_GROUP = "https://t.me/+Cb1uEABDl34xZmE8"
TV_CHANNEL_LINK = "https://t.me/SINNERTV"

# =========================
# START COMMAND
# =========================
@bot.message_handler(commands=['start'])
def start(message):

    markup = InlineKeyboardMarkup(row_width=1)

    markup.add(
        InlineKeyboardButton("💘 Join Connect Group", url=CONNECT_GROUP)
    )

    markup.add(
        InlineKeyboardButton("🌶️ Join Red Room", url=REDROOM_GROUP)
    )

    markup.add(
        InlineKeyboardButton("📺 Join TV Channel", url=TV_CHANNEL_LINK)
    )

    markup.add(
        InlineKeyboardButton(
            "💘 Contact Admin",
            url=f"https://t.me/{ADMIN_USERNAME}"
        )
    )

    bot.send_message(
        message.chat.id,
        """
🔥 WELCOME TO SINNER CITY 🔥

To enjoy the FULL Sinner City experience,
join ALL platforms below 👇

💘 Connect Group
🌶️ Red Room
📺 TV Channel

⚠️ Members who stay inactive or fail to engage may be removed.

Need a private connect?
Use the admin button below 👇
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
2. No spam or scams.
3. Verification is ONLY for ladies.
4. Guys should use connect commands/admin connect.
5. React to at least 5 admin posts weekly.
6. Ghost/inactive users may be removed.
7. No leaking private chats or connects.
8. Red Room is strictly 18+.
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
            "💘 CONTACT ADMIN",
            url=f"https://t.me/{ADMIN_USERNAME}"
        )
    )

    bot.send_message(
        message.chat.id,
        """
💘 READY FOR A CONNECT?

Admin helps with:

• FWB Connects
• Serious Relationships
• Verified Ladies
• Premium Connects

Click below 👇
""",
        reply_markup=markup
    )

# =========================
# MORNING AI BROADCAST
# =========================
@bot.message_handler(commands=['morningaibroadcast'])
def morning(message):

    bot.send_message(
        message.chat.id,
        """
🌅 GOOD MORNING SINNERS 👀

Someone woke up hoping to find their perfect match today 💘

Will it be you?

Need a connect?
Use:
/adminconnect
"""
    )

# =========================
# NIGHT AI MESSAGE
# =========================
@bot.message_handler(commands=['naughtygoodnightaiquote'])
def night(message):

    bot.send_message(
        message.chat.id,
        """
🌙 NAUGHTY NIGHT THOUGHT 😈

Somebody in this community is secretly hoping for a late-night vibe tonight 👀

Ready to find your match?

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
😈 NAUGHTY TRUTH

What’s the boldest thing you’ve ever texted someone at midnight? 👀
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
🔥 EXTREME DARE

Reply to someone in the group using only emojis for 5 minutes 👀
"""
    )

# =========================
# BROADCAST
# =========================
@bot.message_handler(commands=['broadcast'])
def broadcast(message):

    if str(message.from_user.username) != ADMIN_USERNAME:
        return

    bot.reply_to(
        message,
        "📢 Broadcast system coming soon."
    )

# =========================
# BOT RUN
# =========================
bot.infinity_polling()