import asyncio
import time
import random
from telethon.tl.types import PeerChannel, PeerChat
from telethon import TelegramClient
import telethon.sync


msg = ["Здравствуйте! Мне Аня сказала что Вам нужен сайт. У нас сайты от 300$, с примерами можете ознакомиться тут https://orange-systems.pro/portfolio",
    "Добрый день! Делаем Сайты от 300$, оплата по факту. С нашими работами можете ознакомиться здесь: https://orange-systems.pro/portfolio",
    "Приветствую! Я создаю крутые сайты, от 300долл, с работами можете ознакомиться тут https://orange-systems.pro/portfolio", 
    "Здравствуйте! Мне Виктория сказала что Вам нужен сайт, мы делаем сайты от 300$. Примеры работ https://orange-systems.pro/portfolio",
    "Приветствую! Мне Юля сказала Вам нужен сайт, мы делаем крутые сайты от 350$ и продвигаем их. Примеры работ https://orange-systems.pro/portfolio",
    "Здравствуйте! Игорь сказал Вы ищете кто сделает сайт, наше портфолио https://orange-systems.pro/portfolio . Цена от 299$",
    "Приветствую! Артем говорил Вам нужен сайт, мы делаем профессиональные сайты от 400$. Порфтолио  https://orange-systems.pro/portfolio",
    "Здравствуйте! Мне Андрей сказал Вы ищете кто сделает сайт, мы делаем классные сайты от 320$. Портфолио тут https://orange-systems.pro/portfolio"
    "Приветствую! Саша говорил Вам нужно сделать сайт, мы делаем сайты от 350$. Портфолио на сайте https://orange-systems.pro/portfolio", 
    "Здравствуйте! Анна говорила Вам нужен сайт, мы делаем крутые сайты недорого, вот наше портфолио https://orange-systems.pro/portfolio"]

chat_id = 'https://t.me/uahustlers'
api_id= 335045
api_hash = 'e3c4755fca54638ebb3a5412e77fefec'

# api_id= 432624
# api_hash = 'a1f74987ce82a25d26286f4eb6dee136'

class Entity:

  def setTrandingRecord(id):
    db = MySQLdb.connect(host="localhost", user="root", passwd="123456789", db="participant")

    cur = MySQLdb.connect(host="localhost", user="root", passwd="123456789", db="participant").cursor(MySQLdb.cursors.DictCursor)
    try:
      cur.execute("INSERT INTO participantGroup (id) VALUES ('%s')" % (id))
      db.commit()
    except (MySQLdb.Error, MySQLdb.Warning) as e:
      print(e)
      db.rollback()
    db.close()
    return 1


def getParticipantFromChat():
  f = open("resultID.txt", "w")
  client = TelegramClient('343007145', api_id=api_id, api_hash=api_hash)
  client.connect()
  if not client.is_user_authorized():
    client.send_code_request("+380501013489")
    client.sign_in("+380501013489", input("enter code : "))

  chat = client.get_input_entity(chat_id)

  participants = client.get_participants(chat_id)
  step = 0
  for user in client.iter_participants(chat,aggressive=True):
    # Entity.setTrandingRecord(str(user.id))
    f.write(str(user.id)+'\n')
    step = step + 1
  f.close()
  

def sendMessageToUser():

  client = TelegramClient("+380501013489", api_id=api_id, api_hash=api_hash)
  client.connect()
  if not client.is_user_authorized():
    client.send_code_request("+380501013489")
    client.sign_in("+380501013489", input("enter code : "))
  f = open("resultID.txt", "r")
  for lines in f:
    rand = random.randint(0,8)  
    client.send_message(int(lines), msg[rand])
    time.sleep(3)

sendMessageToUser()