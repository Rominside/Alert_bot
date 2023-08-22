import json
from aiogram import Bot


async def main(title, msg):
    with open('config.json') as file:
        templates = json.loads(file.read())
    bot = Bot(token=templates["token"])
    print(title)
    # создаем новую тему, если таковой ещё нет
    if title not in templates["topics"]:
        topic_info = await bot.create_forum_topic(chat_id=templates["chat_id"], name=title)
        templates["topics"][title] = topic_info["message_thread_id"]
        with open('config.json', 'w') as file:
            file.write(json.dumps(templates))

    # отправляем сообщение в соответствующий топик
    await bot.send_message(chat_id=templates["chat_id"], text=msg, parse_mode="HTML",
                           message_thread_id=templates["topics"][title])
    await bot.close()

if __name__ == '__main__':
    pass
