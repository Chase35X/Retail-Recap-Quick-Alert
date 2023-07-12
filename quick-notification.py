import discord
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
import aiohttp


token = # Input bot token

bot = commands.Bot(command_prefix='.')



@bot.command()
async def alert (ctx, arg):

    async with aiohttp.ClientSession() as session:
        webhooks = [
       # Input list of webhooks
        ]


        description = arg
        embed = discord.Embed(
            title = "Retail Recap Drop Info Alert!",
            description = "",
            color = 0x89CFF0
        )
        embed.add_field(name="What's Happening", value=description)

        for webhook in webhooks:
            embed.set_footer(text= "Retail Recap Alerts")
            await webhook.send(embed=embed)

bot.run(token)
