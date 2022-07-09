##name=input("ведите ваше имя: ")
##print("hello world"+" from "+ name)

import random

print("компютер загадал число от одного до десяти отгадай его")
secret_Nomber=random.randint(1, 10)
attempts= 5
while  attempts > 0 :
    user_Nomber= input("ведите ваше чсло: ")
    user_Nomber= int(user_Nomber)
    print(user_Nomber)
    if secret_Nomber > user_Nomber :
        print("секретное число больше")

    if user_Nomber > secret_Nomber :
        print ("секретное число меньше")

    if user_Nomber== secret_Nomber :
        print("ты победил")
        break
    attempts= attempts-1        

