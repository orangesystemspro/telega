import asyncio
import time
import random
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, InputPeerUser
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
api_id= 335045
api_hash = 'e3c4755fca54638ebb3a5412e77fefec'


def sendMessageToUser():

    client = TelegramClient("+380501013489", api_id=api_id, api_hash=api_hash)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request("+380501013489")
        client.sign_in("+380501013489", input("enter code : "))
    f = open("resultUSERNAME.txt", "r")
    for lines in f:
        rand = random.randint(0,8) 
        client.send_message(lines, msg[rand])
        time.sleep(30)

sendMessageToUser()