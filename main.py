# live
from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)


@app.route('/')
def index():
  return '''<body style="margin: 0; padding: 0;">
    <iframe width="100%" height="100%" src="https://myprojectislive.pages.dev" frameborder="0" allowfullscreen></iframe>
  </body>'''


def run():
  app.run(host='0.0.0.0', port=4378)


def keep_alive():
  t = Thread(target=run)
  t.start()


keep_alive()

# import modules
import guilded
import time
import random
from guilded import embed
from guilded.ext import commands

# bot definitions
botprefix = "j!"
bot = commands.Bot(command_prefix=botprefix)
client = guilded.Client()

# bot setup variables
TOKEN = "gapi_nATCehMKKv/ORITvHj0xzVdqqLqNkx6AgAg5/B2WQeHuyJrkANrKSI0ADlpHNXwEhkqj01LspENNCO1VteMp+A=="
footer = "🧃 Juicebox"
muterole = []

# removing commands
bot.remove_command('help')


# bot commands
@bot.event
async def on_ready():
  print(f"Logged in as {bot.user.name} | User Id: {bot.user.id}")
  emoteID = 2212322
  print(len(bot.guilds))
  await bot.set_status(emote=emoteID,
                       content=f"Watching {len(bot.guilds)} servers")


@bot.command()
async def up(ctx):
  if ctx.author.id == "my2epXyA":
    emoteID = 2212322
    await bot.set_status(emote=emoteID,
                         content=f"Watching {len(bot.guilds)} servers")
    author = ctx.author
    embed = guilded.Embed(
        title="Status Update",
        description=f"{author.mention} Bot status updated.",
        color=guilded.Color.green(),
    )
    await ctx.send(embed=embed, private=True)
  else:
    await ctx.send("You don't have permission to use this command.")


@bot.command()
async def offline(ctx):
  if ctx.author.id == "my2epXyA":
    emoteID = 90002583
    await bot.set_status(
        emote=emoteID,
        content=f"Waiting to go back online. Currently offline.")
  else:
    await ctx.send("You don't have permission to use this command.")


@bot.command()
async def help(ctx):
  embed = guilded.Embed(
      title="Bot Commands",
      description=
      "**Moderation**\n setrole \nkick \nban \nmute \nunmute \npurge \n\n**Fun**\n8ball \nrate \ncoinflip \ndice \nrps \nhug \nslap \npunch \nboop \nkiss \ncuddle \nbonk \nwhisper \nquote \n\n**Utility**\navatar \nserverinfo \nuserinfo",
      color=guilded.Color.gold(),
  )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)


@bot.command("8ball")
async def eightball(ctx, *, question=None):
  if question == None:
    embed = guilded.Embed(
        title="Error. Please ask a question",
        description=
        "You did not ask a question. Please use the correct syntax; `a/8ball <question>`",
        color=guilded.Color.red())
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)
  else:
    with open("responses.txt", "r", encoding="utf-8") as f:
      random_response = f.readlines()
    response = random.choice(random_response)
    embed = guilded.Embed(
        title="Magic 8 Ball.",
        description=f"**Question** \n {question} \n **Answer**   \n {response}",
        color=guilded.Color.gold(),
    )
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)


@bot.command()
async def coinflip(ctx):
  flip = random.randint(1, 2)
  if flip == 1:
    response = "Heads"
  else:
    response = "Tails"
  embed = guilded.Embed(
      title="Coin Flip",
      description=f"{ctx.author.mention} flipped a coin and got **{response}**",
      color=guilded.Color.gold(),
  )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)
  print("Command ran! coinflip.")


@bot.command()
async def dice(ctx, minimum, max):
  if int(minimum) > int(max):
    embed = guilded.Embed(
        title="Error",
        description="The minimum number must be less than the maximum number.",
        color=guilded.Color.red(),
    )
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)
    print("[ERROR HAPPENED ]Command ran! dice.")
  else:
    response = str(random.randrange(int(minimum), int(max)))
    embed = guilded.Embed(
        title="Dice Roll",
        description=
        f"{ctx.author.mention} rolled a dice and got **{response}**",
        color=guilded.Color.gold(),
    )
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)
    print("Command ran! dice.")


@bot.command()
async def hug(ctx, member: guilded.Member):
  embed = guilded.Embed(
      title=f"{ctx.author.mention} hugs {member.mention}",
      description=f"{ctx.author.mention} has hugged {member.mention}",
      color=guilded.Color.gold(),
  )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)


@bot.command()
async def slap(ctx, member: guilded.Member):
  embed = guilded.Embed(
      title=f"{ctx.author.mention} slaps {member.mention}",
      description=f"{ctx.author.mention} has slapped {member.mention}",
      color=guilded.Color.gold(),
  )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)


@bot.command()
async def boop(ctx, member: guilded.Member):
  embed = guilded.Embed(
      title=f"{ctx.author.mention} boops {member.mention}",
      description=f"{ctx.author.mention} has booped {member.mention}",
      color=guilded.Color.gold(),
  )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)


@bot.command()
async def punch(ctx, member: guilded.Member):
  embed = guilded.Embed(
      title=f"{ctx.author.mention} punches {member.mention}",
      description=f"{ctx.author.mention} has punched {member.mention}",
      color=guilded.Color.gold(),
  )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)


@bot.command()
async def bonk(ctx, member: guilded.Member):
  embed = guilded.Embed(
      title=f"{ctx.author.mention} bonks {member.mention}",
      description=f"{ctx.author.mention} has bonked {member.mention}",
      color=guilded.Color.gold(),
  )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)


@bot.command()
async def kiss(ctx, member: guilded.Member):
  embed = guilded.Embed(
      title=f"{ctx.author.mention} kisses {member.mention}",
      description=f"{ctx.author.mention} has kissed {member.mention} 😳",
      color=guilded.Color.gold(),
  )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)


@bot.command()
async def cuddle(ctx, member: guilded.Member):
  embed = guilded.Embed(
      title=f"{ctx.author.mention} cuddles {member.mention}",
      description=f"{ctx.author.mention} is cuddling with {member.mention} 😳",
      color=guilded.Color.gold(),
  )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)

# rps is not done and doesnt work. this is a test and hidden command.
@bot.command()
async def rps(ctx, member: guilded.Member):
  embed = guilded.Embed(
      title="Rock, Paper, Scissors",
      description=
      f"{ctx.author.mention} has challenged {member.mention} to a game of rock, paper, scissors.\nSay `accept` to accept or `decline` to decline.",
      color=guilded.Color.gold(),
  )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)
  if member.send("accept"):
    print("Accepted.")
  else:
    print("Declined")


@bot.command()
async def test(ctx):
  embed = guilded.Embed(
      title="Test",
      description=f"The bot is online.",
      color=guilded.Color.green(),
  )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)


@bot.command()
async def serverinfo(ctx):
  serverid = ctx.guild.id
  server = ctx.guild
  serverowner = ctx.guild.owner
  if server.verified:
    serververified = "Server is verified."
  else:
    serververified = "Server is not verified."
  embed = guilded.Embed(
      title="Server Info",
      description=
      f"🏷️**Server Name: {ctx.guild.name} | `{serverid}`**\n 👑**Server Owner:** {serverowner.mention}\n 📆**Created on: {server.created_at}** \n 📃**Server Bio: `{server.about}`** \n\n *{serververified}*",
      color=guilded.Color.gold(),
  )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed, silent=True)


@bot.command()
async def userinfo(ctx, member: guilded.Member):
  member = await ctx.guild.fetch_member(member.id)
  await member.award_xp(0)
  embed = guilded.Embed(
      title="User Info",
      description=
      f"🏷️**User Name:** {member.mention}** | {member.name} | `{member.id}`**\n 📆**Account Created on: {member.created_at}** \n 🗂️**Joined this server on: {member.joined_at}** \n 📛**Nickname: {member.nick}** \n ❎🅿️**User XP: {member.xp}**",
      color=guilded.Color.gold(),
  )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed, silent=True)


@bot.command()
async def whisper(ctx, message=None):
  author = ctx.author
  if message == None or message == "" or message == " ":
    embed = guilded.Embed(
        title="Error while carrying out your anonymous message",
        description=
        f"{author.mention} - Please include a message. `a/whisper <message>`",
        color=guilded.Color.red(),
    )
    embed.set_footer(text=footer)
    await ctx.send(embed=embed, private=True)
    await ctx.message.delete()
  else:
    privateEmbed = guilded.Embed(
        title=f"{author.mention}, your whisper has been heard..",
        description="Your anonymous message has been sent!",
        color=guilded.Color.blue(),
    )
    privateEmbed.set_footer(text=footer)
    await ctx.send(embed=privateEmbed, private=True)
    time.sleep(0.5)
    embed = guilded.Embed(
        title="An anonymous message has arrived!",
        description=f"{message}",
        color=guilded.Color.gold(),
    )
    embed.set_footer(text=footer)
    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command()
async def quote(ctx):
  with open("quotes.txt", "r", encoding="utf-8") as f:
    randomquote = f.readlines()
    response = random.choice(randomquote)
    embed = guilded.Embed(
        title="Random Quote",
        description=f"{response}",
        color=guilded.Color.gold(),
    )
  embed.set_footer(text=footer)
  await ctx.send(embed=embed)


@bot.command()
async def ban(ctx, member: guilded.Member, confirm):
  if confirm == "myferSignedThis":
    await member.ban()
    embed = guilded.Embed(
        title="User Banned",
        description=f"{member.mention} has been banned.",
        color=guilded.Color.red(),
    )
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)


@bot.command()
async def rate(ctx, rate=None):
  if rate == None:
    embed = guilded.Embed(
        title="Error.",
        description=
        "`ERROR:` *Please use `a/rate <RATE THIS>`! \nArgument missing.*")
    embed.set_footer(text=footer)
    ctx.send(embed=embed)
  else:
    if rate == "Myfer" or rate == "Ace":
      rating = random.randint(10, 10)
    else:
      rating = random.randint(1, 10)
    author = ctx.author.id
    embed = guilded.Embed(
        title=f"I rate {rate}",
        description=f"I rate **{rate}** {rating}/10",
        color=guilded.Color.gold(),
    )
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)


bot.run(TOKEN)
