import time
import requests

from secret import tg_token, from_chat_id, message_id

def getUpdates(offset):
    url = 'https://api.telegram.org/bot%s/getUpdates?offset=%d' % (tg_token, offset)
    response = requests.get(url).json()
    return response['result']

def sendMessage(chat_id, text):
    url = 'https://api.telegram.org/bot%s/sendMessage' % tg_token
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data)

def forwardMessage(to_chat_id, from_chat_id, message_id):
    url = 'https://api.telegram.org/bot%s/forwardMessage' % tg_token
    data = {'chat_id': to_chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id}
    requests.post(url, data)

lastUpdateId = 0
while True:
    updates = getUpdates(lastUpdateId + 1)
    for update in updates:
        lastUpdateId = update['update_id']
        message = update.get('message', {})
        chat_id = message.get('chat', {}).get('id')
        new_members = message.get('new_chat_members', [])

        for new_member in new_members:
            if new_member.get('is_bot') == True:
                forwardMessage(chat_id, from_chat_id, message_id)
            else:
                forwardMessage(chat_id, from_chat_id, message_id)

    print (updates)
    time.sleep(1)
