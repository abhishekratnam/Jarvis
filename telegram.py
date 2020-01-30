import config
import requests

url = "https://api.telegram.org/" + config.telegram_bot_id + "/"
print(url)
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]
def getchat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id
update = last_update(url)
print(update)
print(getchat_id(update))
def get_msg_text(update):
    message_text = update['message']['text']
    return message_text
print(get_msg_text(update))
def send_message(chat_id,message_text):
    params = {"chat_id":chat_id, "text":message_text}
    response = requests.post(url + "sendMessage",data = params)
    return response

def message():
    while True:
        update_id = last_update(url)["update_id"]
        update = last_update(url)
        if update_id == update["update_id"]:
            i = get_msg_text(update).lower()
            return i
            update_id += 1
def send(message):
    update = last_update(url)
    chat_id = getchat_id(update)
    send_message(chat_id,message)