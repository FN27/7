things=[['стол','стул','кровать'],['диван','*','кресло']]
while 1==1:
    for i in things:
        print(i)
    a=input('Введите номер строки')
    a=int(a)
    b=input('Введите номер столбца')
    b=int(b)

    s=input('Введите номер строки на которую будет перемещено ')
    s=int(s)
    f=input('Введите номер столбца на которую будет перемещено ')
    f=int(f)
    if things[s][f]=='*':
        c=things[a][b]

        things[s][f]=c
        things[a][b]='*'
    else:
        print('нельзя сделать такой ход')

    for i in things:
        print(i)
    if things[0][2]=='кресло' and things[1][2]=='кровать':
        print('Ты выйграл!')
        break

#сделать проверку возможности и цикл выйгрыш