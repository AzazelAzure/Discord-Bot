# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 23:32:07 2023

@author: Patrick Proctor
"""

#TODO:Create embedder
#TODO:Adjust Logs



import discord
import os
import smtplib
from email.mime.text import MIMEText
from discord.ext.commands import MemberConverter
import logging
from random import randint



def bug_report(report):
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

def location():
    locations = []
    loc = f'Alibis/locations.txt'
    with open(loc) as f:
        for line in f:
            locations.append(line.rstrip())
    #locations = (
     #   'Home', 'The Bar', 'The Post Office', 'Church', 'School', 'A Weed Farm', 
      #  'Disney Land', 'A Night Club', 'A Retirement Home', 
       # 'A Bar Mitzvah', 'The Zoo', 'The Aquarium', 'The Grocery Store', 
        #'A Wedding', 'The Woods on the edge of town'
        #)
    
    send = locations[randint(0, (len(locations)-1))]
    logging.info(f'Location: {send}')
    return send
    
def weapon():
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
    person = []
    adjective = []
    adverb = []
    verb = []
    individual = [person, adjective, adverb, verb]
    per = 'Alibis/people.txt'
    adj = 'Alibis/adjectives.txt'
    adv = 'Alibis/adverbs.txt'
    v = 'Alibis/verbs.txt'
    words = [per, adj, adv, v]
    for i, item in enumerate(words):
        with open(item) as f:
            for line in f:
                individual[i].append(line.title().rstrip())
    """ person = (
        'Three kids in a trenchcoat', 'A guy that communicates solely through a sockpuppet', 
        'A crazy cat lady', 'A drunken clown', 'A pastor with a dark side', 
        'A hobo with a shotgun', 'A stripper', 'A "Karen"', 'Tommy Wiseus alien love child', 
        'A sweaty guy in a sailor moon cosplay', 'A mall santa', 
        'Someone who confidently corrects everything you say with blatently wrong information'
    ) """
    return f"{adjective[randint(0, (len(adjective)-1))]} {person[randint(0, (len(person)-1))]}" # who was {verb[randint(0,(len(verb)-1))]}ing {adverb[randint(0,len(adverb)-1)]}"
    
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
            try:
                with open(f'Alibis/games/{guild}{channel}start.txt') as f:
                    return -1
            except FileNotFoundError:
                with open(filename) as f:
                    x = f.read()
                if str(player) in x:
                    return 0
                with open(filename, 'a') as f:
                    f.write(f'{str(player)}\n')
                with open(filename) as f:
                    players = []
                    plays = f.readlines()
                    for p in plays: players.append(p)
                    if len(plays) <=1:
                        return len(plays)
                    else:
                        return len(plays)
            
       
        if message == '!quit':
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
            try:
                os.remove(f'Alibis/games/{guild}_{channel}_log.txt')
            except FileNotFoundError:
                pass
            try:
                os.remove(f'Alibis/games/{guild}{channel}start.txt')
            except FileNotFoundError:
                pass
            return True
       
        if message == '!start':
            try:
                with open(f'Alibis/games/{guild}{channel}start.txt') as f:
                    pass
            except FileNotFoundError:
                with open(f'Alibis/games/{guild}{channel}start.txt', 'w') as f:
                    f.write('start')
                    pass
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
                    x = f.readline().rstrip()
                    check = str(player).rstrip()
                    logging.info(f"jcheck x: {x}\n"
                                f"jcheck check: {check}\n"
                                f"jcheck comp: {x==check}"
                                f"jcheck player: {player}")
                    if check == x:
                        return True
                    else:
                        return False
            except FileNotFoundError:
                with open(j_file, 'w') as f:
                    f.write(str(player))
        
        if message == '!next':
            with open(filename) as f:
                play = f.readlines()
                logging.info(f'!next play=readlines: {play}')
            with open(filename) as f:
                x = f.read().strip()
                logging.info(f'!next x.read: {x}')
            if x == '':
                return False
            else:
                player = play[randint(0,(len(play)-1))].rstrip()
                logging.info(f'!next random player : {player}')
                x = x.replace(player.rstrip(), '')
                logging.info(f'!next x.replace: {x}')
                with open(filename, 'w') as f:
                    f.write(x)
                is_judge = game_init(channel, guild, message='judge', player=player)
                if is_judge == True:
                    player = game_init(channel, guild, message='!next')
                    return player
                else:
                    return player

        if message == 'end':
            try:
                os.remove(f'Alibis/games/{guild}{channel}quit.txt')
            except FileNotFoundError:
                pass

        if message == '!accuse':
            with open(f'Alibis/games/{guild}{channel}killer.txt') as f:
                x = f.read().rstrip()
            os.remove(f'Alibis/games/{guild}{channel}killer.txt')
            os.remove(f'Alibis/games/{guild}{channel}judge.txt')
            os.remove(f'Alibis/games/{guild}{channel}start.txt')
            return x

        return True
    elif ready_check == False:
        return None

def logger(channel, guild, time, player):
    with open(f'Alibis/games/{guild}_{channel}_log.txt') as f:
        x = f.read()
    with open(f'Alibis/bugs/{guild}_{channel}_{player}_{time}_log.txt', 'w') as f:
        f.write(x)
    


    
    
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
        
    async def on_message(self, message):   
       
        if message.content.startswith('!rotp'):
            logging.basicConfig(filename=f'Alibis/games/{message.guild}_{message.channel}_log.txt', 
                    format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)
            logging.info('Log start')
            await message.channel.send(
            'Welcome to Root of the Problem, a game of murder and mysteries\n'
            'For rules type: `!rules`.  \nTo play type: `!join`'
            )
            game_init(message.channel, message.guild, message='!alibis')
        
        if message.content.startswith('!join'):
            logging.info(f'Caller: {str(message.author)} line:246')
            game = game_init(message.channel, message.guild)
            if game == True:
                players = game_init(message.channel, message.guild, message='!join',player=message.author)
                logging.info(f'!join players response: {players}')
                if players == 0:
                    await message.channel.send(f"{message.author.mention} you're already in the game!")
                    pass
                elif players == -1:
                    await message.channel.send(f"{message.author.mention} The game has already started! Join us next game!")
                    pass
                else:
                    await message.channel.send(f'{message.author.mention} has joined the game.'  
                    f'We have {players} players in the game!'
                    "\nType `!join` to join."
                    )
                if players >= 3:
                    await message.channel.send(
                        'We have enough players!'
                        "\n`!start` when everyone has joined"
                        )
            
        if message.content.startswith('!rules'):
            game = game_init(message.channel, message.guild)
            if game == True:
                await message.channel.send("How to play:"
                "\n\tIn the game of Root of the Problem, there is a Murderer, a Detective, and Suspects"
                "\nEach of the players, except the Detective, will be given a weapon"
                "\nThe players will take turns, using their weapon as a prompt to "
                "explain why they were at the crime scene"
                "\nHowever, no one is allowed to explicitly state what their item is\n"
                "\nIt is up to the Detective to listen to everyones alibi, then make an accusation"
                "\nIf the Detective guesses correctly, the Murderer loses..."
                "\nBut, if they guess wrong, the Murderer wins.\n\n"
                "For more information on the different players, type `!howto detective`, `killer`, or `suspect`"
                )
        
        if message.content.startswith('!howto'):
            game = game_init(message.channel, message.guild)
            if game == True:
                if message.content.lower().endswith('detective'):
                    await message.channel.send("As the detective, it's up to you to solve the case.\n\n"
                                                "During the game, you will listen to everyones alibis\n"
                                                "after which, you will have a chance to ask each suspect\n"
                                                "one question.\n\n"
                                                "Once you decide on who you think is guilty\n"
                                                "Make your accusation, then use !accuse to reveal the killer")
                if message.content.lower().endswith('killer'):
                    await message.channel.send("As the killer, it's your job to convince everyone\n"
                                                "you are innocent...Just one catch though\n\n"
                                                "You won't have an object to base your alibi around\n"
                                                "so you'll have be quick on your feet in throwing off\n"
                                                "the detective from your trail\n\n"
                                                "All suspect rules apply to the killer.")
                if message.content.lower().endswith('suspect'):
                    await message.channel.send("As a suspect, you'll be given a random object\n"
                                                "Using this object, you have to explain why you're innocent\n"
                                                "without saying exactly what your object is\n\n"
                                                "Your alibi must include the person and the place in it as well\n")
                else:
                    await message.channel.send("Use `!howto detective`, `killer`, or `suspect` for more information.")

        if message.content.startswith('!start'):  
            game = game_init(message.channel, message.guild)
            if game == True:
                converter = MemberConverter()
                players = game_init(message.channel, message.guild, '!start')
                if len(players) <=2:
                    await message.channel.send('Not enough players!')
                    pass
                else:
                    judge = players[randint(0,(len(players)-1))]
                    players.remove(judge)
                    logging.info(f'Judge: {judge}')
                    killer = players[randint(0,(len(players)-1))]
                    logging.info(f'Killer: {killer}')
                    players.remove(killer)
                    j = await converter.convert(message.author, judge.rstrip())
                    await message.channel.send(f'{j.mention}, you are the Detective')
                    game_init(message.channel, message.guild, message = 'killer', player=killer)
                    game_init(message.channel, message.guild, player=judge, message='judge')
                    obj = weapon()
                    place = location()
                    person = people()
                    await message.channel.send(f"There was a murder most foul\n"
                        f"{person} was murdered \n"
                        f"with a(an) {obj}\n"
                        f"in/at {place}"
                        )
                    for play in players:
                        play = await converter.convert(message.author, play.rstrip())
                        p_obj = weapon()
                        mess = f'Your item is a(an) {p_obj}'
                        await play.send(mess)
                    killer = await converter.convert(message.author, killer.rstrip())
                    await killer.send("You're the murderer")
                    await message.channel.send('The murderer is out there, and there are many suspects'
                        "\nType `!next` when you're ready to present your alibis"
                        )
            
        if message.content.startswith('!quit'):
            game_end = game_init(message.channel, message.guild, message= '!quit')
            if game_end:
                await message.channel.send('Thanks for playing!')
                       
        if message.content.startswith('!next'):
            game = game_init(message.channel, message.guild)
            if game == True:
                n_player = game_init(message.channel, message.guild, message='!next')
                logging.info(f'n_player check: {n_player}')
                converter = MemberConverter()
                if n_player == False:
                    await message.channel.send(f'All players have had their turn!\n'
                                                'Detective, take this time to ask 1 question to the suspects!\n'
                                                'Once you make your accusation, use `!accuse`.')
                    game_init(message.channel, message.guild, message='end')
                if n_player == '':
                    n_player = game_init(message.channel, message.guild, message='!next')
                    if n_player == False:
                        await message.channel.send(f'All players have had their turn!\n'
                                                'Detective, take this time to ask 1 question to the suspects!\n'
                                                'Once you make your accusation, use `!accuse`.')
                        game_init(message.channel, message.guild, message='end')
                    else:
                        n_user = await converter.convert(message.author, n_player.rstrip())
                        await message.channel.send(f"{n_user.mention}!\nIt's your turn!")
                        logging.error(f'Empty n_player: {n_player}')
                    pass
                else:
                    n_user = await converter.convert(message.author, n_player.rstrip())
                    await message.channel.send(f"{n_user.mention}!\nIt's your turn!")
                
                pass
                      
        if message.content.startswith('!accuse'):
            game = game_init(message.channel, message.guild)
            if game == True:
                is_judge = game_init(message.channel, message.guild, player=message.author, message='judge')
                logging.info(f'!accuse jcheck: Call: {str(message.author)} Response: {is_judge}')
                if is_judge == True:
                    reveal = game_init(message.channel, message.guild, message='!accuse')
                    converter = MemberConverter()
                    k = await converter.convert(message.author, reveal)
                    await message.channel.send(f'{k.mention} was the killer!\nUse `!alibis` to play again')
                    game_init(message.channel, message.guild, message='!quit')
                    pass
                else:
                    await message.channel.send(f"{message.author.mention} you're not the detective!")
                    pass
    
        if message.content.startswith('!bug'):
            logger(message.channel, message.guild, message.created_at, message.author)
            report = f'Bug reported by {message.author} in {message.guild} at {message.created_at}'
            sent = bug_report(report)
            if sent:
                await message.channel.send('Bug reported')
            else:
                await message.channel.send('Bug report failed')


    

    



intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

client = MyClient(intents=intents)

client.run('MTA3MTMxMTg4MjE2MzU4OTE1MQ.GdJmF1.kPKe4peRhXuy8LUs_HtPHgC_Jkp9Y7M2quffWs')