import discord 
from discord.ext import commands

token = "bot token"
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.event
async def on_message(message):
    ctx = await bot.get_context(message) # Defining Context
    member = ctx.message.author # Defining Member
    verified = discord.utils.get(ctx.guild.roles, name="(Verified Role Name)") # Getting Role
    if ctx.channel.id == 1009351551749476382: # <- Input Your Verification Channel ID
        if message.content == ">verify":
            await message.delete() # Deletes message 
            if verified in member.roles: # Checks if Member Is Already Verified
                await member.send("You are Already Verified...") # Responds If Member Is Verified
            else: # If Member Isnt Verified
                await member.add_roles(verified) # Gives Verified Role
                embed=discord.Embed(title=f"New Member Inbound!", description=f"Congrats {member.mention} \nYou Have Successfully Verified! \nYou Can Now View The Rest of The Server!")
                embed.set_footer(text=footertext, icon_url=footericonurl)
                await member.send(embed=embed) # Sends Your Embed to Member
                await bot.get_channel(1009354583975407617).send(embed=embed) # Welcome Message (Remove if You Want.. Kinda Useless)
        else:
            await message.delete()
            
            
# / Running the Bot! # \
bot.run(token)
