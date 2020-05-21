from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
@bot.command()
async def おはよう(ctx):
    ohayo = ['おはようございます', 'ふふ、もう昼ですよ', 'おはようございます、お寝坊さんですね', 'おはようございます。朝食はもう取りましたか？', 'おはようございます、今日も一緒に頑張りましょうね']
    ohayoFinal = random.choice(ohayo)
    await ctx.send(ohayoFinal)
    
@bot.command()
async def おやすみ(ctx):
    oyasumi = ['おやすみなさい', 'はい、いい夢を', 'もう寝てしまうのですか……', '子守歌でも歌いましょうか？……ふふ、冗談ですよ']
    oyasumiFinal = random.choice(oyasumi)
    await ctx.send(oyasumiFinal)
    
@bot.command()
async def つかれた(ctx):
    tukareta = ['御冗談を、まだいけるでしょう？', 'おやおや、ひとまずお茶でも飲みましょうか', '本気で言ってます？']
    tukaretaFinal = random.choice(tukareta)
    await ctx.send(tukareFinal)
                   
bot.run(token)
