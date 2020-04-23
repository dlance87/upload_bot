from pyrogram import Client
from urllib.request import urlretrieve
from urllib.parse import unquote 
from re import compile
from downloadProcess import download
from os import remove 
from os.path import isfile

async def upload (bot, m):
	try:
		extract_url = compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[#!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+").search(m.text).group(0)
		url = extract_url
		msg = await m.reply_text("..processing")
		if "|" in m.text and not m.text.split("|")[1].strip() == "": filename = unquote(m.text.split('|')[-1].strip())
		else: filename = unquote(url.split("filename=")[-1].split("name=")[-1].split("title=")[-1].split("&")[0].split('/')[-1].split('?')[0].split("&")[0])
		await msg.edit_text("...downloading file")
		resp_status = await download(url, filename, m)
		
		if not resp_status: pass
		else: 
			await msg.edit_text("..uploading file")
			await m.reply_document(filename)
			if isfile(filename): remove(filename)
		await msg.delete()
	except Exception as e:
		print (e)
		await msg.edit_text("Invalid URL")
			
			
		
		
