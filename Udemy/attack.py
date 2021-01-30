import random

playerHp = 260
enemyAttackLow = 60
enemyAttackHigh = 80

while playerHp > 0:
    dmg = random.randrange(enemyAttackLow, enemyAttackHigh)
    playerHp = playerHp - dmg
    if playerHp <= 0:
        playerHp = 0
    
    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerHp)

    if playerHp == 0:
        print("You don kolo")