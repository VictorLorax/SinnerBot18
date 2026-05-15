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

    # CONNECT GROUP
    markup.add(
        InlineKeyboardButton(
            "🔞 Connect Group",
            url=CONNECT_GROUP
        )
    )

    # RED ROOM
    markup.add(
        InlineKeyboardButton(
            "🥵💦 Red Room",
            url=REDROOM_GROUP
        )
    )

    # TV CHANNEL
    markup.add(
        InlineKeyboardButton(
            "📺 TV Channel",
            url=TV_CHANNEL
        )
    )

    # CONTACT ADMIN
    markup.add(
        InlineKeyboardButton(
            "🔞 CONTACT ADMIN",
            url=f"https://t.me/{ADMIN_USERNAME.replace('@','')}"
        )
    )

    # SEND TO CONNECT GROUP
    sent_msg1 = bot.send_message(
        CONNECT_CHAT_ID,
        message_text,
        reply_markup=markup
    )

    # ADD REACTIONS
    bot.edit_message_reply_markup(
        CONNECT_CHAT_ID,
        sent_msg1.message_id,
        reply_markup=reaction_buttons(sent_msg1.message_id)
    )

    # SEND TO RED ROOM
    sent_msg2 = bot.send_message(
        REDROOM_CHAT_ID,
        message_text,
        reply_markup=markup
    )

    # ADD REACTIONS
    bot.edit_message_reply_markup(
        REDROOM_CHAT_ID,
        sent_msg2.message_id,
        reply_markup=reaction_buttons(sent_msg2.message_id)
    )

    # CLEAR MEMBER STORAGE
    daily_new_members.clear()


# =========================
# POST MEDIA EVERYWHERE
# REPLY TO PHOTO / VIDEO / FILE
# =========================
@bot.message_handler(commands=['postmedia'])
def post_media(message):

    # =========================
    # ADMIN CHECK
    # =========================
    if message.from_user.username != ADMIN_USERNAME.replace("@", ""):
        return

    # =========================
    # MUST REPLY TO MEDIA
    # =========================
    if not message.reply_to_message:

        bot.reply_to(
            message,
            "⚠️ Reply to a media file with:\n/postmedia Your Caption"
        )
        return

    # =========================
    # CAPTION
    # =========================
    caption = message.text.replace('/postmedia', '').strip()

    if not caption:
        caption = "🔥 New Sinner City Drop 🔥"

    # =========================
    # PROMO TEXT
    # =========================
    promo_text = """
🔥 SINNER CITY PROMO REQUEST 🔥

Name / Brand:
Advert Type:
What are you promoting:

I am ready to pay ₦1000 for promo.
"""

    # =========================
    # GET REPLIED MEDIA
    # =========================
    reply_msg = message.reply_to_message

    # STORE SENT MESSAGES
    sent_messages = []

    # =========================
    # PHOTO
    # =========================
    if reply_msg.photo:

        file_id = reply_msg.photo[-1].file_id

        sent1 = bot.send_photo(
            CONNECT_CHAT_ID,
            file_id,
            caption=caption
        )

        sent2 = bot.send_photo(
            REDROOM_CHAT_ID,
            file_id,
            caption=caption
        )

        sent3 = bot.send_photo(
            TV_CHANNEL_ID,
            file_id,
            caption=caption
        )

        sent_messages = [
            (sent1, CONNECT_CHAT_ID),
            (sent2, REDROOM_CHAT_ID),
            (sent3, TV_CHANNEL_ID)
        ]

    # =========================
    # VIDEO
    # =========================
    elif reply_msg.video:

        file_id = reply_msg.video.file_id

        sent1 = bot.send_video(
            CONNECT_CHAT_ID,
            file_id,
            caption=caption
        )

        sent2 = bot.send_video(
            REDROOM_CHAT_ID,
            file_id,
            caption=caption
        )

        sent3 = bot.send_video(
            TV_CHANNEL_ID,
            file_id,
            caption=caption
        )

        sent_messages = [
            (sent1, CONNECT_CHAT_ID),
            (sent2, REDROOM_CHAT_ID),
            (sent3, TV_CHANNEL_ID)
        ]

    # =========================
    # DOCUMENT / MOVIE FILE
    # =========================
    elif reply_msg.document:

        file_id = reply_msg.document.file_id

        sent1 = bot.send_document(
            CONNECT_CHAT_ID,
            file_id,
            caption=caption
        )

        sent2 = bot.send_document(
            REDROOM_CHAT_ID,
            file_id,
            caption=caption
        )

        sent3 = bot.send_document(
            TV_CHANNEL_ID,
            file_id,
            caption=caption
        )

        sent_messages = [
            (sent1, CONNECT_CHAT_ID),
            (sent2, REDROOM_CHAT_ID),
            (sent3, TV_CHANNEL_ID)
        ]

    # =========================
    # UNSUPPORTED MEDIA
    # =========================
    else:

        bot.reply_to(
            message,
            "⚠️ Unsupported media type."
        )
        return

    # =========================
    # ADD BUTTONS + REACTIONS
    # =========================
    for sent_msg, chat_id in sent_messages:

        # CREATE REACTION STORAGE
        if sent_msg.message_id not in reaction_counts:

            reaction_counts[sent_msg.message_id] = {
                "fire": 0,
                "hot": 0,
                "laugh": 0
            }

        # FINAL BUTTON MARKUP
        final_markup = InlineKeyboardMarkup(row_width=1)

        # DOWNLOAD BUTTON
        final_markup.add(
            InlineKeyboardButton(
                "⬇️ Download Here",
                url=TV_CHANNEL
            )
        )

        # ADS BUTTON
        final_markup.add(
            InlineKeyboardButton(
                "📢 DM for Ads/Promo",
                url=f"https://t.me/share/url?url=&text={promo_text}"
            )
        )

        # MATCH BUTTON
        final_markup.add(
            InlineKeyboardButton(
                "🔞 Click To Find A Match",
                url=CONNECT_GROUP
            )
        )

        # REACTION BUTTONS
        final_markup.row(

            InlineKeyboardButton(
                f"🔥 {reaction_counts[sent_msg.message_id]['fire']}",
                callback_data=f"fire_{sent_msg.message_id}"
            ),

            InlineKeyboardButton(
                f"🥵 {reaction_counts[sent_msg.message_id]['hot']}",
                callback_data=f"hot_{sent_msg.message_id}"
            ),

            InlineKeyboardButton(
                f"😂 {reaction_counts[sent_msg.message_id]['laugh']}",
                callback_data=f"laugh_{sent_msg.message_id}"
            )
        )

        # APPLY BUTTONS
        bot.edit_message_reply_markup(
            chat_id,
            sent_msg.message_id,
            reply_markup=final_markup
        )

    # =========================
    # SUCCESS MESSAGE
    # =========================
    bot.reply_to(
        message,
        "✅ Media posted everywhere successfully."
    )