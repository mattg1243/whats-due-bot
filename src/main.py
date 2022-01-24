from canvasapi import Canvas
from datetime import date, time, datetime, timedelta
from dotenv import load_dotenv, find_dotenv
import discord
import os
import random

# load env variables
load_dotenv(find_dotenv())
API_URL = os.environ.get('API_URL')
API_TOKEN = os.environ.get('API_TOKEN')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
GUILD = os.environ.get('SERVER')
CLASS_NUMBER = os.environ.get('CALC1')
# create instance of Canvas object to gain access to the API
canvas = Canvas(API_URL, API_TOKEN)
# get the whole calculus class object
course = canvas.get_course(CLASS_NUMBER)
print(course.name)
# create the empty response arrary
assignments_response = []
# assemble a list of all assignments
assignments = course.get_assignments()
for a in assignments:
    assignments_response.append(a)
# date logic
today = date.today()
nextWeek = today + timedelta(days=7)
# test output for bot response
format_str = "%a %b %d"
response_msg = "What's due in the next 7 days:"
for a in assignments_response:
    if date.fromisoformat(a.due_at.split("T")[0]) <= nextWeek:
        due_date = date.fromisoformat(a.due_at.split("T")[0]).strftime(format_str)
        response_msg += f"\n{a.name} due {due_date}"

# bot logic
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )

@client.event
async def on_message(message):
    if '/whatsdue' in message.content.lower():
        await message.channel.send(response_msg)

client.run(BOT_TOKEN)