
import random
weapons = {'none':(4, 6), 'sword':(8, 12), 'dagger':(6, 10), 'mace':(7, 11)}
armor = {'none':(1), 'clothes':(3), 'chain mail armor':(5)}
player = {'weapon': None, 'armor': None, 'health': 50}
boss = {'weapon':weapons['mace'], 'armor':armor['clothes'], 'health': 60}



def fight (player, boss):
    while player['health'] > 0 and boss['health'] > 0:
        action = raw_input("Type Attack or Dodge. ").lower().strip()
        if action == "attack":
            player_damage = random.randint(*boss['weapon']) - player['armor']
            boss_damage = random.randint(*player['weapon']) - boss['armor']
            player['health'] -= player_damage
            boss['health'] -= boss_damage
            print("You hit the boss for {} damage, he has {} health left.".format(boss_damage, boss['health']))
            print("The boss hits you for {} damage, you have {} health left.".format(player_damage, player['health']))
        if action == "dodge":
            if random.random() > .25:
                boss['health'] -= 2
                print("The boss misses and hit's his himself for 2 damage, he has {} health left.".format(boss['health']))   
            else:
                player_damage = random.randint(*boss['weapon']) - player['armor']
                player['health'] -= player_damage
                print("Your dodge failed. You were hit for {} health. You have {} health left.".format(player_damage, player['health']))
                
        if player['health'] <= 0 and boss['health'] >= 1:
            print("You die")
        elif boss['health'] <= 0 and player['health'] >= 1:
            print("You win!")
        elif boss['health'] <= 0 and player['health'] <= 0:
            print("You kill eachother...")



print("You wake up naked to a full moon at night in the middle of the woods.")
print("On the floor, you see a compass and a note telling you to go North or else you will die.")
print("You decide to take the note's advice and travel North. Also, you might want to find some clothes...")
print("You see a faint light in the distance and a trail heading off into the dark.")
print("Do you choose to walk towards the light or do you choose to follow the trail?")
action = raw_input("Type: Light or Trail, then press enter: ").lower().strip()

if action == "light":
    print("You come across a house.")
    print("Do you open the door and walk inside the house?")
    action = raw_input("Type: Yes or No, then press enter: ").lower().strip()
    if action == "yes":
        print("You open the door, walk into the house and instantly get shot.")
        print("Why would you walk into a house without knocking????")
        print("Game over, please reset")
    elif action == "no":
        print("Before you open the door, you get the sudden urge to knock first.")
        print("Sir Treysef Brohamual L Jackson Bandemirius III opens the door and says 'What do you want?'")
        action = raw_input("Type 1 or 2: 1 for 'Can you help me find some clothes?' 2 for 'I feel as if I am one with the universe.' ").strip()
        if action == "1":
            print("Sir Treysef Brohamual L Jackson Bandemirius III says: Ofcoarse! Here take these old but clean clothes. It isn't much, but it's something.")
            print("Sir Treysef Brohamual L Jackson Bandemirius III says: Also take this dagger for some protection!.")
            print("Is there anything else I can help you out with brosef?")
            print("A sudden urge comes over you and you ask where the closest town is.")
            print("The Old Man says 'If you head down the trail right next to my house, you'll make it to the town of Brunswick.")
            print("But be careful over there. People have been known to have been captured and never seen again in the universe.")
            print("You travel down the trail and reach the town of Brunswick.")
            print("Instantly you are spotted by a guard and he asks if you like access into the Town.")
            action = raw_input("Type: Yes or No, then press enter: ").lower().strip()
            if action == "yes":
                print("The guard gladly leads you into the town of Brunsiwck.")
                print("Once the gate closes, the guard immeadiately places you under arrest.")
                action = raw_input("Type run or stay, then press enter: ").lower().strip()
                if action == "run":
                    print("You punch the guard and run down the closest alleyway.")
                    print("Down the alleyway, you see a door, do you open it?")
                    action = raw_input("Type yes or no, then press enter: ").lower().strip()
                    if action == "yes":
                        print("You walk through the door and notice that someone obviously lives here.")
                        print("You see a very nice looking sword hanging about a fireplace.")
                        print("Do you choose to take the sword? Yes or No.")
                        action = raw_input("Type yes or yes, then press enter: ").lower().strip()
                        if action == "yes":
                            player['weapon'] = weapons['sword']
                            player['armor'] = armor['clothes']
                            print("You take the sword and run out of the house.")
                            print("As you are running out of the house, you step on a trap door and fall into it.")
                            print("You land in a room underground and you see a man walking towards you.")
                            print("He has a mace in his hand and looks as if he wants to kill you.")
                            fight(player, boss)
                        elif action == "no":
                            player['weapon'] = weapons['dagger']
                            player['armor'] = armor['clothes']
                            print("You take the sword and run out of the house.")
                            print("As you are running out of the house, you step on a trap door and fall into it.")
                            print("You land in a room underground and you see a man walking towards you.")
                            print("He has a mace in his hand and looks as if he wants to kill you.")
                            fight(player, boss)
                elif action == "stay":
                    player['armor'] = armor['none']
                    player['weapon'] = weapons['none']
                    print("You are stripped of all of your weapons and armor and taken to an unknown location.")
                    print("You see a man walking towards you.")
                    print("He has a mace in his hand and looks as if he wants to kill you.")
                    fight(player, boss)
            if action == "no":
                print("The guard doesnt take no as an answer and forces you into the town of Brunsiwck.")
                print("Once the gate closes, the guard immeadiately places you under arrest.")
                action = raw_input("Type run or stay, then press enter: ").lower().strip()
                if action == "run":
                    print("You punch the guard and run down the closest alleyway.")
                    print("Down the alleyway, you see a door, do you open it?")
                    action = raw_input("Type yes or no, then press enter: ").lower().strip()
                    if action == "yes":
                        print("You walk through the door and notice that someone obviously lives here.")
                        print("You see a very nice looking sword hanging about a fireplace.")
                        print("Do you choose to take the sword? Yes or No.")
                        action = raw_input("Type yes or no, then press enter: ").lower().strip()
                        if action == "yes":
                            player['weapon'] = weapons['sword']
                            player['armor'] = armor['clothes']
                            print("You take the sword and run out of the house.")
                            print("As you are running out of the house, you step on a trap door and fall into it.")
                            print("You land in a room underground and you see a man walking towards you.")
                            print("He has a mace in his hand and looks as if he wants to kill you.")
                            fight(player, boss)
                        elif action == "no":
                            player['weapon'] = weapons['dagger']
                            player['armor'] = armor['clothes']
                            print("You take the sword and run out of the house.")
                            print("As you are running out of the house, you step on a trap door and fall into it.")
                            print("You land in a room underground and you see a man walking towards you.")
                            print("He has a mace in his hand and looks as if he wants to kill you.")
                            fight(player, boss)
                    if action == "no":
                        print("The guard catches you and bashes your head in for punching him in the face.")
                        print("You die....")
                elif action == "stay":
                    player['armor'] = armor['none']
                    player['weapon'] = weapons['none']
                    print("You are stripped of all of your weapons and armor and taken to an unknown location.")
                    print("You see a man walking towards you.")
                    print("He has a mace in his hand and looks as if he wants to kill you.")
                    fight(player, boss)
            
        elif action == "2":
            print("Sir Treysef Brohamual L Jackson Bandemirius III says: Ahhh, you speak my language perfectly.")
            print("Sir Treysef Brohamual L Jackson Bandemirius III says: No wonder you lost your clothes. Here take this, it'll suit you well.")
            print("Sir Treysef Brohamual L Jackson Bandemirius III gives you chain mail armor.")
            print("Sir Treysef Brohamual L Jackson Bandemirius III says: Also take this dagger for some protection!.")
            print("Is there anything else I can help you out with brosef?")
            print("A sudden urge comes over you and you ask where the closest town is.")
            print("Sir Treysef Brohamual L Jackson Bandemirius III says 'If you head down the trail right next to my house, you'll make it to the town of Brunswick.")
            print("But be careful over there. People have been known to have been captured and never seen again in the universe.")
            print("You travel down the trail and reach the town of Brunswick.")
            print("Instantly you are spotted by a guard and he asks if you like access into the Town.")
            action = raw_input("Type: Yes or No, then press enter: ").lower().strip()
            if action == "yes":
                print("The guard gladly leads you into the town of Brunsiwck.")
                print("Once the gate closes, the guard immeadiately places you under arrest.")
                action = raw_input("Type run or stay, then press enter: ").lower().strip()
                if action == "run":
                    print("You punch the guard and run down the closest alleyway.")
                    print("Down the alleyway, you see a door, do you open it?")
                    action = raw_input("Type yes or no, then press enter: ").lower().strip()
                    if action == "yes":
                        print("You walk through the door and notice that someone obviously lives here.")
                        print("You see a very nice looking sword hanging about a fireplace.")
                        print("Do you choose to take the sword? Yes or No.")
                        action = raw_input("Type yes or No, then press enter: ").lower().strip()
                        if action == "yes":
                            player['weapon'] = weapons['sword']
                            player['armor'] = armor['chain mail armor']
                            print("You take the sword and run out of the house.")
                            print("As you are running out of the house, you step on a trap door and fall into it.")
                            print("You land in a room underground and you see a man walking towards you.")
                            print("He has a mace in his hand and looks as if he wants to kill you.")
                            fight(player, boss)
                        elif action == "no":
                            player['weapon'] = weapons['dagger']
                            player['armor'] = armor['clothes']
                            print("You take the sword and run out of the house.")
                            print("As you are running out of the house, you step on a trap door and fall into it.")
                            print("You land in a room underground and you see a man walking towards you.")
                            print("He has a mace in his hand and looks as if he wants to kill you.")
                            fight(player, boss)
                elif action == "stay":
                    player['armor'] = armor['none']
                    player['weapon'] = weapons['none']
                    print("You are stripped of all of your weapons and armor and taken to an unknown location.")
                    print("You see a man walking towards you.")
                    print("He has a mace in his hand and looks as if he wants to kill you.")
                    fight(player, boss)
            if action == "no":
                print("The guard doesnt take no as an answer and forces you into the town of Brunsiwck.")
                print("Once the gate closes, the guard immeadiately places you under arrest.")
                action = raw_input("Type run or stay, then press enter: ").lower().strip()
                if action == "run":
                    print("You punch the guard and run down the closest alleyway.")
                    print("Down the alleyway, you see a door, do you open it?")
                    action = raw_input("Type yes or no, then press enter: ").lower().strip()
                    if action == "yes":
                        print("You walk through the door and notice that someone obviously lives here.")
                        print("You see a very nice looking sword hanging about a fireplace.")
                        print("Do you choose to take the sword? Yes or No.")
                        action = raw_input("Type yes or no, then press enter: ").lower().strip()
                        if action == "yes":
                            player['weapon'] = weapons['sword']
                            player['armor'] = armor['chain mail armor']
                            print("You take the sword and run out of the house.")
                            print("As you are running out of the house, you step on a trap door and fall into it.")
                            print("You land in a room underground and you see a man walking towards you.")
                            print("He has a mace in his hand and looks as if he wants to kill you.")
                            fight(player, boss)
                        elif action == "no":
                            player['weapon'] = weapons['dagger']
                            player['armor'] = armor['clothes']
                            print("You take the sword and run out of the house.")
                            print("As you are running out of the house, you step on a trap door and fall into it.")
                            print("You land in a room underground and you see a man walking towards you.")
                            print("He has a mace in his hand and looks as if he wants to kill you.")
                            fight(player, boss)
                    if action == "no":
                        print("The guard catches you and bashes your head in for punching him in the face.")
                        print("You die....")
                elif action == "stay":
                    player['armor'] = armor['none']
                    player['weapon'] = weapons['none']
                    print("You are stripped of all of your weapons and armor and taken to an unknown location.")
                    print("You see a man walking towards you.")
                    print("He has a mace in his hand and looks as if he wants to kill you.")
                    fight(player, boss)
elif action == "trail":
    print("You proceed to walk down the trail.")
    print("You come to the front gates of a town with a big sign saying Brunswick.")
    print("You notice a guard patroling the enterance of the town.")
    print("Do you choose to Approach the guard or Sneak into the town naked?")
    action = raw_input("Type: Approach or Sneak, then press enter: ").lower().strip()
    if action == "approach":
        print("The guard instantly notices your naked body and immediately feels threatened for his manhood.")
        print("The guard strikes you down with a mighty blow with his sword.")
        print("You die.... Maybe you should have found some clothes first...")
    elif action == "sneak":
        print("You stay hidden in the dark and sneak past the guard.")
        print("You find a small hole in the side of the walls of the town that you can barely fit through.")
        print("You crawl through the hole and see a back door to a building right next to the wall.")
        print("Do you choose to walk through the door or travel into the town?")
        action = raw_input("Type door or town, then press enter: ").lower().strip()
        if action == "town":
            print("You walk into the town and people scream at the sight of your naked body.")
            print("A guard rushes you and strikes you down.")
            print("You die.... Maybe you should have found some clothes first...")
        elif action == "door":
            print("You walk through the door and notice that someone obviously lives here.")
            print("You see a very nice looking sword hanging about a fireplace.")
            print("Do you choose to take the sword? Yes or No.")
            action = raw_input("Type yes or no, then press enter: ").lower().strip()
            if action == "yes":
                player['weapon'] = weapons['sword']
                player['armor'] = armor['none']
                print("You take the sword and run out of the house.")
                print("As you are running out of the house, you step on a trap door and fall into it.")
                print("You land in a room underground and you see a man walking towards you.")
                print("He has a mace in his hand and looks as if he wants to kill you.")
                fight(player, boss)
            if action == "no":
                player['weapon'] = weapons['none']
                player['armor'] = armor['none']
                print("You take the sword and run out of the house.")
                print("As you are running out of the house, you step on a trap door and fall into it.")
                print("You land in a room underground and you see a man walking towards you.")
                print("He has a mace in his hand and looks as if he wants to kill you.")
                fight(player, boss)

