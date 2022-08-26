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

        # If Anyone Trys to Type Anything Else In Your Verification Channel (Including Admins)
        if 'a' in message.content:
            await message.delete()
        if 'A' in message.content:
            await message.delete()
        if 'b' in message.content:
            await message.delete()
        if 'B' in message.content:
            await message.delete()
        if 'c' in message.content:
            await message.delete()
        if 'C' in message.content:
            await message.delete()
        if 'd' in message.content:
            await message.delete()
        if 'D' in message.content:
            await message.delete()
        if 'e' in message.content:
            await message.delete()
        if 'E' in message.content:
            await message.delete()
        if 'f' in message.content:
            await message.delete()
        if 'F' in message.content:
            await message.delete()
        if 'g' in message.content:
            await message.delete()
        if 'G' in message.content:
            await message.delete()
        if 'h' in message.content:
            await message.delete()
        if 'H' in message.content:
            await message.delete()
        if 'i' in message.content:
            await message.delete()
        if 'I' in message.content:
            await message.delete()
        if 'j' in message.content:
            await message.delete()
        if 'J' in message.content:
            await message.delete()
        if 'k' in message.content:
            await message.delete()
        if 'K' in message.content:
            await message.delete()
        if 'l' in message.content:
            await message.delete()
        if 'L' in message.content:
            await message.delete()
        if 'm' in message.content:
            await message.delete()
        if 'M' in message.content:
            await message.delete()
        if 'n' in message.content:
            await message.delete()
        if 'N' in message.content:
            await message.delete()
        if 'o' in message.content:
            await message.delete()
        if 'O' in message.content:
            await message.delete()
        if 'p' in message.content:
            await message.delete()
        if 'P' in message.content:
            await message.delete()
        if 'q' in message.content:
            await message.delete()
        if 'Q' in message.content:
            await message.delete()
        if 'r' in message.content:
            await message.delete()
        if 'R' in message.content:
            await message.delete()
        if 's' in message.content:
            await message.delete()
        if 'S' in message.content:
            await message.delete()
        if 't' in message.content:
            await message.delete()
        if 'T' in message.content:
            await message.delete()
        if 'u' in message.content:
            await message.delete()
        if 'U' in message.content:
            await message.delete()
        if 'v' in message.content:
            await message.delete()
        if 'V' in message.content:
            await message.delete()
        if 'w' in message.content:
            await message.delete()
        if 'W' in message.content:
            await message.delete()
        if 'x' in message.content:
            await message.delete()
        if 'X' in message.content:
            await message.delete()
        if 'y' in message.content:
            await message.delete()
        if 'Y' in message.content:
            await message.delete()
        if 'z' in message.content:
            await message.delete()
        if 'Z' in message.content:
            await message.delete()
            
            
# / Running the Bot! # \
bot.run(token)
