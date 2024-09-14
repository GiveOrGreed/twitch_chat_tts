# Twitch Chat TTS
A python script that reads twitch chat aloud using TTS. Bad words are censored before reading.

## SETUP
1. Run `pip install -r requirements.txt` to install all modules
2. If you don't already have a Twitch OAuth Token, get one here: https://twitchtokengenerator.com/
3. Create a `.env` file using the lines below, replacing the values with your own:
```python
TWITCH_OAUTH_TOKEN=<your twitch oauth token>
TWITCH_CHANNEL=<your twitch channel>
```

## USAGE
1. Run `python main.py`