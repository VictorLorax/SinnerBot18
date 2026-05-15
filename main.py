import telebot
import os
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from apscheduler.schedulers.background import BackgroundScheduler

# =========================
# BOT TOKEN
# =========================
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
# STORAGE
# =========================
daily_new_members = []
reaction_counts = {}

# =========================
# RANDOM QUOTES
# =========================
morning_quotes = [

    "🌅 Someone woke up hoping to meet their perfect vibe today 👀",
    "🔥 A new day in Sinner City means new connects and new energy.",
    "🥵 Somebody is already checking the group hoping you text first.",
    "💘 Today might be the day you find your late-night partner.",
    "👀 Don’t just watch silently… your next vibe may be waiting."
]

night_quotes = [

    "🌙 Someone in this group secretly wants a midnight vibe tonight 👀",
    "😈 The night is young… and somebody wants attention badly.",
    "🔥 Late-night conversations hit differently in Sinner City.",
    "🥵 Someone is scrolling quietly hoping for a naughty DM.",
    "💘 The bold ones usually get the best connects."
]

truth_questions = [

    "😈 What’s your wildest late-night thought?",
    "🔥 Have you ever had a secret crush inside a group?",
    "👀 What’s something risky you’ve never admitted before?",
    "💘 What instantly catches your attention during chats?",
    "🥵 Have you ever texted someone something bold at midnight?"
]

dare_questions = [

    "🔥 Reply to someone using only emojis for 2 minutes.",
    "😈 Change your profile emoji for 10 minutes.",
    "👀 Compliment a random member publicly.",
    "🥵 Send a funny GIF in the chat.",
    "💘 DM someone in the group and say hi."
]

# =========================
# REACTION BUTTON SYSTEM
# =========================
def reaction_buttons(message_id):

    if message_id not in reaction_counts:

        reaction_counts[message_id] = {
            "fire": 0,
            "hot": 0,
            "love": 0,
            "laugh": 0
        }

    markup = InlineKeyboardMarkup()

    markup.row(

        InlineKeyboardButton(
            f"🔥 {reaction_counts[message_id]['fire']}",
            callback_data=f"fire_{message_id}"
        ),

        InlineKeyboardButton(
            f"🥵 {reaction_counts[message_id]['hot']}",
            callback_data=f"hot_{message_id}"
        ),

        InlineKeyboardButton(
            f"💘 {reaction_counts[message_id]['love']}",
            callback_data=f"love_{message_id}"
        ),

        InlineKeyboardButton(
            f"😂 {reaction_counts[message_id]['laugh']}",
            callback_data=f"laugh_{message_id}"
        )
    )

    return markup

# =========================
# STORE NEW MEMBERS
# =========================
@bot.message_handler(content_types=['new_chat_members'])
def collect_new_members(message):

    for user in message.new_chat_members:

        if user.username:
            daily_new_members.append(f"@{user.username}")

        else:
            daily_new_members.append(user.first_name)

# =========================
# DAILY WELCOME SYSTEM
# =========================
def daily_welcome_post():

    if not daily_new_members:
        return

    members_text = "\n".join(daily_new_members)

    message_text = f"""
🔥 DAILY SINNER CITY WELCOME 🔥

Welcome our new sinners today 👀

{members_text}

━━━━━━━━━━━━━━━

📜 SINNER CITY RULES

1. Respect all members.
2. No spam or unnecessary flooding.
3. Verification is ONLY for ladies.
4. Guys use /adminconnect
5. React to admin posts daily.
6. XP is earned through engagement.
7. Ghost members may be removed.
8. No leaking private connects.
9. Stay active in all official spaces.

━━━━━━━━━━━━━━━

✅ Engage with admin posts daily
✅ Reactions & activity give XP
✅ Level up inside Sinner City
"""

    markup = InlineKeyboardMarkup(row_width=1)

    markup.add(
        InlineKeyboardButton(
            "🔞 Connect Group",
            url=CONNECT_GROUP
        )
    )

    markup.add(
        InlineKeyboardButton(
            "🥵💦 Red Room",
            url=REDROOM_GROUP
        )
    )

    markup.add(
        InlineKeyboardButton(
            "📺 TV Channel",
            url=TV_CHANNEL
        )
    )

    markup.add(
        InlineKeyboardButton(
            "🔞 CONTACT ADMIN",
            url=f"https://t.me/{ADMIN_USERNAME.replace('@','')}"
        )
    )

    sent1 = bot.send_message(
        CONNECT_CHAT_ID,
        message_text,
        reply_markup=markup
    )

    sent2 = bot.send_message(
        REDROOM_CHAT_ID,
        message_text,
        reply_markup=markup
    )

    bot.edit_message_reply_markup(
        CONNECT_CHAT_ID,
        sent1.message_id,
        reply_markup=reaction_buttons(sent1.message_id)
    )

    bot.edit_message_reply_markup(
        REDROOM_CHAT_ID,
        sent2.message_id,
        reply_markup=reaction_buttons(sent2.message_id)
    )

    daily_new_members.clear()

# =========================
# START COMMAND
# =========================
@bot.message_handler(commands=['start'])
def start(message):

    markup = InlineKeyboardMarkup(row_width=1)

    markup.add(
        InlineKeyboardButton(
            "🔞 Connect Group",
            url=CONNECT_GROUP
        )
    )

    markup.add(
        InlineKeyboardButton(
            "🥵💦 Red Room",
            url=REDROOM_GROUP
        )
    )

    markup.add(
        InlineKeyboardButton(
            "📺 TV Channel",
            url=TV_CHANNEL
        )
    )

    markup.add(
        InlineKeyboardButton(
            "🔞 CONTACT ADMIN",
            url=f"https://t.me/{ADMIN_USERNAME.replace('@','')}"
        )
    )

    bot.send_message(
        message.chat.id,
        """
🔥 Welcome To Sinner City 🔥

Choose your destination below 👇
""",
        reply_markup=markup
    )

# =========================
# RULES COMMAND
# =========================
@bot.message_handler(commands=['rules'])
def rules(message):

    sent_msg = bot.send_message(
        message.chat.id,
        """
📜 SINNER CITY RULES

1. Respect all members.
2. No spam or flooding.
3. Verification is ONLY for ladies.
4. Guys use /adminconnect
5. React to admin posts daily.
6. XP is earned through engagement.
7. Ghost members may be removed.
8. No leaking private connects.
9. Stay active in all official spaces.
"""
    )

    bot.edit_message_reply_markup(
        message.chat.id,
        sent_msg.message_id,
        reply_markup=reaction_buttons(sent_msg.message_id)
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
            url=f"https://t.me/{ADMIN_USERNAME.replace('@','')}"
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
""",
        reply_markup=markup
    )

# =========================
# MORNING AI
# =========================
@bot.message_handler(commands=['morningaibroadcast'])
def morning(message):

    quote = random.choice(morning_quotes)

    sent_msg = bot.send_message(
        message.chat.id,
        quote
    )

    bot.edit_message_reply_markup(
        message.chat.id,
        sent_msg.message_id,
        reply_markup=reaction_buttons(sent_msg.message_id)
    )

# =========================
# NIGHT AI
# =========================
@bot.message_handler(commands=['naughtygoodnightaiquote'])
def night(message):

    quote = random.choice(night_quotes)

    sent_msg = bot.send_message(
        message.chat.id,
        quote
    )

    bot.edit_message_reply_markup(
        message.chat.id,
        sent_msg.message_id,
        reply_markup=reaction_buttons(sent_msg.message_id)
    )

# =========================
# TRUTH COMMAND
# =========================
@bot.message_handler(commands=['naughtytruth'])
def truth(message):

    question = random.choice(truth_questions)

    sent_msg = bot.send_message(
        message.chat.id,
        question
    )

    bot.edit_message_reply_markup(
        message.chat.id,
        sent_msg.message_id,
        reply_markup=reaction_buttons(sent_msg.message_id)
    )

# =========================
# DARE COMMAND
# =========================
@bot.message_handler(commands=['extremedare'])
def dare(message):

    question = random.choice(dare_questions)

    sent_msg = bot.send_message(
        message.chat.id,
        question
    )

    bot.edit_message_reply_markup(
        message.chat.id,
        sent_msg.message_id,
        reply_markup=reaction_buttons(sent_msg.message_id)
    )

# =========================
# CHAT ID COMMAND
# =========================
@bot.message_handler(commands=['id'])
def get_id(message):

    bot.reply_to(
        message,
        f"🆔 Chat ID: {message.chat.id}"
    )

# =========================
# POST CONNECT TEXT
# =========================
@bot.message_handler(commands=['postconnectgroup'])
def post_connect(message):

    text = message.text.replace('/postconnectgroup', '').strip()

    if not text:
        return

    sent_msg = bot.send_message(
        CONNECT_CHAT_ID,
        f"📢 {text}"
    )

    bot.edit_message_reply_markup(
        CONNECT_CHAT_ID,
        sent_msg.message_id,
        reply_markup=reaction_buttons(sent_msg.message_id)
    )

# =========================
# POST RED ROOM TEXT
# =========================
@bot.message_handler(commands=['postredroom'])
def post_red(message):

    text = message.text.replace('/postredroom', '').strip()

    if not text:
        return

    sent_msg = bot.send_message(
        REDROOM_CHAT_ID,
        f"📢 {text}"
    )

    bot.edit_message_reply_markup(
        REDROOM_CHAT_ID,
        sent_msg.message_id,
        reply_markup=reaction_buttons(sent_msg.message_id)
    )

# =========================
# POST TV TEXT
# =========================
@bot.message_handler(commands=['posttv'])
def post_tv(message):

    text = message.text.replace('/posttv', '').strip()

    if not text:
        return

    sent_msg = bot.send_message(
        TV_CHANNEL_ID,
        f"📢 {text}"
    )

    bot.edit_message_reply_markup(
        TV_CHANNEL_ID,
        sent_msg.message_id,
        reply_markup=reaction_buttons(sent_msg.message_id)
    )

# =========================
# POST MEDIA TO CONNECT
# =========================
@bot.message_handler(commands=['postconnectmedia'])
def post_connect_media(message):

    if message.from_user.username != ADMIN_USERNAME.replace("@", ""):
        return

    if not message.reply_to_message:
        return

    caption = message.text.replace('/postconnectmedia', '').strip()

    if not caption:
        caption = "🔥 New Sinner City Drop 🔥"

    promo_text = """
🔥 SINNER CITY PROMO REQUEST 🔥
"""

    reply_msg = message.reply_to_message

    if reply_msg.photo:

        sent_msg = bot.send_photo(
            CONNECT_CHAT_ID,
            reply_msg.photo[-1].file_id,
            caption=caption
        )

    elif reply_msg.video:

        sent_msg = bot.send_video(
            CONNECT_CHAT_ID,
            reply_msg.video.file_id,
            caption=caption
        )

    elif reply_msg.document:

        sent_msg = bot.send_document(
            CONNECT_CHAT_ID,
            reply_msg.document.file_id,
            caption=caption
        )

    else:
        return

    markup = InlineKeyboardMarkup(row_width=1)

    markup.add(
        InlineKeyboardButton(
            "⬇️ Download Here",
            url=TV_CHANNEL
        )
    )

    markup.add(
        InlineKeyboardButton(
            "🔞 Click To Find A Match",
            url=CONNECT_GROUP
        )
    )

    markup.row(

        InlineKeyboardButton(
            "🔥 0",
            callback_data=f"fire_{sent_msg.message_id}"
        ),

        InlineKeyboardButton(
            "🥵 0",
            callback_data=f"hot_{sent_msg.message_id}"
        ),

        InlineKeyboardButton(
            "💘 0",
            callback_data=f"love_{sent_msg.message_id}"
        ),

        InlineKeyboardButton(
            "😂 0",
            callback_data=f"laugh_{sent_msg.message_id}"
        )
    )

    bot.edit_message_reply_markup(
        CONNECT_CHAT_ID,
        sent_msg.message_id,
        reply_markup=markup
    )

# =========================
# CALLBACK SYSTEM
# =========================
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    if "_" not in call.data:
        return

    reaction, message_id = call.data.split("_")

    message_id = int(message_id)

    if message_id not in reaction_counts:

        reaction_counts[message_id] = {
            "fire": 0,
            "hot": 0,
            "love": 0,
            "laugh": 0
        }

    reaction_counts[message_id][reaction] += 1

    markup = reaction_buttons(message_id)

    bot.edit_message_reply_markup(
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

    bot.answer_callback_query(
        call.id,
        "Reaction Added 🔥"
    )

# =========================
# DAILY TIMER
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