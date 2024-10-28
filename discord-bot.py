import discord
from discord.ext import commands

# Initialize the Discord client
bot = commands.Bot(command_prefix='!')

@bot.command()
async def menu(ctx, menu_name):
    if menu_name in menus:
        # Send the menu prompt and options to the Discord channel
        await ctx.send(menus[menu_name]["prompt"])
        await ctx.send("\n".join(menus[menu_name]["options"]))
    else:
        await ctx.send("Invalid menu name.")

# Run the bot
bot.run('YOUR_BOT_TOKEN')