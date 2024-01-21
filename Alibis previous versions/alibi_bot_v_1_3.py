# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 23:32:07 2023

@author: Patrick Proctor
"""

#TODO:Set different message status to a interger or binary system
#TODO:Create embedder
#TODO:Upload places and people lists
#TODO:Find lists of adverbs and verbs
#TODO:Create gamepage on GGJ website
#TODO:lower all player names when checking names
#TODO:Fix howtos
#TODO:Remove logs
#TODO:fix !next algorithm, currently is bypassing new game check, and re-adding players after removal
    #   Check logs on fix, explains issues
#TODO:fix file deletion algorith.  Missing players files on !quit
#TODO:Fix !join to quiet fail if game started

import discord
import os
import pathlib
import json
from discord.ext.commands import MemberConverter
from random import randint




def location():
    locations = (
        'Home', 'The Bar', 'The Post Office', 'Church', 'School', 'A Weed Farm', 
        'Disney Land', 'A Night Club', 'A Retirement Home', 
        'A Bar Mitzvah', 'The Zoo', 'The Aquarium', 'The Grocery Store', 
        'A Wedding', 'The Woods on the edge of town'
        )
    return locations[randint(0, (len(locations)-1))]
    
def weapon(*args):
    object = args
    directory = pathlib.Path.cwd()
    adjectives = []
    noun_list =[]
    adjs = f'Alibis/adjectives.txt'
    nouns = f'Alibis/nouns.txt'
    with open(adjs) as file_object:
        for line in file_object:
            adjectives.append(line.rstrip())
    with open(nouns) as file_object:
        for line in file_object:
            noun_list.append(line.rstrip())
    n_weapon = f'{adjectives[randint(0, (len(adjectives)-1))]} {noun_list[randint(0,(len(noun_list)-1))]}'
    return n_weapon
    
def people():
    person = (
        'Three kids in a trenchcoat', 'A guy that communicates solely through a sockpuppet', 
        'A crazy cat lady', 'A drunken clown', 'A pastor with a dark side', 
        'A hobo with a shotgun', 'A stripper', 'A "Karen"', 'Tommy Wiseus alien love child', 
        'A sweaty guy in a sailor moon cosplay', 'A mall santa', 
        'Someone who confidently corrects everything you say with blatently wrong information'
    )
    return person[randint(0, (len(person)-1))]
    
def motives():
    n_motive = ("","")
    return n_motive(randint(0, (len(n_motive)-1)))



def instancer(filename, message=None):
    if message == '!alibis':
        try:
            with open(filename):
                pass
        except FileNotFoundError:
            with open(filename, 'w') as f:
                f.write("")
                pass
    elif not message:
        try:
            with open(filename) as f:
                return True
        except FileNotFoundError:
            return False
    


def game_init(channel, guild, message=None, player=None, *args):
    filename = f'Alibis/games/{guild}{channel}.txt'
    if message == '!alibis': 
        instancer(filename, message)
        return None
    ready_check = instancer(filename)
    if ready_check == True:
        if message == '!join':
            with open(filename, 'a') as f:
                f.write(str(player)+",\n")
            with open(filename) as f:
                players = []
                plays = f.readlines()
                for p in plays: players.append(p)
                print(f'Plays:{plays} length{len(plays)} line: 103')
                if len(plays) <=1:
                    return len(plays)
                else:
                    return len(plays)
       
        if message == '!quit':
            with open(filename) as f:
                    for n in f:
                        try:
                            os.remove(f'Alibis/games/{guild}{channel}{n.rstrip()}.txt')
                        except FileNotFoundError:
                            pass
            os.remove(filename)
            try:
                os.remove(f'Alibis/games/{guild}{channel}killer.txt')
            except FileNotFoundError:
                pass
            try:
                os.remove(f'Alibis/games/{guild}{channel}judge.txt')
            except FileNotFoundError:
                pass
            try:
                os.remove(f'Alibis/games/{guild}{channel}start.txt')
            except FileNotFoundError:
                pass
            try:
                os.remove(f'Alibis/games/{guild}{channel}quit.txt')
            except FileNotFoundError:
                pass
            return True
       
        if message == '!start':
            with open(filename) as f:
                players = []
                plays = f.readlines()
                for p in plays:
                    players.append(p)
                return players
       
        if message == 'killer':
            k_file = f'Alibis/games/{guild}{channel}killer.txt'
            try:
                with open(k_file) as f:
                    pass
            except FileNotFoundError:
                with open(k_file, 'w') as f:
                    f.write(str(player))
       
        if message == 'judge':
            j_file = f'Alibis/games/{guild}{channel}judge.txt'
            try:
                with open(j_file) as f:
                    print(f'Judge checker compare: {f.readline()} vs {player}')
                    if player == f.readline():
                        return True
                    else:
                        return False
            except FileNotFoundError:
                with open(j_file, 'w') as f:
                    f.write(str(player))
        
        if message == '!next':
            with open(filename) as f:
                gamers = f.readlines()
                print(f'!next gamers: {gamers} line: 167')
            for g in gamers:
                print(f'!next G in gamers: {g} line:169')
                filename = f'Alibis/games/{guild}{channel}{g.rstrip()}.txt'
                try:
                    with open(filename):
                        print(f'G: {g}, Path open, filename: {filename} line:173')
                        return investigation(channel, guild, players=g)
                except FileNotFoundError:
                    try:
                        with open(f'Alibis/games/{guild}{channel}start.txt'):
                            with open(filename, 'w') as f:
                                print(f'G: {g} Path fnf, start found, filename:{filename} line:179\n')
                                f.write(g)
                                continue
                    except FileNotFoundError:
                        with open(f'Alibis/games/{guild}{channel}start.txt', 'w') as f:
                            f.write('begin')
                            print(f'G: {g} Path fnf, start nf, filename:{filename} line:185\n')
                            return investigation(channel, guild)                         
            try:
                with open(f'Alibis/games/{guild}{channel}start.txt'):
                    return investigation(channel, guild, gamers[0])
            except FileNotFoundError:
                return 'Ready'
        return True
    elif ready_check == False:
        return None

def investigation(channel, guild, players='newgame'):
    gamers = []
    single = ''
    if players == 'newgame':
        try:
            with open(f'Alibis/games/{guild}{channel}quit.txt'):
                os.remove(f'Alibis/games/{guild}{channel}quit.txt')
                os.remove(f'Alibis/games/{guild}{channel}start.txt')
                return 'New Game'
        except FileNotFoundError:
            with open(f'Alibis/games/{guild}{channel}quit.txt', 'w') as f:
                f.write('quit check')
                return 'New Game'
    for player in players:
        single += player
        gamers.append(player)
    if len(gamers) >= 1:
        try:
            os.remove(f'Alibis/games/{guild}{channel}{players}.txt')
            os.remove(f'Alibis/games/{guild}{channel}killer.txt')
            os.remove(f'Alibis/games/{guild}{channel}judge.txt')
            return 'New Game'
        except FileNotFoundError:
            order = gamers[randint(0,(len(gamers)-1))]
            os.remove(f'Alibis/games/{guild}{channel}{order.rstrip()}.txt')
            return order
    elif len(players) == 1:
        os.remove(f'Alibis/games/{guild}{channel}{players}.txt')
    elif len(gamers) == 0:
        pass


def dm(client, player=None, message=None):
    this_client = client
    this_client.ctx.player.send(message)
    pass
    
            


    
    
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
        

    async def on_message(self, message):   
        if message.content.startswith('!alibis'):
            await message.channel.send(
            'Welcome to Alibis, a game of murder and mysteries\n'
            'For rules type: !rules.  \nTo play type: !join'
            )
            game_init(message.channel, message.guild, message='!alibis')
        if message.content.startswith('!join'):
            print(f'Caller: {message.author} line:246')
            game = game_init(message.channel, message.guild)
            if game == True:
                players = game_init(message.channel, message.guild, message='!join',player=message.author)
                await message.channel.send(f'{message.author.mention} has joined the game.'  
                    f'We have {players} players in the game!'
                    "\nType !join to join."
                    )
                if players >= 3:
                    await message.channel.send(
                        'We have enough players!'
                        "\n!start when everyone has joined"
                        )
            
        if message.content.startswith('!rules'):
            game = game_init(message.channel, message.guild)
            if game == True:
                await message.channel.send("How to play:"
                "\n\tIn the game of Alibis, there is a Murderer, a Detective, and Suspects"
                "\n\tEach of the players, except the Detective, will be given a weapon"
                "\n\tThe players will take turns, using their weapon as a prompt to "
                "explain why they were at the crime scene"
                "\n\tHowever, no one is allowed to explicitly state what their item is\n"
                "\n\tIt is up to the Detective to listen to everyones alibi, then make an accusation"
                "\n\tIf the Detective guesses correctly, the Murderer loses..."
                "\n\tBut, if they guess wrong, the Murderer wins.\n"
                "\nFor more information on the different players, type !howto Detective, Murderer, or Suspect"
                )
        
        if message.content.startswith('!howto'):
            game = game_init(message.channel, message.guild)
            if game == True:
                if message.content.lower().contains('detective'):
                    await message.channel.send('')
                if message.content.lower().contains('murderer'):
                    await message.channel.send('')
                if message.content.lower().contains('suspect'):
                    await message.channel.send('')
                else:
                    message.channel.send("Sorry, I didn't get that")

        if message.content.startswith('!start'):  
            game = game_init(message.channel, message.guild)
            if game == True:
                converter = MemberConverter()
                players = game_init(message.channel, message.guild, '!start')
                judge = players[randint(0,(len(players)-1))]
                players.remove(judge)
                print(f'Judge: {judge}')
                killer = players[randint(0,(len(players)-1))]
                print(f'Killer: {killer}')
                players.remove(killer)
                j = await converter.convert(message.author, judge.replace(',','').rstrip())
                await message.channel.send(f'{j.mention}, you are the Detective')
                game_init(message.channel, message.guild, message = 'killer', player=killer)
                game_init(message.channel, message.guild, player=judge, message='judge')
                obj = weapon()
                place = location()
                person = people()
                await message.channel.send(f'There was a murder most foul\n'
                    f'{person} was murdered \nwith a(an) {obj}\n'
                    f'in/at {place}'
                    )
                for play in players:
                    play = await converter.convert(message.author, play.replace(',','').rstrip())
                    p_obj = weapon()
                    mess = f'Your item is a(an) {p_obj}'
                    await play.send(mess)
                killer = await converter.convert(message.author, killer.replace(',','').rstrip())
                await killer.send("You're the murderer")
                await message.channel.send('The murderer is out there, and there are many suspects'
                    "\nType !next when you're ready to present your alibis"
                    )
            
        if message.content.startswith('!quit'):
            game_end = game_init(message.channel, message.guild, message= '!quit')
            if game_end:
                await message.channel.send('Thanks for playing!')
            else:
                await message.channel.send('Quit loop functioning')
                pass
            
        if message.content.startswith('!next'):
            game = game_init(message.channel, message.guild)
            if game == True:
                n_player = game_init(message.channel, message.guild, message='!next')
                is_judge = game_init(message.channel, message.guild, player=n_player, message='judge')
                print(f'Judge check: {is_judge}')
                if n_player == 'New Game':
                    await message.channel.send("It's a new game!  Type !next to continue, or !quit to quit.")
                    pass
                elif is_judge == True:
                    n_player = game_init(message.channel, message.guild, message='!next')
                    pass
                elif n_player == 'Ready':
                    print(f'n_player before modify: {n_player}')
                    n_player = game_init(message.channel, message.guild, message='!next')
                    print(f'n_player after modify{n_player}')
                    await message.channel.send(f"@{n_player}, it's your turn!")

                else:
                    await message.channel.send(f'@{n_player}, its your turn!')
        
        if message.content.startswith('!accuse'):
            game = game_init(message.channel, message.guild)
            if game == True:
                is_judge = game_init(message.channel, message.guild, player=message.author, message='judge')
                if is_judge == True:
                    message.replace('!accuse', '').lower()
                    pass
    
                    
                

    

    



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTA3MTMxMTg4MjE2MzU4OTE1MQ.GdJmF1.kPKe4peRhXuy8LUs_HtPHgC_Jkp9Y7M2quffWs')