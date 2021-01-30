from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


#create black magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

#create white magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
highPotion = Item("High Potion", "potion", "Heals 100 HP", 100)
superPotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixir = Item("Elixir", "elixir", "Fully restores HP/HP of one party member", 9999)
highElixir = Item("Mega Elixir", "elixir", "Fully restores party's HP/HP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_magic = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_magic = [fire, meteor, cure]
player_items = [{"item": potion, "quantity": 15}, {"item": highPotion, "quantity": 5}, {"item": superPotion, "quantity" : 5},
                {"item": elixir, "quantity": 5}, {"item":highElixir, "quantity": 6}]
player1 = Person("Valos :", 3260, 132, 300, 34, player_magic,player_items)
player2 = Person("Egoli :", 3960, 169, 300, 34, player_magic,player_items)
player3 = Person("Chris :", 4260, 355, 400, 34, player_magic,player_items)

enemy1 = Person("Rasta :", 1250, 130, 560, 325, enemy_magic,[])
enemy2 = Person("Julio :", 17200, 855, 525, 205, enemy_magic,[])
enemy3 = Person("Motep :", 1250, 135, 555, 305, enemy_magic,[])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]



running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("=================================")

    for player in players:
        print("\n\n")
        print("NAME                    HP                                     MP")
        player.get_stats()

    for enemy in enemies:
        print("\n\n")
        enemy.get_enemy_stats()

    for player in players:
        
       
        player.choose_action()
        choice = input("Choose action:")
        index = int(choice) - 1
        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_enemy(enemies)
            enemies[enemy].take_damage(dmg)
            print(player.name + " attacked "+ enemies[enemy].name +  "for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " has died")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()
            if spell.cost > current_mp:
                print(bcolors.FAIL + "\n Not enough MP\n"+ bcolors.ENDC)
                continue

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP."+bcolors.ENDC)
                player.reduce_mp(spell.cost)
            elif spell.type == "black":
                enemy = player.choose_enemy(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg)," points of damage to "+ enemies[enemy].name + "HP."+bcolors.ENDC)
                player.reduce_mp(spell.cost)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died")
                    del enemies[enemy]
        
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose Item: ")) - 1
            
            if item_choice == -1:
                continue
            
            if player.items[item_choice]['quantity'] == 0:
                print(bcolors.FAIL + "\n" + "None left...." + bcolors.ENDC)
                continue

            item = player.items[item_choice]['item']
            player.items[item_choice]['quantity'] -= 1

            
            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + "heals for ", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixir":
                if item.name == "Mega Elixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                elif item.name == "Elixir":
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + "fully restores HP/MP " + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_enemy(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop)," points of damage to "+ enemies[enemy].name + "HP."+bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died")
                    del enemies[enemy]

    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1
    
    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1
    
    if defeated_enemies == 2:
         print(bcolors.OKGREEN + "YOU WIN!" + bcolors.ENDC)
         running = False
    
    if defeated_players == 2:
        print(bcolors.FAIL + "YOUR ENEMIES HAVE DEFEATED YOU" + bcolors.ENDC)
        running = False
   
    print("\n " + " ENEMIES ADVANCE")
    for enemy in enemies:

        enemy_choice = random.randrange(0,2)
        if enemy_choice == 0:
            enemy_damage = enemy.generate_damage()
            enemy_target = random.randrange(0,3)
            players[enemy_target].take_damage(enemy_damage)
            print(enemy.name + " attacks "+ players[enemy_target].name + " for ", enemy_damage)
            print("--------------------------------------")

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)
            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals "+ enemy.name+ " for", str(magic_dmg), "HP."+bcolors.ENDC)
                player.reduce_mp(spell.cost)
            elif spell.type == "black":
                enemy_target = random.randrange(0,3)
                players[enemy_target].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + enemy.name + "'s " + spell.name + " deals", str(magic_dmg)," points of damage to "+ players[enemy_target].name + "HP."+bcolors.ENDC)
                player.reduce_mp(spell.cost)
                if players[enemy_target].get_hp() == 0:
                    print(players[enemy_target].name + " has died")
                    del players[enemy_target]

    #print("Enemy HP: ",bcolors.FAIL + str(players[enemy_target].get_hp()) + "/" + str(players[enemy_target].get_max_hp()) + bcolors.ENDC)

    