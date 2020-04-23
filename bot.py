from pyrogram import Client, Filters, MessageHandler, CallbackQueryHandler
from robot.commands import *
from upload import upload
from downloadProcess import download

if __name__ == "__main__" :
                #Lets create our download directory, if it doesnt exist
        if not os.path.isdir("/Downloads"):
                os.makedirs("/Downloads")
                token_bot = "TOKEN"
                bot = Client(
                        "my_bot",
                        bot_token=token_bot,
                        api_id=838378,
                        api_hash="05370bb6f2eea0f33c6325eaa5ad3ac3",
                        workers=100
                )
                bot.DOWNLOAD_WORKERS = 100
                #
                bot.add_handler(MessageHandler(
                        startBot,
                        filters=Filters.command(["start"], prefixes=["/", "!", "$", "#"]))
	        )
                bot.add_handler(MessageHandler(
                        help_func,
                        filters=Filters.command(["help"], prefixes=["/", "!", "$", "#"]))
	        )
                bot.add_handler(MessageHandler(
                        rename_func,
                        filters=Filters.command(["rename"], prefixes=["/"]))
	        )
                bot.add_handler(MessageHandler(
                        upload_func,
                        filters=Filters.command(["upload"], prefixes=["/"]))
	        )
                bot.add_handler(MessageHandler(
                        savethumbnail_func,
                        filters=Filters.command(["savethumbnail"], prefixes=["/"]))
	        )
                bot.add_handler(MessageHandler(
                        clearthumbnail_func,
                        filters=Filters.command(["clearthumbnail"], prefixes=["/"]))
	        )
                bot.add_handler(MessageHandler(
                        screenshots_func,
                        filters=Filters.command(["screenshots"], prefixes=["/"]))
	        )
                bot.add_handler(MessageHandler(
                        process,
                        filters=Filters.text)
	        )
                #
                bot.run()
