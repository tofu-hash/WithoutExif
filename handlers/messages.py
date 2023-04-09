from handlers.init import *
from aiogram.types import Message
from utils.image_processing import remove_exif


async def start_cmd_handler(msg: Message):
    answer = ('🧑‍💻 Отправь мне фото, и я удалю '
              'все скрытые данные в нём.\n\n'
              '💠 *Просто. Быстро. Безопасно.*\n\n'
              '🖼 Если ты отправляешь фото без '
              'сжатия, то ты можешь получить '
              'его в качестве документа, добавив '
              'к нему подпись */doc*.')

    await msg.answer_sticker(sticker='CAACAgIAAxkBAAMKZCqF8NxyEdlQYjNX0uQ-kMCKBRsAAvINAAK7fWBIH8H7_ft7nyovBA')
    await msg.answer(text=answer, parse_mode='markdown')


async def remove_exif_handler(msg: Message):
    await msg.answer(text='🖼 Обрабатываю изображение')

    if msg.document or msg.photo:
        file_format = 'jpeg'

        if msg.document:
            file_format = msg.document.file_name.split('.')[-1]
            path = 'source/service/WithoutExifImage.' + file_format
            await msg.document.download(destination_file=path)

        elif msg.photo:
            path = 'source/service/WithoutExifImage.%s' % file_format
            await msg.photo[-1].download(destination_file=path)

        photo = open('source/service/WithoutExifImage.%s' % file_format, 'rb')

        exif = remove_exif(file_format=file_format)

        if exif:
            exif = '\n'.join(['• *%s:* `%s`' % (_, exif[_]) for _ in exif])
            answers = ['💠 EXIF данные:\n' + exif]
        else:
            answers = ['💠 EXIF данные отсутствуют.']

        if len(answers) > 1500:
            answers = [answers[:1500], answers[1500:]]

        await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id + 1)

        for answer in answers:
            await msg.answer(text=answer, parse_mode='markdown')

        if msg.caption == '/doc':
            await msg.answer_document(document=photo)
        else:
            await msg.answer_photo(photo=photo)


async def help_cmd_handler(msg: Message):
    answer = ('🧑‍💻 Отправь мне фото, '
              'и я удалю все скрытые данные из него.\n\n'
              '💠 *Бот не хранит никаких данных о пользователях, '
              'включая сохранение информации об идентификаторе '
              'пользователя и данных его профиля.*')
    await msg.answer(answer, parse_mode='markdown')
