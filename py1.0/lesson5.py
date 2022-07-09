

##dels=["clean", "vacuumn", "lay", "clear"]
##dels[0] = 'emty'
####print(dels)
##dels.append('emty')
##dels.remove('clean')
##delnum=dels.index('lay')
##ddtf=dels.pop(delnum)
##print(dels)
##print(ddtf)



##games=["fallout4","fortnite","cs-go", "owerwatch","dota2" ]
##game=input('введите игру')
##if game in games:
##    print("я играл")
##else :
##    print("я не играл")
##    games.append(game)
##    print('добавленна игра'+game)
##print(games)
##lieng=len(games)
##for i in range(lieng):   
##    print(f"{i+1}.{games[i]}")
##for game in games:
##    print(game)


import random
pril=['мудрый ','крутой ','дерзкий ','счастливый ','дикий ','гордый ']
anymal=['орёл','бобёр','заяц','волк','суслик','бык','ястреб']
f_name=random.choice(pril)
s_name=random.choice(anymal)
print(f'в племяни индейцев тебя бы звали       {f_name} {s_name}')
