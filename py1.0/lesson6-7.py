##def say_hi(name):
##    print(f'Hello{name}')
##say_hi('Вася')
##say_hi('Петя')
##say_hi('Федя')
##def area_sqeare(sideA,sideB):
##    s=sideA*sideB
##    print(f"sqear={s}")
##
##area_sqeare(8,9)

##import random
##def latry():
##    tickets=[1,55,96,27,83,21]
##    ticket=random.choice(tickets)
##    return ticket
##winner=latry()
##print(f'выйгрышный билет={winner}')

##def multylatery():
##    tickets=[3, 6, 8, 33, 65, 82, 24]
##    ticket1=random.choice(tickets)
##    tickets.remove(ticket1)
##    ticket2=random.choice(tickets)
##    return ticket1,ticket2
##winner1,winner2=multylatery()
##print (f'выйгрышный билет= {winner1}, {winner2}')
##def factorial(n):
##    y=1
##    for s in range(1,n+1):
##        y*=s
##    return y
##result=factorial(int(input()))
##print(result)
##    
#moowe=lambda a,b:a*b
#print(moowe(2,7))
mom='мама'
for new in mom:
    print(new)