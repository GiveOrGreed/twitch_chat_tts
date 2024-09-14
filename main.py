import pyttsx3
from better_profanity import profanity
from twitchio.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get OAuth Token and Channel Name from .env
OAUTH_TOKEN = os.getenv('TWITCH_OAUTH_TOKEN')  # https://twitchtokengenerator.com/
CHANNEL = os.getenv('TWITCH_CHANNEL')

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Load the profanity filter with default word list
profanity.load_censor_words()

# Twitch Bot
class Bot(commands.Bot):
    def __init__(self):
        # Use the environment variables for token and channel
        super().__init__(token=OAUTH_TOKEN, prefix='!', initial_channels=[CHANNEL])

    async def event_ready(self):
        print(f'Logged in as {self.nick}')
        print(f'Connected to chat!')

    async def event_message(self, message):
        # Don't respond to our own messages (comment this logic out for testing)
        if message.author.name.lower() == self.nick.lower():
            return

        # Censor message for any bad words (will be replaced with ****)
        censored_text = profanity.censor(message.content)

        # Read the censored message out loud
        print(f'Reading message by {message.author.display_name}: {censored_text}')
        engine.say(f"{message.author.display_name} said: {censored_text}")
        engine.runAndWait()

# Main entry point
if __name__ == "__main__":
    bot = Bot()
    bot.run()