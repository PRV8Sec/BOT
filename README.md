# Bot Subscribe Telegram
A Telegram bot that requires users to subscribe to a channel in order to send messages in a group.

### Features:
- Add a channel/group that users must subscribe to.

- Supports invite links to private groups/channels.

- Group administrators can send messages without being subscribed.

- Deletes messages from users who are not subscribed to the channel.

- Deletes messages sent on behalf of a channel/chat.

- Handles albums if a user sends multiple media messages.

### Installation and Setup

> [!IMPORTANT]
❗ Required Python version: 3.11.

1. Navigate to the project folder:

cd Bot-Subscribe-Telegram

2. Install dependencies:

pip3 install -r requirements.txt

## Configuration:

1. Create a bot via @BotFather and get the token.

2. Open the file named input and enter the required data:

- TOKEN= (Your bot's token, obtained from @BotFather)

- ADM_ID= (Bot administrator ID to receive notifications)

- CHANNEL_ID= (The channel/group ID that users must subscribe to)

- INVITE_LINK= (Invitation link to the channel/group, public or private, starting with t.me/)

3. Add the bot to the channel that users need to subscribe to.

4. Add the bot to the group where it will monitor and delete messages from unsubscribed users.

# Running the Bot

-
run main.py

-
python3 main.py
