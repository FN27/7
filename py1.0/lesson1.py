
def game1() :
    import random
    name= input("ведите ваше имя: ")
    letters=[]
    words= ["school","play", "life","math","game","map","car"]
    word=random.choice(words)
    need=True
    trys=input("введите количество попыток: ")
    trys=int(trys)
    while trys>0 :
        need=True
        letter= input("Введите букву: ")
        letters.append (letter)
    
        for chare in word :
            if chare in letters :
                print( chare, end = " ")
            
            else :
                need=False
                print("*", end = " ")
        

        print()



        if need==True :
            print(name+" выйграл")
            agein= input ("сыграть ещё раз: ")
            if agein == "да" :
                game1()
            break
        if letter not in word :
            trys=trys-1
        
            print("Такой буквы нет . Осталось " + str(trys) +" попытки")

            if trys==0 :
                print(name +" проиграл")
                agein= input ("сыграть ещё раз: ")
                if agein == "да" :
                    game1()
                break
        

game1()

    
        

    



##        От Vadim Gryaznykh всем:  07:59 PM
##Добавить возможность настраивать игру через ввод в консоль, спрашиваем:
##Кол-во попыток (не забудь сделать преобразование);
##Секретное слово;
##Имя игрока (при проигрыше и выигрыше программа должна говорить "Вася, ты выиграл" или "Вася, ты проиграл").


 
    

