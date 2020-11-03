import discord
import math
import json, os
import random
from discord.ext import commands
token = ""

os.chdir("./")
prefix = ["!","-","=","_","+","~",",",".","/","?"]

client = commands.Bot(command_prefix=prefix)
 


@client.event
async def on_ready():
    print('bot is ready')


    
    
	

@client.command()
async def test(ctx):
    await ctx.send("Test Complete")
    await ctx.send(100 * math.pi)
    await ctx.send("That's 100 * PI")
    await ctx.send(100 * math.pow(10,90))


@client.command()
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(
        title=f"{ctx.author.name}'s balance", color=discord.Color.blue())
    em.add_field(name="Wallet", value=wallet_amt)
    em.add_field(name="Bank", value=bank_amt)
    await ctx.send(embed=em)

@client.command()
async def work(ctx):
    await open_account(ctx.author)
    user = ctx.author
    jobs = ["macdonalds","walmart","karen","coder"]
    users = await get_bank_data()
    job = random.choice(jobs)
    earnings = random.randrange(101)

    await ctx.send(f"{job} gave you {earnings} coins")

    users[str(user.id)]["wallet"] += earnings

    with open("db.json", "w") as f:
        json.dump(users, f)

@client.command()
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f"Someone gave you {earnings} coins")

    users[str(user.id)]["wallet"] += earnings

    with open("db.json", "w") as f:
        json.dump(users, f)


async def bot_config_file():
        with open("prefix.json", "r") as f:
       
         configfile = json.load(f)
         return configfile
        

async def open_account(user):
    users = await get_bank_data()

    with open("db.json", "r") as f:
        users = json.load(f)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}

        users[str(user.id)]["wallet"] = 0

        users[str(user.id)]["bank"] = "Not Working Right Now"

    with open("db.json", "w") as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open("db.json", "r") as f:
        users = json.load(f)
    return users

async def update_bank(user,change = 0,mode = "wallet"):
        users = await get_bank_data()
        

        users[str(user.id)][mode] += change
        print("got pass error")

        with open("db.json", "w") as f:
          json.dump(users, f)
          bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
        return bal













client.run(token)
