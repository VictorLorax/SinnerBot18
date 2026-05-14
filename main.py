import telebot
import os
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from apscheduler.schedulers.background import BackgroundScheduler

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
# CHAT IDs
# =========================
CONNECT_CHAT_ID = -1003256157463
REDROOM_CHAT_ID = -1003867191682
TV_CHANNEL_ID = -1002681661405

# =========================
# DAILY NEW MEMBERS STORAGE
# =========================
daily_new_members = []

# =========================
# RANDOM MORNING QUOTES
# =========================
morning_quotes = [

    "🌅 Someone woke up hoping to meet their perfect vibe today 👀",

    "🔥 A new day in Sinner City means new connects and new energy.",

    "🥵 Somebody is already checking the group hoping you text first.",

    "💘 Today might be the day you find your late-night partner.",

    "👀 Don’t just watch silently… your next vibe may be waiting."
]

# =========================
# RANDOM NIGHT QUOTES
# =========================
night_quotes = [

    "🌙 Someone in this group secretly wants a midnight vibe tonight 👀",

    "😈 The night is young… and somebody wants attention badly.",

    "🔥 Late-night conversations hit differently in Sinner City.",

    "🥵 Someone is scrolling quietly hoping for a naughty DM.",

    "💘 The bold ones usually get the best connects."
]

# =========================
# RANDOM TRUTH QUESTIONS
# =========================
truth_questions = [

    "😈 What’s your wildest late-night thought?",

    "🔥 Have you ever had a secret crush inside a group?",

    "👀 What’s something risky you’ve never admitted before?",

    "💘 What instantly catches your attention during chats?",

    "🥵 Have you ever texted someone something bold at midnight?"
]

# =========================
# RANDOM DARE QUESTIONS
# =========================
dare_questions = [

    "🔥 Reply to someone using only emojis for 2 minutes.",

    "😈 Change your profile emoji for 10 minutes.",

    "👀 Compliment a random member publicly.",

    "🥵 Send a funny GIF in the chat.",

    "💘 DM someone in the group and say hi."
]

# =========================
# REACTION BUTTONS
# =========================
def reaction_buttons():

    markup = InlineKeyboardMarkup()

    markup.row(
        InlineKeyboardButton("🔥", callback_data="fire"),
        InlineKeyboardButton("🥵", callback_data="hot"),
        InlineKeyboardButton("💘", callback_data="love")
    )

    return markup

# =========================
# STORE NEW MEMBERS
# =========================
@bot.message_handler(content_types=['new_chat_members'])
def collect_new_members(message):

    for user in message.new_chat_members:

        username = user.username

        if username:
            daily_new_members.append(f"@{username}")
        else:
            daily_new_members.append(user.first_name)

# =========================
# DAILY SHOUTOUT SYSTEM
# =========================
def daily_welcome_post():

    if not daily_new_members:
        return

    members_text = "\n".join(daily_new_members)

    message_text = f"""
🔥 DAILY SINNER CITY WELCOME 🔥

Welcome our new sinners today 👀

{members_text}

✅ Engage with admin posts daily
✅ Reactions & activity give XP
✅ Level up inside Sinner City
✅ Join all official spaces below 👇
"""

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
            "📜 GROUP RULES",
            callback_data="show_rules"
        )
    )

    bot.send_message(
        CONNECT_CHAT_ID,
        message_text,
        reply_markup=markup
    )

    bot.send_message(
        REDROOM_CHAT_ID,
        message_text,
        reply_markup=markup
    )

    daily_new_members.clear()

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
            "📜 GROUP RULES",
            callback_data="show_rules"
        )
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
8. XP is earned through engagement.
9. Join all official Sinner City spaces.
""",
        reply_markup=reaction_buttons()
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

    quote = random.choice(morning_quotes)

    bot.send_message(
        message.chat.id,
        f"""
{quote}

Need a connect?
Use:
/adminconnect
""",
        reply_markup=reaction_buttons()
    )

# =========================
# NIGHT MESSAGE
# =========================
@bot.message_handler(commands=['naughtygoodnightaiquote'])
def night(message):

    quote = random.choice(night_quotes)

    bot.send_message(
        message.chat.id,
        f"""
{quote}

Ready to find your vibe?

Use:
/adminconnect
""",
        reply_markup=reaction_buttons()
    )

# =========================
# NAUGHTY TRUTH
# =========================
@bot.message_handler(commands=['naughtytruth'])
def truth(message):

    question = random.choice(truth_questions)

    bot.send_message(
        message.chat.id,
        question,
        reply_markup=reaction_buttons()
    )

# =========================
# EXTREME DARE
# =========================
@bot.message_handler(commands=['extremedare'])
def dare(message):

    question = random.choice(dare_questions)

    bot.send_message(
        message.chat.id,
        question,
        reply_markup=reaction_buttons()
    )

# =========================
# GET CHAT ID
# =========================
@bot.message_handler(commands=['id'])
def get_id(message):

    bot.reply_to(
        message,
        f"🆔 Chat ID: {message.chat.id}"
    )

# =========================
# POST TO CONNECT GROUP
# =========================
@bot.message_handler(commands=['postconnectgroup'])
def post_connect(message):

    text = message.text.replace('/postconnectgroup', '').strip()

    if not text:
        bot.reply_to(message, "⚠️ Type a message.")
        return

    bot.send_message(
        CONNECT_CHAT_ID,
        f"📢 {text}",
        reply_markup=reaction_buttons()
    )

    bot.reply_to(message, "✅ Posted to Connect Group.")

# =========================
# POST TO RED ROOM
# =========================
@bot.message_handler(commands=['postredroom'])
def post_redroom(message):

    text = message.text.replace('/postredroom', '').strip()

    if not text:
        bot.reply_to(message, "⚠️ Type a message.")
        return

    bot.send_message(
        REDROOM_CHAT_ID,
        f"📢 {text}",
        reply_markup=reaction_buttons()
    )

    bot.reply_to(message, "✅ Posted to Red Room.")

# =========================
# POST TO TV CHANNEL
# =========================
@bot.message_handler(commands=['posttv'])
def post_tv(message):

    text = message.text.replace('/posttv', '').strip()

    if not text:
        bot.reply_to(message, "⚠️ Type a message.")
        return

    bot.send_message(
        TV_CHANNEL_ID,
        f"📢 {text}",
        reply_markup=reaction_buttons()
    )

    bot.reply_to(message, "✅ Posted to TV Channel.")

# =========================
# POST EVERYWHERE
# =========================
@bot.message_handler(commands=['postall'])
def post_all(message):

    text = message.text.replace('/postall', '').strip()

    if not text:
        bot.reply_to(message, "⚠️ Type a message.")
        return

    bot.send_message(
        CONNECT_CHAT_ID,
        f"📢 {text}",
        reply_markup=reaction_buttons()
    )

    bot.send_message(
        REDROOM_CHAT_ID,
        f"📢 {text}",
        reply_markup=reaction_buttons()
    )

    bot.send_message(
        TV_CHANNEL_ID,
        f"📢 {text}",
        reply_markup=reaction_buttons()
    )

    bot.reply_to(message, "✅ Posted everywhere.")

# =========================
# BUTTON CALLBACKS
# =========================
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    if call.data == "show_rules":

        bot.send_message(
            call.message.chat.id,
            """
🔥 SINNER CITY RULES 🔥

1. Respect all members.
2. No spam.
3. Verification is ONLY for ladies.
4. Guys use connect commands/admin connect.
5. React to at least 5 admin posts weekly.
6. Ghost members may be removed.
7. No leaking private connects.
8. XP is earned through engagement.
9. Join all official Sinner City spaces.
"""
        )

    else:

        bot.answer_callback_query(
            call.id,
            "🔥 Reaction received!"
        )

# =========================
# DAILY AUTOMATIC TIMER
# =========================
scheduler = BackgroundScheduler()

scheduler.add_job(
    daily_welcome_post,
    'cron',
    hour=23,
    minute=0
)

scheduler.start()

# =========================
# BOT RUN
# =========================
bot.infinity_polling()