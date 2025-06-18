import asyncio
from environs import Env
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from collections import defaultdict


async def delete_start_func(message: Message):
    if not await user_is_subscriber(message.bot, message.from_user.id, Env().str("CHANNEL_ID")):
        await AlbumHandler().check_album_and_send(message)


async def user_is_subscriber(bot, user_id: int, channel_id: str) -> bool:
    try:
        member_status = await bot.get_chat_member(channel_id, user_id)
        return member_status.status not in ["left", "kicked"]
    except Exception as e:
        print(f"Error checking subscription status: {e}")
        return False


class AlbumHandler:
    def __init__(self):
        self.album_end_tracker = defaultdict(list)
        self.album_locks = defaultdict(asyncio.Lock)

    async def check_album_and_send(self, message: Message):
        if message.media_group_id:
            self.album_end_tracker[message.media_group_id].append(message.message_id)

            async with self.album_locks[message.media_group_id]:
                await asyncio.sleep(4)
                if self.album_end_tracker[message.media_group_id][-1] == message.message_id:

                    for msg_id in self.album_end_tracker[message.media_group_id]:
                        await message.bot.delete_message(message.chat.id, msg_id)
                    del self.album_end_tracker[message.media_group_id]
                    del self.album_locks[message.media_group_id]
                    await answer_message(message)
        else:
            await message.delete()
            await answer_message(message)


async def first_name(message: Message):
    if message.from_user.first_name or message.from_user.full_name or message.from_user.username is not None:
        return (message.from_user.first_name + ',' or message.from_user.full_name + ','
                or message.from_user.username + ',')
    else:
        return 'Dear user!'


async def answer_message(message: Message):
    send_answer = await message.answer(
        '<a href="tg://user?id=' + str(message.from_user.id) + '">' + str(await first_name(message)) + '</a>' +
        "\nPlease subscribe to the channel to be able to send messages in this chat.",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
            text="Subscribe to the channel", url=Env().str("INVITE_LINK"))]]))
    await asyncio.sleep(180)  # Wait for 3 minutes, then delete the message to avoid spam
    await send_answer.delete()
