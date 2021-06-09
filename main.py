from telegram.ext import *
import Messages as M

API_KEY = "1595620905:AAE70FUVJBAXQb4gInwrlu4o_aAJQIOyaOw"


def start_command(update, context):
    update.message.reply_text("Type anything to get started!")


def help_command(update, context):
    update.message.reply_text("If you want help, ask google.")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = M.sample_responses(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(API_KEY, use_context=True)
    ud = updater.dispatcher

    ud.add_handler(CommandHandler("start", start_command))
    ud.add_handler(CommandHandler("help", help_command))
    ud.add_handler(MessageHandler(Filters.text, handle_message))
    ud.add_error_handler(error)
    updater.start_polling()
    updater.idle()


main()
