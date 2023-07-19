import logging
import os
from db import create_table, retrieve_file_id_by_file_name, insert_data, retrieve_admins_by_chat_id
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from dotenv import load_dotenv
load_dotenv()


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Telegram bot token
token = os.getenv('telegram_bot_token')

# Initialize bot
bot = telegram.Bot(token)


class Updates:
    def __init__(self, update):
        self.update = update
        update = self.update
        self.update_id = update['update_id']
        self.is_file = True
        update = self.update['message']
        try:
            self.file_id = update['document']['file_id']
            logging.info(f"File id : {self.file_id}")
        except:
            self.is_file = False
        self.message_txt = update['text']
        self.message_id = update['message_id']
        self.chat_id = update['chat']['id']
        self.chat_type = update['chat']['type']
        self.sender_id = update['from_user']['id']
        if update['caption'] != None:
            self.caption = update['caption']
        update = self.update['message']['from_user']
        self.sender_id = update['id']
        self.sender_username = update['username']

        logging.info(
            f"Message ID : {self.message_id} | Sender ID : {self.sender_id} | Chat ID : {self.chat_id}")

# Commands for non-admin users


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    message = """Hi! This is @Rushour0 's bot
Enter "/file filename" to get a specific file """

    update.message.reply_text(message)


def document(update, context):
    """Document"""
    info = Updates(update)
    try:
        logging.info(f"Caption : {info.caption}")
    except:
        pass


def text(update, context):
    """Text"""
    info = Updates(update)


def callfile(update, context):
    info = Updates(update)
    file_name = info.message_txt[6:].lower()
    logging.info(f"File called : {file_name}")
    file_id = retrieve_file_id_by_file_name(file_name)
    if file_id:
        bot.sendDocument(info.chat_id, document=file_id)
        logging.info(f"File sent : {file_name}")
    else:
        bot.sendMessage(info.chat_id, "File not found!")
        logging.info(f"File not found : {file_name}")

# Commands for admin users


def addfile(update, context):
    info = Updates(update)
    file_name = info.caption[9:].lower()
    logging.info(f"Adding file : {file_name}")
    if info.caption and info.caption.startswith("/addfile ") and ((info.sender_id == info.chat_id) or (retrieve_admins_by_chat_id(info.chat_id))):
        message_id = retrieve_file_id_by_file_name(file_name)
        if message_id:
            update.message.reply_text(
                "File name already exists, save with another file name")
            return
        insert_data(file_name, info.file_id)
        update.message.reply_text("File has been saved!")
        logging.info(f"File saved : {file_name}")
        return
    logging.info(f"File not saved : {file_name}")
    update.message.reply_text("File not saved! You are not an admin")


def error(update, context):
    """Log Errors caused by Updates."""
    logging.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Initialize the bot commands."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("file", callfile))

    # message checkers
    dp.add_handler(MessageHandler(Filters.document, addfile))
    dp.add_handler(MessageHandler(Filters.text, text))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    create_table()
    main()
    bot.sendMessage(chat_id=702154724, text="Hi")
# bot.sendMessage(chat_id=1087968824,text = "Grp")
