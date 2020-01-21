import os, discord
from dotenv import load_dotenv
from discord.ext import commands

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
        message.content = bot_name + '_'.join(split_content[1:])
    # if maid.user.mentioned_in(message) and 'whoareyou' in str(message.content).lower().replace(' ', ''):
    #     await message.channel.send(' I am a maid!')
    await maid.process_commands(message)


# the current time
@maid.command()
async def now(ctx: commands.Context):
    await ctx.send('I has just been born and the concept of a fourth time dimension is unimaginable to me!')


# the help command
maid.remove_command('help')


@maid.command()
async def help(ctx):
    now_help = "**now**:   display the current time of everyone"
    await ctx.send(now_help)


maid.run(token)
