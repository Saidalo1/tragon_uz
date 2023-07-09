import asyncio

from root.settings import bot, chat_id


def send_notification(name, phone, source, selected_services):
    # Send message on telegram
    message_text = '        🛒 New purchase        \n' \
                   '👤 Name: {}\n' \
                   '☎️ Phone: {}\n' \
                   '🏭 Source: \n'.format(name, phone, source)
    services_list = ', '.join(map(str, selected_services))
    message_text += f'📦 Services: {services_list}\n'

    bot.send_message(chat_id, message_text)
