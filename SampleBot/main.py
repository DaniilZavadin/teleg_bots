import logging
from telegram.ext import *
import constants as keys
import responses as responses

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s %(levelname)s - %(message)s', level=logging.INFO)
logging.info('CryoBot onilne!')


def start_command(update, context):
    update.message.reply_text('Greetings! Whatcha been up to?')


def help_command(update, context):
    update.message.reply_text('Try typing anything')


def handle_message(update, context):
    text = str(update.message.text).lower()
    # res = responses.sample_responses(text)
    res = responses.get_response(text)
    logging.info(f'User {update.message.chat.id} says: {text}')

    update.message.reply_text(res)


def error(update, context):
    logging.info(f"Update {context} caused erorr {context.error}")


if __name__ == "__main__":
    updater = Updater(keys.API_KEY, use_context=True)
    dispatch = updater.dispatcher

    dispatch.add_handler(CommandHandler('start', start_command))
    dispatch.add_handler(CommandHandler('help', help_command))

    dispatch.add_handler(MessageHandler(Filters.text, handle_message))

    dispatch.add_error_handler(error)

    updater.start_polling(2)
    updater.idle()
