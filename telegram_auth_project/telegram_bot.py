
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

TELEGRAM_BOT_TOKEN = '7656557494:AAGU4BMCZg9I3iLhVSP01Q9tUz4oipDy1Go'
DJANGO_SERVER_URL = 'http://127.0.0.1:8000'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    token = context.args[0]
    response = requests.post(f'{DJANGO_SERVER_URL}/auth/', data={'telegram_id': user.id, 'token': token})
    print(f'Sent auth request with telegram_id: {user.id}, token: {token}, response status: {response.status_code}')  # Отладочное сообщение
    if response.status_code == 200:
        await update.message.reply_text(f'Привет, {user.first_name}! Вы успешно авторизованы.')
    else:
        await update.message.reply_text('Произошла ошибка при авторизации. Попробуйте снова.')

def main() -> None:
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
