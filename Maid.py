import json
import os
from datetime import datetime

import pytz
from discord.ext import commands
from dotenv import load_dotenv

from Utilities import right_padding, to_monospace, move_feature_log, get_feature_type
from weather import get_weather_data_of_city_with_id
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
        #
        hour = when.hour
        am_pm_icon = '☀' if 8 < hour < 23 else '☪'
        who = to_monospace(who)
        when = to_monospace(when.strftime("%I:%M %p"))
        # calculate the size of the text
        return f'**{right_padding(who)}**' + f'{right_padding(when, 90)}' + am_pm_icon

    with open('SimpleDB/timezones.json', 'r') as f:
        timezones = json.load(f)
        message = '\n'.join(
            [pretty_print(person, datetime.now(pytz.timezone(timezones[person]))) for person in timezones])
    await ctx.send(message)


@maid.command()
async def relationship(ctx: commands.Context):
    # set time zone of people
    with open('SimpleDB/relationships.json', 'r') as f:
        relationships = json.load(f)
    message = '\n'.join(
        [f'**{right_padding(to_monospace(person))}**' + relationships[person] for person in
         relationships])
    await ctx.send(message)


@maid.command()
async def weather(ctx: commands.Context, who='all'):
    # set time zone of people
    with open('SimpleDB/weather.json', 'r') as f:
        locations = json.load(f)
    message = '\n'.join(
        [f'**{right_padding(to_monospace(person))}**' + get_weather_data_of_city_with_id(
            locations[person]) for person in
         locations])
    await ctx.send(message)


@maid.command()
async def update_relationship(ctx: commands.Context, person, status):
    with open('SimpleDB/relationships.json', 'r') as f:
        relationships = json.load(f)

    if person in relationships:
        relationships[person] = status
    #     save it
    with open('SimpleDB/relationships.json', 'w') as f:
        json.dump(relationships, f)
    #  print the relationships again
    message = ' '.join(
        [right_padding(f'**{person}**') + relationships[person] + '\n' for person in relationships])
    await ctx.send(message)


maid.remove_command('help')


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


@maid.command()
async def completed_features(ctx):
    response = get_feature_type(FeatureTypes.COMPLETED.value)
    await ctx.send(response)


@maid.command()
async def developing_features(ctx):
    response = get_feature_type(FeatureTypes.DEVELOPING.value)
    await ctx.send(response)


@maid.command()
async def working_on_feature(ctx, index: int):
    response = move_feature_log(FeatureTypes.REQUESTED.value, FeatureTypes.DEVELOPING.value, index)
    await ctx.send(response)


@maid.command()
async def complete_feature(ctx, index: int):
    response = move_feature_log(FeatureTypes.DEVELOPING.value, FeatureTypes.COMPLETED.value, index)
    await ctx.send(response)


@maid.command()
async def help(ctx):
    now_help = f"**{right_padding('now')}**:   display the current time of everyone \n"
    relationship_help = f"**{right_padding('relationship')}**:   display the relationship statuses of everyone\n"
    update_relationship_help = f"{right_padding('**update_relationship**  *person*  *status*')}: " \
                               f"update the relationship of a person [ for example: update_relationship Khai taken']"
    message = now_help + relationship_help + update_relationship_help
    await ctx.send(message)


if __name__ == '__main__':
    maid.run(token)
