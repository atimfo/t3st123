import urllib.request
import requests
import time

_flag = True

def telegram_send_msg(text: str):
    token = "6258019496:AAHgCwSdQ9ATKfwrMNhse8vg7Zt1fBaEIUA"
    url = "https://api.telegram.org/bot"
    channel_id = "@sofaavibe"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        raise Exception("post_text error")

while True:
    page = urllib.request.urlopen('https://fipi.ru/ege/demoversii-specifikacii-kodifikatory').read().decode('utf-8')
    if "2024 года" in page and _flag:
        print('Демка вышла!!!')
        telegram_send_msg('Кажется Демоверсия 2024 вышла!!! проверяй – https://clck.ru/NDBxt')
        _flag = False
        break
    else:
        print("–")
    time.sleep(20)
