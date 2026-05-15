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
# REACTION STORAGE
# =========================
reaction_counts = {}

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
def reaction_buttons(message_id):

    if message_id not in reaction_counts:

        reaction_counts[message_id] = {
            "fire": 0,
            "hot": 0,
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
✅ Join all official spaces below 👇
"""

    markup = InlineKeyboardMarkup()

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

    sent_msg1 = bot.send_message(
        CONNECT_CHAT_ID,
        message_text
    )

    bot.edit_message_reply_markup(
        CONNECT_CHAT_ID,
        sent_msg1.message_id,
        reply_markup=markup
    )

    sent_msg2 = bot.send_message(
        REDROOM_CHAT_ID,
        message_text
    )

    bot.edit_message_reply_markup(
        REDROOM_CHAT_ID,
        sent_msg2.message_id,
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
            "📜 GROUP RULES",
            callback_data="show_rules"
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

    sent_msg = bot.send_message(
        message.chat.id,
        """
🔥 SINNER CITY RULES 🔥

1. Respect all members.
2. No spam or unnecessary flooding.
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

    sent_msg = bot.send_message(
        message.chat.id,
        f"""
{quote}

Need a connect?

Use:
/adminconnect
"""
    )

    bot.edit_message_reply_markup(
        message.chat.id,
        sent_msg.message_id,
        reply_markup=reaction_buttons(sent_msg.message_id)
    )

# =========================
# NIGHT MESSAGE
# =========================
@bot.message_handler(commands=['naughtygoodnightaiquote'])
def night(message):

    quote = random.choice(night_quotes)

    sent_msg = bot.send_message(
        message.chat.id,
        f"""
{quote}

Ready to find your vibe?

Use:
/adminconnect
"""
    )

    bot.edit_message_reply_markup(
        message.chat.id,
        sent_msg.message_id,
        reply_markup=reaction_buttons(sent_msg.message_id)
    )

# =========================
# NAUGHTY TRUTH
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
# EXTREME DARE
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

    sent_msg = bot.send_message(
        CONNECT_CHAT_ID,
        f"📢 {text}",
        reply_markup=reaction_buttons(0)
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

    sent_msg = bot.send_message(
        REDROOM_CHAT_ID,
        f"📢 {text}",
        reply_markup=reaction_buttons(0)
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

    sent_msg = bot.send_message(
        TV_CHANNEL_ID,
        f"📢 {text}",
        reply_markup=reaction_buttons(0)
    )

    bot.reply_to(message, "✅ Posted to TV Channel.")

# =========================
# POST ALL TEXT
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
        reply_markup=reaction_buttons(0)
    )

    bot.send_message(
        REDROOM_CHAT_ID,
        f"📢 {text}",
        reply_markup=reaction_buttons(0)
    )

    bot.send_message(
        TV_CHANNEL_ID,
        f"📢 {text}",
        reply_markup=reaction_buttons(0)
    )

    bot.reply_to(message, "✅ Posted everywhere.")

# =========================
# POST MEDIA TO CONNECT GROUP
# =========================
@bot.message_handler(commands=['postconnectmedia'])
def post_connect_media(message):

    if message.from_user.username != ADMIN_USERNAME.replace("@", ""):
        return

    if not message.reply_to_message:

        bot.reply_to(
            message,
            "⚠️ Reply to media with:\n/postconnectmedia Caption"
        )
        return

    caption = message.text.replace('/postconnectmedia', '').strip()

    if not caption:
        caption = "🔥 New Sinner City Drop 🔥"

    promo_text = """
🔥 SINNER CITY PROMO REQUEST 🔥

Name / Brand:
Advert Type:
What are you promoting:
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
        bot.reply_to(message, "⚠️ Unsupported media.")
        return

    reaction_counts[sent_msg.message_id] = {
        "fire": 0,
        "hot": 0,
        "laugh": 0
    }

    markup = InlineKeyboardMarkup(row_width=1)

    markup.add(
        InlineKeyboardButton(
            "⬇️ Download Here",
            url=TV_CHANNEL
        )
    )

    markup.add(
        InlineKeyboardButton(
            "📢 DM for Ads/Promo",
            url=f"https://t.me/share/url?url=&text={promo_text}"
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
            "😂 0",
            callback_data=f"laugh_{sent_msg.message_id}"
        )
    )

    bot.edit_message_reply_markup(
        CONNECT_CHAT_ID,
        sent_msg.message_id,
        reply_markup=markup
    )

    bot.reply_to(message, "✅ Media posted to Connect Group.")

# =========================
# POST MEDIA TO RED ROOM
# =========================
@bot.message_handler(commands=['postredmedia'])
def post_red_media(message):

    if message.from_user.username != ADMIN_USERNAME.replace("@", ""):
        return

    if not message.reply_to_message:

        bot.reply_to(
            message,
            "⚠️ Reply to media with:\n/postredmedia Caption"
        )
        return

    caption = message.text.replace('/postredmedia', '').strip()

    if not caption:
        caption = "🔥 New Sinner City Drop 🔥"

    reply_msg = message.reply_to_message

    if reply_msg.photo:

        sent_msg = bot.send_photo(
            REDROOM_CHAT_ID,
            reply_msg.photo[-1].file_id,
            caption=caption
        )

    elif reply_msg.video:

        sent_msg = bot.send_video(
            REDROOM_CHAT_ID,
            reply_msg.video.file_id,
            caption=caption
        )

    elif reply_msg.document:

        sent_msg = bot.send_document(
            REDROOM_CHAT_ID,
            reply_msg.document.file_id,
            caption=caption
        )

    else:
        bot.reply_to(message, "⚠️ Unsupported media.")
        return

    reaction_counts[sent_msg.message_id] = {
        "fire": 0,
        "hot": 0,
        "laugh": 0
    }

    bot.edit_message_reply_markup(
        REDROOM_CHAT_ID,
        sent_msg.message_id,
        reply_markup=reaction_buttons(sent_msg.message_id)
    )

    bot.reply_to(message, "✅ Media posted to Red Room.")

# =========================
# POST MEDIA TO TV CHANNEL
# =========================
@bot.message_handler(commands=['posttvmedia'])
def post_tv_media(message):

    if message.from_user.username != ADMIN_USERNAME.replace("@", ""):
        return

    if not message.reply_to_message:

        bot.reply_to(
            message,
            "⚠️ Reply to media with:\n/posttvmedia Caption"
        )
        return

    caption = message.text.replace('/posttvmedia', '').strip()

    if not caption:
        caption = "🔥 New Sinner City Drop 🔥"

    reply_msg = message.reply_to_message

    if reply_msg.photo:

        sent_msg = bot.send_photo(
            TV_CHANNEL_ID,
            reply_msg.photo[-1].file_id,
            caption=caption
        )

    elif reply_msg.video:

        sent_msg = bot.send_video(
            TV_CHANNEL_ID,
            reply_msg.video.file_id,
            caption=caption
        )

    elif reply_msg.document:

        sent_msg = bot.send_document(
            TV_CHANNEL_ID,
            reply_msg.document.file_id,
            caption=caption
        )

    else:
        bot.reply_to(message, "⚠️ Unsupported media.")
        return

    reaction_counts[sent_msg.message_id] = {
        "fire": 0,
        "hot": 0,
        "laugh": 0
    }

    bot.edit_message_reply_markup(
        TV_CHANNEL_ID,
        sent_msg.message_id,
        reply_markup=reaction_buttons(sent_msg.message_id)
    )

    bot.reply_to(message, "✅ Media posted to TV Channel.")

# =========================
# CALLBACKS
# =========================
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    if call.data == "show_rules":

        bot.send_message(
            call.message.chat.id,
            """
🔥 SINNER CITY RULES 🔥

1. Respect all members.
2. No spam or unnecessary flooding.
3. Verification is ONLY for ladies.
4. Guys use /adminconnect
5. React to admin posts daily.
6. XP is earned through engagement.
7. Ghost members may be removed.
8. No leaking private connects.
9. Stay active in all official spaces.
"""
        )
        return

    data = call.data.split("_")

    reaction = data[0]
    message_id = int(data[1])

    if message_id not in reaction_counts:

        reaction_counts[message_id] = {
            "fire": 0,
            "hot": 0,
            "laugh": 0
        }

    reaction_counts[message_id][reaction] += 1

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
            f"😂 {reaction_counts[message_id]['laugh']}",
            callback_data=f"laugh_{message_id}"
        )
    )

    bot.edit_message_reply_markup(
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

    bot.answer_callback_query(
        call.id,
        "Reaction added 🔥"
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