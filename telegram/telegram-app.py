from telethon import TelegramClient
from datetime import timezone, timedelta, datetime
from time import sleep
from api import *
import ktrain

# load model
classifier = ktrain.load_predictor('../models/distilbert')

# define functions to get and send messages
async def get_messages():
    # get AmplifyUkraine messages from last hour 
    global api_id
    global api_hash
    messages = []
    async with TelegramClient(api_id=api_id, api_hash=api_hash, session='this') as client:
        async for message in client.iter_messages('AmplifyUkraine', offset_date=datetime.now(tz=timezone.utc) - timedelta(hours=12), reverse=True):
            messages.append(message)
    return messages

async def post_messages(messages):
    # iteratively post messages to the given channel
    global api_id
    global api_hash
    channel = -1002040681043 # update this var to change channel
    async with TelegramClient(api_id=api_id, api_hash=api_hash, session='this') as client:
        for message in messages:
            await client.send_message(entity=channel, message=message.text)

async def post_report(report):
    # post message of program logs
    global api_id
    global api_hash
    channel = -1002040681043 # update this to private report channel
    async with TelegramClient(api_id=api_id, api_hash=api_hash, session='this') as client:
        await client.send_message(entity=channel, message=report) # update entity to report channel


# define function to classify messages with model
def find_combats(messages):
    # iteratively predicts messages
    # does NOT currently clean/pre-process the message
    # this func should be improved
    global classifier
    combats = []
    for message in messages:
        if classifier.predict(message.text) == 'annotation':
            combats.append(message)
    return combats

async def main():
    while True:
        report = {'time': datetime.now(),'num_messages': 0, 'num_combats': 0, 'errors': []}

        try:
            messages = await get_messages()
            num_messages = len(messages)
            report['num_messages'] = num_messages
        
        
            if num_messages > 0:
                try:
                    combats = find_combats(messages)
                    num_combats = len(combats)
                    report['num_combats'] = num_combats

                    if num_combats > 0:
                        try:
                            await post_messages(combats)
                        except:
                            report['errors'].append('Failed to post messages.')

                except:
                    report['errors'].append('Failed to classify messages')

        except:
            report['errors'].append('Failed to get messages')

        if len(report['errors']) == 0:
            report['errors'].append('None')

        error_string = ''
        for error in report['errors']:
            error_string += error + '\n'

        report_string = f"{report['time']}\nRetrieved {report['num_messages']} new messages. \nFound {report['num_combats']} combat events. \n Errors: {error_string}"

        try:
            await post_report(report_string)
        except:
            pass

        sleep(3600)

if __name__ == "__main__":
    main()
