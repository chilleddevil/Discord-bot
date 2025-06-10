import discord
import random
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

roasts = [
    "I'd explain it to you, but I don't have any crayons.",
    "You have the right to remain silent because whatever you say will probably be stupid anyway.",
    "If I wanted to kill myself, I'd climb your ego and jump to your IQ.",
    "You bring everyone so much joy… when you leave the room.",
    "I’d agree with you, but then we’d both be wrong.",
    "If I wanted a joke, I’d just look at your life choices.",
    "You’re as useless as the ‘ueue’ in ‘queue’.",
    "Somewhere out there is a tree tirelessly producing oxygen for you. You owe it an apology.",
    "I’m not saying you’re dumb, but you have bad luck thinking.",
    "Your secrets are always safe with me. I never even listen when you tell me them.",
    "If laughter is the best medicine, your face must be curing the world.",
    "You're the reason the gene pool needs a lifeguard.",
    "Light travels faster than sound, which is why you seemed bright until you spoke.",
    "If ignorance is bliss, you must be the happiest person alive.",
    "You have the charm and personality of a dial-up modem.",
    "I would roast you, but I’m afraid you’d catch fire and ruin the barbecue.",
    "You’re as sharp as a marble.",
    "You have the emotional range of a teaspoon.",
    "You are the human equivalent of a participation trophy.",
    "If I wanted to hear from someone with no brains, I’d talk to a mirror."
]

dark_facts = [
    "Did you know? More people are bitten by New Yorkers each year than by sharks.",
    "The average person walks past 36 murderers in their lifetime.",
    "There are more vacant houses than homeless people in the US.",
    "There are thousands of bodies on Mount Everest, used as waypoints for climbers.",
    "Some tumors can grow hair, teeth, bones, and even eyes.",
    "The air you breathe in a subway is 15% human skin.",
    "You shed about 40 pounds of skin in your lifetime.",
    "There are more possible iterations of a game of chess than there are atoms in the known universe.",
    "A human head remains conscious for about 20 seconds after being decapitated.",
    "Rats multiply so quickly that in 18 months, two rats could have over a million descendants.",
    "If the sun exploded, you wouldn’t know for 8 minutes.",
    "There are millions of microscopic mites living on your face right now.",
    "Some fish eat their own babies.",
    "The last sense to go when you die is hearing.",
    "There are lakes underneath Antarctica that have been cut off from the world for millions of years.",
    "The world’s quietest room is so silent you can hear your own blood flowing.",
    "If you die alone at home, your pet might try to eat you to survive.",
    "Your skeleton is wet.",
    "Cockroaches can live for weeks without their heads before dying of starvation.",
    "You’re always only a few minutes away from a spider."
]

memes_api = "https://meme-api.com/gimme"

# Rule-based responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm doing well, thanks!", "I'm good!", "All good here!"],
    "what's up": ["Not much!", "Just chilling.", "Looking at memes."],
    "goodbye": ["Bye!", "See you later!", "Goodbye!"]
}

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()

    # Auto-talking logic
    for trigger, bot_responses in responses.items():
        if trigger in content:
            await message.channel.send(random.choice(bot_responses))
            return  # Stop after finding the first match

    if content.startswith('!meme'):
        try:
            response = requests.get(memes_api)
            data = response.json()
            meme_url = data.get('url')
            if meme_url:
                await message.channel.send(meme_url)
            else:
                await message.channel.send("Couldn't fetch a meme right now.")
        except Exception:
            await message.channel.send("Error fetching meme.")

    elif content.startswith('!roast'):
        roast = random.choice(roasts)
        await message.channel.send(roast)

    elif content.startswith('!darkfact'):
        fact = random.choice(dark_facts)
        await message.channel.send(fact)

client.run(TOKEN)
