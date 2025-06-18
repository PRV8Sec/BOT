from aiogram.types import Message
from aiogram.filters import BaseFilter


class FilterChatType(BaseFilter):
    async def __call__(self, event: Message) -> bool:
        if event.chat.type == 'group' or event.chat.type == 'supergroup':
            return True
        else:
            await event.answer('This bot is intended for groups only.\n\nBot Developer: @PRV8x')
            return False


class FilterChatAdmin(BaseFilter):
    async def __call__(self, event: Message) -> bool:
        if event.from_user.id in event.chat.get_administrators():
            return False
        else:
            return True


class FilterSenderAnonim(BaseFilter):
    async def __call__(self, event: Message) -> bool:
        if event.sender_chat is not None:
            if event.chat.id == event.sender_chat.id:
                return False
            elif event.sender_chat.type in ('channel', 'group', 'supergroup'):
                print('Message sent on behalf of a channel or chat: ' + str(event.sender_chat.id) + ' '
                      + str(event.sender_chat.type) + ' @' + str(event.sender_chat.username))
                await event.bot.delete_message(event.chat.id, event.message_id)
                return False
        else:
            return True
