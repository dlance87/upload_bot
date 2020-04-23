from aiohttp import ClientSession
import aiofiles

async def download(url, nome, msg):
	try:
		async with ClientSession() as session:
			async with session.get(url, ssl=False) as resp:
				async with aiofiles.open(nome, "wb") as f:
					while True:
						chunk = await resp.content.read(16144)
						if not chunk: break
						await f.write(chunk)
					f.close()
					return True
						
	except Exception as e:
		await msg.reply_text(f"ERROR: {e}")
		return False 