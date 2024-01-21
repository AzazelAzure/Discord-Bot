# -*- coding: utf-8 -*-
"""

@author: Patrick Proctor
"""

import discord
import os
import json
import logging
import asyncio
from email.mime.text import MIMEText
from discord.ext.commands import MemberConverter

#   Diablo meets Civ for combat
    #   Set a damage calculation for combat based on stats
    #   Provide players with a approximate outcome to let them make a decision:
        #   Fight or Flee
    #   Perhaps use a d20 model
        #   Or a percentage model?
        #   Maybe both?


#TODO:Create terrain generator
#TODO:Create mapping system
#TODO:Create location tracker
#TODO:Create monster generator
#TODO:Create item generator
    #   Randomly generate adjective, the weapon, and bonus?
    #   Make specific legendary(?) items, -> Named(maybe)

#TODO:Create player generator
    #   Classes
        #   Fighter
            #   The tank
        #   Rogue/Ranger
            #   physical dps
        #   Caster
            #   magic dps
        #   Stat modifiers
        #   Abilities
        #   Restrictions?
    #   Stats

#TODO:Create combat system
    #   Allow for ranged combat
        #   Compass system/facing for movement
    #   Damage types


intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True


client = discord.Client(intents=intents)

#   Create the bug reporter
def bug_report(report):
    """Creates and emails a bug report"""
    sender = "etusnproctor@gmail.com"
    recipient = "etusnproctor@gmail.com"
    password = "rrjm wusl sboo ejnm"

    message = MIMEText(report)
    message["Subject"] = "Discord Bot Bug Report"
    message["From"] = sender
    message["To"] = recipient

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender, password)
        smtp.send_message(message)
        return True

#   Create the initial game instance
def instancer(guild, channel):
    """Creates the initial game instance"""
    guild = guild
    channel = channel
    send ={'channel':str(channel)}
    filepath = f"Discablo/games/{guild}/{channel}.json"
    with open(filepath, 'w') as f:
        json.dump(send, f)


def channel_check(guild, channel):
    """
    Checks to see if command is in the correct channel.
    Returns True if command is in correct channel.
    Returns False if command is in incorrect channel.
    Returns None if function fails.
    """
    guild = guild
    channel = channel
    channel_check = {'channel': str(channel)}
    try:
        with open(f"Discablo/games/{guild}/{channel}.json") as f:
            read_check = json.load(f)
            if channel_check['channel'] == read_check['channel']:
                return True
            else:
                return None
    except FileNotFoundError:
        return False

def player_handler(guild, channel, player):
    filename = f'Discablo/games/{guild}/{player}.json'
    try:
        with open(filename) as f:
            pass
    except FileNotFoundError:
        return False
    pass

def new_char(guild, channel, player):
    """
    Creates the new character file.
    """
    filename = f'Discablo/games/{guild}/{player}.json'
    try:
        with open(filename) as f:
            pass
    except FileNotFoundError:
        with open(filename, 'w') as f:
            new_char = {
            'Player': {player}, 
            'Guild': {guild},
            'Channel': {channel},
            }
            json.dump({new_char}, f)
    pass

def embedder(embedded):
    if embedded == 'new_char':
        embed = discord.Embed(title= 'Create a character', description= 'Time to start your adventure')
        embed.add_field(name= '', value= 'Would you like to create a new character?', inline= True)
        embed.add_field(name="\u200b", value = '[Yes]')
        embed.add_field(name="\u200b", value='[No]')
        embed.set_footer(text="use `!help` for more information")
        return embed

    elif embedded == 'make_char':
        embed = discord.Embed(title= 'Welcome, newcomer', description= 'Your destiny awaits')
        embed.add_field(value= "Welcome, stranger.  Your adventure awaits.  But first.... \n" 
                                "Tell me....  What is your profession\n\n", inline= True)
        embed.add_field(name="\u200b", value = '[Warrior]')
        embed.add_field(name="\u200b", value='[Rogue]')
        embed.add_field(name="\u200b", value='[Wizard]')
        embed.set_footer(text="use `!help <class>` for more information")
        return embed

    elif embedded == 'warrior':
        embed = discord.Embed(title= 'Warrior', description= 'A mighty fighter')
        embed.add_field(value= "Ah, I see, so you are a Warrior?\n\n", inline= True)
        embed.add_field(name="\u200b", value = '[Yes]')
        embed.add_field(name="\u200b", value='[No]')
        embed.set_footer(text="use `!help <class>` for more information")
        return embed
    
    elif embedded == 'rogue':
        embed = discord.Embed(title= 'Rogue', description= 'A cunning thief')
        embed.add_field(value= "Ah, I see, so you are a Rogue?\n\n", inline= True)
        embed.add_field(name="\u200b", value = '[Yes]')
        embed.add_field(name="\u200b", value='[No]')
        embed.set_footer(text="use `!help <class>` for more information")
        return embed
    
    elif embedded == 'wizard':
        embed = discord.Embed(title= 'Wizard', description= 'A brilliant mage')
        embed.add_field(value= "Ah, I see, so you are a Wizard?\n\n", inline= True)
        embed.add_field(name="\u200b", value = '[Yes]')
        embed.add_field(name="\u200b", value='[No]')
        embed.set_footer(text="use `!help <class>` for more information")
        return embed


def check_reaction(reaction, user, emoji):
    return str(reaction.emoji) == emoji

@client.event
async def on_ready():
    print(f'Logged on as {client.user}')
    
@client.event
async def on_message(message):
    logging.basicConfig(filename=f'Discablo/games/{message.guild}/{message.guild}_log.txt', 
                format='%(levelname)s:%(message)s',
                level=logging.DEBUG)

    if message.content.startswith('!disc'):
        start_check = channel_check(message.guild, message.channel)
        if message.content.lower().endswith('start'):
            logging.info(f'!disc start check: {start_check}')
            if start_check == True:
                with open(f"Discablo/games/{message.guild}/{message.channel}.json") as f:
                    game_started = json.load(f)
                    await message.channel.send(f"Game already started in {game_started['channel']}")
            elif start_check == False:
                instancer(message.guild, message.channel)
                await message.channel.send(f"Game started in {message.channel}")
            elif start_check == None:
                logging.error(f"<!disc start> command failed to create start json")

        if message.content.lower().endswith('join'):
            if start_check == True:
                in_game = player_handler(message.guild, message.channel, message.author)
                if in_game == False:
                    create_char = embedder('new_char')
                    msg = await message.channel.send(embed=create_char)
                    await msg.add_reaction('Button: Yes')
                    await msg.add_reaction('Button: No')
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=lambda r, u: check_reaction(r, u, 'Button: Yes', client))
                        make_char = True
                    except asyncio.TimeoutError:
                        await message.channel.send('No selection made')
                        await msg.delete()
                        pass

                    if make_char:     
                        new_char(message.guild, message.channel, message.author)
                        make_char = embedder('make_char')
                        msg = await message.author.send(embed=make_char)
                        await msg.add_reaction('Button: Warrior')
                        await msg.add_reaction('Button: Rogue')
                        await msg.add_reaction('Button: Wizard')
                    warrior = check_reaction(reaction, client, 'Button: Warrior')
                    rogue = check_reaction(reaction, client, 'Button: Rogue')
                    wizard = check_reaction(reaction, client, 'Button: Wizard')
                    if warrior:
                        embed = embedder('warrior')
                        msg = await message.author.send(embed=embed)
                        await msg.add_reaction('Button: Yes')
                        await msg.add_reaction('Button: No')
                        logging.info(f'Made it through Warrior')
                    if rogue:
                        embed = embedder('rogue')
                        msg = await message.author.send(embed=embed)
                        await msg.add_reaction('Button: Yes')
                        await msg.add_reaction('Button: No')
                        logging.info(f'Made it through rogue')
                        
                    if wizard:
                        embed = embedder('wizard')
                        msg = await message.author.send(embed=embed)
                        await msg.add_reaction('Button: Yes')
                        await msg.add_reaction('Button: No')
                        logging.info(f'Made it through wizard')
                        


                pass
            elif start_check == False:
                pass
            pass

@client.event
async def on_reaction_add(reaction, user, guild, channel):
    if reaction == None:
        pass
    pass

@client.event
async def on_guild_join(guild):
    path = f'Discablo/games/{guild}'
    if not os.path.exists(path):
        os.makedirs(path)
    logging.basicConfig(filename=f'Discablo/games/{guild}/{guild}_log.txt', 
                format='%(levelname)s:%(message)s',
                level=logging.DEBUG)
    message1 = "Hello!  Navigate to an open channel and enter `!disc start` to create a new instance of the game to run in that channel"
    message2 = "Discablo can only run in one channel"
    owner = guild.owner
    logging.info(f'Server owner: {owner} Guild owner check:{guild.owner}')
    if owner != None:
        await owner.send(message1)
        await owner.send(message2)
    else:
        logging.error(f'Owner returned none')
        join_channel = guild.text_channels[0]
        await join_channel.send(message1)
        await join_channel.send(message2)


client.run('MTA3MjI5OTkwNzc5NDM0NjA4NA.GyCEeq.JntVWGnxE0nzR4_AQeb3J4tzyBj1TUV7toFoko')