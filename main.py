import os, json, re, requests, asyncio, sys
from pyrogram import Client, idle

# 1. تعريف المتغيرات الأساسية من Environment Variables
token = os.environ.get("8063254835:AAHxabPeLMA4t4_R33MI8nP__8hfZR8g7uE")
owner_id = int(os.environ.get("8526612004"))
Dev_Neptune = token.split(':')[0]

print('''
Loading…
█▒▒▒▒▒▒▒▒▒''')

# 2. جلب البيانات وحفظها
try:
    from information import *
    Dev_Neptune = token.split(':')[0]
except:
    with open('information.py','w+') as www:
        www.write(f'token = "{token}"\nowner_id = {owner_id}')

print('''
10% 
███▒▒▒▒▒▒▒ ''')

# 3. تجهيز ملف الإعدادات config.py
to_config = f"token = '{token}'\n"
to_config += f"Dev_Neptune = token.split(':')[0]\n"
to_config += f"sudo_id = {owner_id}\n"

# جلب اليوزر نيم
try:
    username = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()["result"]["username"]
except:
    username = "unknown"

to_config += f"botUsername = '{username}'\n"
to_config += "from kvsqlite.sync import Client as DB\n"
to_config += "ytdb = DB('ytdb.sqlite')\n"
to_config += "sounddb = DB('sounddb.sqlite')\n"
to_config += "wsdb = DB('wsdb.sqlite')"

print('''
30% 
█████▒▒▒▒▒ ''')

with open('config.py','w+') as w:
    w.write(to_config)

print('''
50% 
███████▒▒▒ ''')

# 4. تشغيل التطبيق
app = Client(f'{Dev_Neptune}Neptune', 28850159, '09a3e7d212b434aec973ad5ea10d8ec6', bot_token=token, plugins={"root": "Plugins"})

app.start()
print("• 𝖲𝖮𝖴𝖱𝖢𝖤 𝖩𝖠𝖢𝖪 𝖨𝖲 𝖴𝖯 𝖠𝖭𝖣 𝖱𝖴𝖭𝖭I𝖭𝖦 ...")
print('100% \n██████████')
idle()
