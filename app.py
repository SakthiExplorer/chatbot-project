from Adafruit_IO import Client

from telegram.ext import Updater,MessageHandler,Filters
aio = Client(username, Adafruit_API)
def demo1(bot,update):
  chat_id=bot.message.chat_id
  path = 'https://image.shutterstock.com/image-vector/fine-sticker-social-media-content-260nw-1138003112.jpg'
  bot.message.reply_text('I am fine')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def demo2(bot,update):
  bot.message.reply_text("That's great")

def demo3(bot,update):
  bot.message.reply_text("My name is SakthiBot")

def demo4(bot,update):
  aio.send('light', 1)
  data = aio.receive('light')
  print(f'Received value: {data.value}')
  chat_id=bot.message.chat_id
  path = 'https://etimg.etb2bimg.com/photo/71884644.cms'
  bot.message.reply_text("Light turned ON")
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def demo5(bot,update):
  aio.send('light', 0)
  data = aio.receive('light')
  print(f'Received value: {data.value}')
  chat_id=bot.message.chat_id
  path = 'https://image.shutterstock.com/image-photo/light-bulb-turned-off-over-260nw-162882104.jpg'
  bot.message.reply_text("Light turned OFF")
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def demo6(bot,update):
  aio.send('fan', 1)
  data = aio.receive('fan')
  print(f'Received value: {data.value}')
  chat_id=bot.message.chat_id
  path = 'https://ak.picdn.net/shutterstock/videos/10251269/thumb/1.jpg'
  bot.message.reply_text("Fan turned ON")
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def demo7(bot,update):
  aio.send('fan', 0)
  data = aio.receive('fan')
  print(f'Received value: {data.value}')
  chat_id=bot.message.chat_id
  path = 'https://image.shutterstock.com/image-photo/portable-switched-off-table-fan-260nw-1739277872.jpg'
  bot.message.reply_text("Fan turned OFF")
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def func1(bot,update):
  a = bot.message.text.lower()
  print(a)
  if a=="how are you?":
    demo1(bot,update)
  elif a=="i have completed my major project":
    demo2(bot,update)
  elif a=="what is your name?":
    demo3(bot,update)
  elif a=="turn light on":
    demo4(bot,update)
  elif a=="turn light off":
    demo5(bot,update) 
  elif a=="turn fan on":
    demo6(bot,update)
  elif a=="turn fan off":
    demo7(bot,update)  
  else:
    bot.message.reply_text("Invalid Text")

u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,func1))
u.start_polling()
u.idle()
