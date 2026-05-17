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
# ADMIN INFO
# =========================
ADMIN_USERNAME = "@SinnerKing"

# BETTER: replace with your real Telegram numeric ID
# Example:
# ADMIN_ID = 123456789

# =========================
# LINKS
# =========================
CONNECT_GROUP = "https://t.me/+IsnkwS7RZRU3YTNk"
REDROOM_GROUP = "https://t.me/+Cb1uEABDl34xZmE8"
TV_CHANNEL = "https://t.me/SINNERTV"

# =========================
# CHAT IDS
# =========================
CONNECT_CHAT_ID = -1003256157463
REDROOM_CHAT_ID = -1003867191682
TV_CHANNEL_ID = -1002681661405

# =========================
# STORAGE
# =========================
daily_new_members = []
reaction_counts = {}
media_store = {}
user_states = {}

# =========================
# QUOTES
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
# SAVE MEDIA
# =========================
def save_media(message_id, file_id, media_type):

    media_store[message_id] = {
        "file_id": file_id,
        "type": media_type
    }

# =========================
# SEND DOWNLOAD
# =========================
def send_download(chat_id, message_id):

    if message_id not in media_store:

        bot.send_message(
            chat_id,
            "⚠️ File unavailable."
        )
        return

    media = media_store[message_id]

    if media["type"] == "photo":

        bot.send_photo(
            chat_id,
            media["file_id"],
            caption="⬇️ Download Ready"
        )

    elif media["type"] == "video":

        bot.send_video(
            chat_id,
            media["file_id"],
            caption="⬇️ Download Ready"
        )

    elif media["type"] == "document":

        bot.send_document(
            chat_id,
            media["file_id"],
            caption="⬇️ Download Ready"
        )

# =========================
# BUTTON SYSTEM
# =========================
def media_buttons(message_id):

    if message_id not in reaction_counts:

        reaction_counts[message_id] = {
            "fire": 0,
            "hot": 0,
            "laugh": 0
        }

    markup = InlineKeyboardMarkup(row_width=1)

    # DOWNLOAD
    markup.add(
        InlineKeyboardButton(
            "⬇️ Download File",
            callback_data=f"download_{message_id}"
        )
    )

    # ADS
    markup.add(
        InlineKeyboardButton(
            "📢 DM for Ads/Promo",
            callback_data="ads_form"
        )
    )

    # MATCH
    markup.add(
        InlineKeyboardButton(
            "🔞 Click To Find A Match",
            callback_data="match_form"
        )
    )

    # REACTIONS
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
# NEW MEMBERS
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
# DAILY WELCOME
# =========================
def daily_welcome_post():

    if not daily_new_members:
        return

    members_text = "\n".join(daily_new_members)

    text = f"""
🔥 DAILY SINNER CITY WELCOME 🔥

Welcome our new sinners today 👀

{members_text}

━━━━━━━━━━━━━━━

📜 SINNER CITY RULES

1. Respect all members.
2. No spam.
3. Verification is ONLY for ladies.
4. Guys use /adminconnect
5. React to admin posts daily.
6. XP is earned through engagement.
7. Ghost members may be removed.
8. No leaking private connects.
9. Stay active in all official spaces.
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

    bot.send_message(
        CONNECT_CHAT_ID,
        text,
        reply_markup=markup
    )

    bot.send_message(
        REDROOM_CHAT_ID,
        text,
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
            "📜 Rules",
            callback_data="show_rules"
        )
    )

    bot.send_message(
        message.chat.id,
        """
🔥 Welcome To Sinner City 🔥

Choose where you want to enter 👇
""",
        reply_markup=markup
    )

# =========================
# RULES
# =========================
@bot.message_handler(commands=['rules'])
def rules(message):

    sent_msg = bot.send_message(
        message.chat.id,
        """
📜 SINNER CITY RULES

1. Respect members
2. No spam
3. No leaks
4. Stay active
"""
    )

    bot.edit_message_reply_markup(
        message.chat.id,
        sent_msg.message_id,
        reply_markup=media_buttons(sent_msg.message_id)
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
        reply_markup=media_buttons(sent_msg.message_id)
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
        reply_markup=media_buttons(sent_msg.message_id)
    )

# =========================
# TRUTH
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
        reply_markup=media_buttons(sent_msg.message_id)
    )

# =========================
# DARE
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
        reply_markup=media_buttons(sent_msg.message_id)
    )

# =========================
# POST CONNECT MEDIA
# =========================
@bot.message_handler(commands=['postconnectmedia'])
def post_connect_media(message):

    if not message.reply_to_message:

        bot.reply_to(
            message,
            "⚠️ Reply to media with:\n/postconnectmedia Caption"
        )
        return

    caption = message.text.replace('/postconnectmedia', '').strip()

    if not caption:
        caption = "🔥 New Sinner City Drop 🔥"

    reply_msg = message.reply_to_message

    # PHOTO
    if reply_msg.photo:

        file_id = reply_msg.photo[-1].file_id

        sent_msg = bot.send_photo(
            CONNECT_CHAT_ID,
            file_id,
            caption=caption
        )

        save_media(
            sent_msg.message_id,
            file_id,
            "photo"
        )

    # VIDEO
    elif reply_msg.video:

        file_id = reply_msg.video.file_id

        sent_msg = bot.send_video(
            CONNECT_CHAT_ID,
            file_id,
            caption=caption
        )

        save_media(
            sent_msg.message_id,
            file_id,
            "video"
        )

    # DOCUMENT
    elif reply_msg.document:

        file_id = reply_msg.document.file_id

        sent_msg = bot.send_document(
            CONNECT_CHAT_ID,
            file_id,
            caption=caption
        )

        save_media(
            sent_msg.message_id,
            file_id,
            "document"
        )

    else:

        bot.reply_to(
            message,
            "⚠️ Unsupported media."
        )
        return

    bot.edit_message_reply_markup(
        CONNECT_CHAT_ID,
        sent_msg.message_id,
        reply_markup=media_buttons(sent_msg.message_id)
    )

    bot.reply_to(
        message,
        "✅ Media posted."
    )

# =========================
# POST MEDIA TO TV CHANNEL
# =========================
@bot.message_handler(commands=['posttvmedia'])
def post_tv_media(message):

    if not message.reply_to_message:

        bot.reply_to(
            message,
            "⚠️ Reply to media with:\n/posttvmedia Caption"
        )
        return

    caption = message.text.replace('/posttvmedia', '').strip()

    if not caption:
        caption = "🔥 New TV Channel Drop 🔥"

    reply_msg = message.reply_to_message

    # PHOTO
    if reply_msg.photo:

        file_id = reply_msg.photo[-1].file_id

        sent_msg = bot.send_photo(
            TV_CHANNEL_ID,
            file_id,
            caption=caption
        )

        save_media(
            sent_msg.message_id,
            file_id,
            "photo"
        )

    # VIDEO
    elif reply_msg.video:

        file_id = reply_msg.video.file_id

        sent_msg = bot.send_video(
            TV_CHANNEL_ID,
            file_id,
            caption=caption
        )

        save_media(
            sent_msg.message_id,
            file_id,
            "video"
        )

    # DOCUMENT
    elif reply_msg.document:

        file_id = reply_msg.document.file_id

        sent_msg = bot.send_document(
            TV_CHANNEL_ID,
            file_id,
            caption=caption
        )

        save_media(
            sent_msg.message_id,
            file_id,
            "document"
        )

    else:

        bot.reply_to(
            message,
            "⚠️ Unsupported media."
        )
        return

    bot.edit_message_reply_markup(
        TV_CHANNEL_ID,
        sent_msg.message_id,
        reply_markup=media_buttons(sent_msg.message_id)
    )

    bot.reply_to(
        message,
        "✅ Media posted to TV Channel."
    )

# =========================
# POST MEDIA TO RED ROOM
# =========================
@bot.message_handler(commands=['postredmedia'])
def post_red_media(message):

    if not message.reply_to_message:

        bot.reply_to(
            message,
            "⚠️ Reply to media with:\n/postredmedia Caption"
        )
        return

    caption = message.text.replace('/postredmedia', '').strip()

    if not caption:
        caption = "🔥 New Red Room Drop 🔥"

    reply_msg = message.reply_to_message

    # PHOTO
    if reply_msg.photo:

        file_id = reply_msg.photo[-1].file_id

        sent_msg = bot.send_photo(
            REDROOM_CHAT_ID,
            file_id,
            caption=caption
        )

        save_media(
            sent_msg.message_id,
            file_id,
            "photo"
        )

    # VIDEO
    elif reply_msg.video:

        file_id = reply_msg.video.file_id

        sent_msg = bot.send_video(
            REDROOM_CHAT_ID,
            file_id,
            caption=caption
        )

        save_media(
            sent_msg.message_id,
            file_id,
            "video"
        )

    # DOCUMENT
    elif reply_msg.document:

        file_id = reply_msg.document.file_id

        sent_msg = bot.send_document(
            REDROOM_CHAT_ID,
            file_id,
            caption=caption
        )

        save_media(
            sent_msg.message_id,
            file_id,
            "document"
        )

    else:

        bot.reply_to(
            message,
            "⚠️ Unsupported media."
        )
        return

    bot.edit_message_reply_markup(
        REDROOM_CHAT_ID,
        sent_msg.message_id,
        reply_markup=media_buttons(sent_msg.message_id)
    )

    bot.reply_to(
        message,
        "✅ Media posted to Red Room."
    )

# =========================
# ADS FORM
# =========================
def start_ads_form(user_id):

    user_states[user_id] = "ads_name"

    bot.send_message(
        user_id,
        """
📢 SINNER CITY ADS REQUEST

Send your Name / Brand:
"""
    )

# =========================
# MATCH FORM
# =========================
def start_match_form(user_id):

    user_states[user_id] = "match_name"

    bot.send_message(
        user_id,
        """
🔞 SINNER CITY MATCH REQUEST

Send your name:
"""
    )

# =========================
# PRIVATE FORM HANDLER
# =========================
@bot.message_handler(func=lambda m: m.chat.type == "private")
def private_forms(message):

    user_id = message.from_user.id

    if user_id not in user_states:
        return

    state = user_states[user_id]

    # ADS FLOW
    if state == "ads_name":

        user_states[user_id] = {
            "flow": "ads",
            "name": message.text
        }

        bot.send_message(
            user_id,
            "📢 What are you promoting?"
        )

    elif isinstance(state, dict) and state["flow"] == "ads" and "promo" not in state:

        state["promo"] = message.text

        user_states[user_id] = state

        bot.send_message(
            user_id,
            """
💰 Promo fee is ₦1000

Type:
I ACCEPT
"""
        )

    elif isinstance(state, dict) and state["flow"] == "ads" and "promo" in state:

        if message.text.upper() != "I ACCEPT":

            bot.send_message(
                user_id,
                "⚠️ Type I ACCEPT"
            )
            return

        bot.send_message(
            ADMIN_USERNAME,
            f"""
📢 NEW PROMO REQUEST

👤 Name:
{state['name']}

📢 Promotion:
{state['promo']}

💰 Accepted ₦1000 fee.
"""
        )

        bot.send_message(
            user_id,
            "✅ Promo request sent."
        )

        del user_states[user_id]

    # MATCH FLOW
    elif state == "match_name":

        user_states[user_id] = {
            "flow": "match",
            "name": message.text
        }

        bot.send_message(
            user_id,
            "📍 Send your location:"
        )

    elif isinstance(state, dict) and state["flow"] == "match" and "location" not in state:

        state["location"] = message.text

        user_states[user_id] = state

        bot.send_message(
            user_id,
            "🔞 What type of connect do you want?"
        )

    elif isinstance(state, dict) and state["flow"] == "match" and "connect" not in state:

        state["connect"] = message.text

        bot.send_message(
            ADMIN_USERNAME,
            f"""
🔞 NEW MATCH REQUEST

👤 Name:
{state['name']}

📍 Location:
{state['location']}

🔞 Connect Type:
{state['connect']}
"""
        )

        bot.send_message(
            user_id,
            "✅ Match request sent."
        )

        del user_states[user_id]

# =========================
# CALLBACKS
# =========================
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    # RULES
    if call.data == "show_rules":

        bot.send_message(
            call.message.chat.id,
            """
📜 SINNER CITY RULES

1. Respect members
2. No spam
3. No leaks
4. Stay active
"""
        )
        return

    # DOWNLOAD
    if call.data.startswith("download_"):

        message_id = int(call.data.split("_")[1])

        send_download(
            call.from_user.id,
            message_id
        )

        bot.answer_callback_query(
            call.id,
            "⬇️ Download sent to your DM."
        )

        return

    # ADS FORM
    if call.data == "ads_form":

        start_ads_form(call.from_user.id)

        bot.answer_callback_query(
            call.id,
            "📢 Check your DM."
        )

        return

    # MATCH FORM
    if call.data == "match_form":

        start_match_form(call.from_user.id)

        bot.answer_callback_query(
            call.id,
            "🔞 Check your DM."
        )

        return

    # REACTIONS
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

    bot.edit_message_reply_markup(
        call.message.chat.id,
        call.message.message_id,
        reply_markup=media_buttons(message_id)
    )

    bot.answer_callback_query(
        call.id,
        "🔥 Reaction Added"
    )

# =========================
# SCHEDULER
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
print("🔥 Sinner City Bot Running...")

bot.infinity_polling()