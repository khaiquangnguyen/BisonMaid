import json
import os
from datetime import datetime

import pytz
from discord import Embed
from discord.ext import commands
from dotenv import load_dotenv

from Utilities import right_padding, to_monospace, move_feature_log, get_feature_type, to_markdown
from weather import get_weather_of_city_id
from Constants import FeatureTypes

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
name = os.getenv('DISCORD_BOT_NAME')
bot_name = '<@!668950009831489536>'
maid: commands.Bot = commands.Bot(['$'])


@maid.event
async def on_ready():
    print(f'{maid.user} has connected to Discord!')
    print(maid.guilds)
    for guild in maid.guilds:
        print(f'{guild.name}')


# @maid.event
# async def on_message(message: discord.Message):
#     # strip the bot name from the message
#     if len(message.content.split()) > 1:
#         split_content = message.content.split()
#         # reassemble the command with _ and bot mention
#         message.content = bot_name + ' '.join(split_content[1:])
#         # get all of the params
#
#     # if maid.user.mentioned_in(message) and 'whoareyou' in str(message.content).lower().replace(' ', ''):
#     #     await message.channel.send(' I am a maid!')
#     await maid.process_commands(message)
#

# the current time
@maid.command()
async def now(ctx: commands.Context):
    def pretty_print(who, when):
        hour = when.hour
        am_pm_icon = ':sun_with_face: ' if 8 < hour < 23 else '☪'
        who = to_monospace(who)
        when = to_monospace(when.strftime("%I:%M %p"))
        # calculate the size of the text
        return f'**{right_padding(who)}**' + f'{right_padding(when, 90)}' + am_pm_icon

    with open('SimpleDB/timezones.json', 'r') as f:
        embed = Embed(title="Time", description=":alarm_clock: If I could save time in a bottle :alarm_clock: ",
                      color=0x00ff00)
        timezones = json.load(f)
        for person in timezones:
            time_data = datetime.now(pytz.timezone(timezones[person]))
            am_pm_icon = '☀' if 8 < time_data.hour < 23 else '☪'
            time_data = time_data.strftime("%I:%M %p")
            time_data = f'{time_data:12}{am_pm_icon}'
            embed.add_field(name=f'{person}', value=to_markdown(time_data), inline=False)
    await ctx.send(embed=embed)


@maid.command()
async def weather(ctx: commands.Context, who='all'):
    # set time zone of people
    embed = Embed(title="Weather", description=":musical_note: Weathering with you :musical_note: ", color=0x00ff00)
    with open('SimpleDB/weather.json', 'r') as f:
        locations = json.load(f)
        for person in locations:
            weather_data = get_weather_of_city_id(locations[person])
            embed.add_field(name=f'**{person}**', value=to_markdown(weather_data), inline=False)
    await ctx.send(embed=embed)


@maid.command()
async def vidcall(ctx):
    await ctx.send('https://meet.google.com/kvh-xfkw-ymo')


@maid.command()
async def request_feature(ctx, feature: str):
    with open('SimpleDB/features.json', 'r') as f:
        all_features = json.load(f)
        requested = all_features.get(FeatureTypes.REQUESTED.value, [])
        time_stamp = datetime.timestamp(datetime.now())
        requested.append({'feature': feature, 'time_stamp': time_stamp})
        all_features[FeatureTypes.REQUESTED.value] = requested
    with open('SimpleDB/features.json', 'w') as f:
        json.dump(all_features, f)
    await ctx.send('The requested feature has been added to feature list. ')


@maid.command()
async def requested_features(ctx):
    response = get_feature_type(FeatureTypes.REQUESTED.value)
    await ctx.send(response)


maid.remove_command('help')


@maid.command()
async def help(ctx):
    embed = Embed(title="Help", description="A list of all commands", color=0xffffff)
    all_commands = {
        'now': 'display the current time of everyone',
        'requested_features': "list all current requested features",
        'request_feature  "feature"': "add a feature to the list of requested features",
        'weather': 'show the current weather of everyone'
    }
    for command in all_commands:
        embed.add_field(name=f'{command}', value=to_markdown(all_commands[command]), inline=False)
    await ctx.send(embed=embed)


if __name__ == '__main__':
    maid.run(token)
