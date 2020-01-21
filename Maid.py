import os, discord
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime
import Constants
import pytz
from Utilities import right_padding
import json

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
name = os.getenv('DISCORD_BOT_NAME')
bot_name = '<@!668950009831489536>'
maid: commands.Bot = commands.Bot(['<@!668950009831489536>', '$'])


@maid.event
async def on_ready():
    print(f'{maid.user} has connected to Discord!')
    print(maid.guilds)
    for guild in maid.guilds:
        print(f'{guild.name}')


@maid.event
async def on_message(message: discord.Message):
    # strip the bot name from the message
    if len(message.content.split()) > 1:
        split_content = message.content.split()
        # reassemble the command with _ and bot mention
        message.content = bot_name + ' '.join(split_content[1:])
        # get all of the params

    # if maid.user.mentioned_in(message) and 'whoareyou' in str(message.content).lower().replace(' ', ''):
    #     await message.channel.send(' I am a maid!')
    await maid.process_commands(message)


# the current time
@maid.command()
async def now(ctx: commands.Context):
    # set time zone of people
    tz_london = pytz.timezone('Europe/London')
    tz_us_east = pytz.timezone('US/Eastern')
    tz_us_west = pytz.timezone('US/Pacific')
    tz_vn = pytz.timezone('Asia/Ho_Chi_Minh')
    now_london = datetime.now(tz_london)
    now_us_east = datetime.now(tz_us_east)
    now_us_west = datetime.now(tz_us_west)
    now_vn = datetime.now(tz_vn)

    # print a pretty table
    def pretty_print(who, when):
        #
        hour = when.hour
        am_pm_icon = '          :sun_with_face:' if 8 < hour < 23 else '          :full_moon:'

        return right_padding(f'**{who}**') + when.strftime("%I:%M %p") + am_pm_icon + '\n'

    message = pretty_print('Hang', now_london) + pretty_print('Khoi', now_vn) + pretty_print('Phuong',
                                                                                             now_vn) + pretty_print(
        'Trung', now_us_east) + pretty_print('Khai', now_us_west) + pretty_print('Son', now_us_west)

    await ctx.send(message)


@maid.command()
async def relationship(ctx: commands.Context):
    # set time zone of people
    with open('SimpleDB/relationships.json', 'r') as f:
        relationships = json.load(f)
    message = ' '.join([right_padding(f'**{person}**') + relationships[person] + '\n' for person in
                        relationships])
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
async def help(ctx):
    now_help = f"**{right_padding('now')}**:   display the current time of everyone \n"
    relationship_help = f"**{right_padding('relationship')}**:   display the relationship statuses of everyone\n"
    update_relationship_help = f"{right_padding('**update_relationship**  *person*  *status*')}: update the relationship of a person [ for example: update_relationship Khai taken']"
    message = now_help + relationship_help + update_relationship_help
    await ctx.send(message)


maid.run(token)
