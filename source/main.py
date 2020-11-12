import signal
import threading
import time

from discord.ext import commands

from bot.quiz_bot import QuizBot
from settings import CONFIG, KEYS


if __name__ == '__main__':

    # Set defaults if they are not present in the config file.
    CONFIG.get_or_set('language', 'en')

    # Check token
    DISCORD_TOKEN = KEYS.get('TOKEN')

    # Setup the bot.
    bot = commands.Bot(command_prefix='!')
    qb = QuizBot(bot)


    # Signal handler for termination from user.
    def signal_handler(sig, frame):
        qb.exit()
        # log('Ctrl+C!')
        exit(0)


    signal.signal(signal.SIGINT, signal_handler)

    # Bot will run in a separate thread.
    t = threading.Thread(target=bot.run, args=[DISCORD_TOKEN], daemon=True)
    t.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            exit(0)
            break
