import os
import asyncio



async def startBot(bot, m):
	print (m)
	await bot.send_message(m.chat.id, "HELLO WORLD")
	
async def  help_func(bot, m):
	print (m)
	await bot.send_message(m.chat.id, " There are multiple things i can do:\nI can Rename Files.\nUpload Files from url.\nApply Thumbnail on Uploaded Files\nGenerate Screenshots from a media file."
	)
	
async def rename_func(bot, m):
	print(m)
	await bot.send_message(m.chat.id, "Welcome to the rename module\nSend me a file, and reply the file with your new Name."
	)
	
async def upload_func(bot, m):
	print(m)
	await bot.send_message(m.chat.id, "Welcome to the upload module \nSend me a valid, and i will try to upload it on Telegram."
	)
	
async def savethumbnail_func(bot, m):
	print(m)
	await bot.send_message(m.chat.id, "Thumbnail Saved \nit will be used on your uploaded file"
 )
 
async def clearthumbnail_func(bot, m):
	print(m)
	await bot.send_message(m.chat.id, "Thumbnail is deleted!")
	
async def screenshots_func(bot, m):
	print(m)
	await bot.send_message(m.chat.id, " Send me a file, and i will generate screenshots from it.")
	
	
