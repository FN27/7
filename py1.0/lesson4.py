import random
points= 100
huugy=int(input("Ваша ставка "))

nombers=random.randint(2,12)
player_nomber=int(input("введите ваше число(от 2 до 12): "))
while points>0:

    if nombers<7:
        
    if player_nomber>7 and nombers>7:
        huugy=huugy*2 + points

    if player_nomber<7 and nombers<7:
        points=huugy*2 +points

    if player_nomber==nombers:
        points=huugy*4 +  points

    else:
        points=points-huugy

        
        
        

    
        
