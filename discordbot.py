from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

ohayo = ['おはようございます', 'ふふ、もう昼ですよ', 'おはようございます、お寝坊さんですね', 'おはようございます。朝食はもう取りましたか？', 'おはようございます、今日も一緒に頑張りましょうね']
errorsMessages = ['すみません、理解できません', 'おやおや、何かお忘れでは？']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(random.choice(errorsMessages) \n error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')



@bot.command()
async def おはよう(ctx):
    await ctx.send(random.choice(ohayo))
                   
                   
bot.run(token)
