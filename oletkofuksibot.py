import time
import requests

from secret import tg_token

def getUpdates(offset):
    url = 'https://api.telegram.org/bot%s/getUpdates?offset=%d' % (tg_token, offset)
    response = requests.get(url).json()
    return response['result']

def sendMessage(chat_id, text):
    url = 'https://api.telegram.org/bot%s/sendMessage' % tg_token
    data = {'chat_id': chat_id, 'text': text}
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
                sendMessage(chat_id, 'Fuksibotti?')
            else:
                sendMessage(chat_id, 'Fuksi?')

    print (updates)
    time.sleep(1)
