import os
from slack import RTMClient
from config import SLACK_BOT_TOKEN

# token = os.environ.get('SLACK_BOT_TOKEN')
token = SLACK_BOT_TOKEN


@RTMClient.run_on(event="message")
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    if 'Hello' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user}>!",
            thread_ts=thread_ts
        )

@RTMClient.run_on(event="open")
def open(**payload):
    print(payload)


@RTMClient.run_on(event="channel_joined")
def open(**payload):
    print(payload)


# instantiate Slack client
slack_client = RTMClient(token=token)

# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

if __name__ == "__main__":
    slack_client.start()