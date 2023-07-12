
Field = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']]

count = 1

print('Крестики нолики')
print('Для хода вводите числа через пробел')
print('Строка - Столбец')
def show_Field(Field):
    print(' ',0,1,2)
    for i in range (0,3):
        print(i, end=' ')
        for j in range(0,3):
            print(Field[i][j], end=' ')
        print()

def turn(Field):
    while True:
        TurnXY = input().split()
        if len(TurnXY) == 2:
            x, y = TurnXY
            if x.isdigit() and y.isdigit():
                x, y = int(x), int(y)
                if x in range(0,3) and y in range(0,3) and Field[x][y] == '-':
                    break
                else:
                    print('Некорректный Ввод ')
                    print('Попробуйте снова: ')
            else:
                print('Некорректный Ввод ')
                print('Попробуйте снова: ')
        else:
            print('Введите 2 числа')

    return x, y

def If_Win(Field, symbol):

    Check = False
    if (Field[0][0] == Field[0][1] == Field[0][2] == symbol) or (Field[1][0] == Field[1][1] == Field[1][2] == symbol) or (Field[2][0] == Field[2][1] == Field[2][2] == symbol) or (Field[0][0] == Field[1][1] == Field[2][2] == symbol) or (Field[0][2] == Field[1][1] == Field[2][0] == symbol) or (Field[0][0] == Field[1][0] == Field[2][0] == symbol) or (Field[0][1] == Field[1][1] == Field[2][1] == symbol) or (Field[0][2] == Field[1][2] == Field[2][2] == symbol):
        Check = True
    return Check


while True:

    show_Field(Field)
    if count % 2 == 0:
        print(' Ходит Нолик ')
        x,y = turn(Field)
        Field[x][y] = 'O'
        if If_Win(Field, 'O'):
            print('Победил Нолик')
            show_Field(Field)
            break
    else:
        print(' Ходит Крестик ')
        x, y = turn(Field)
        Field[x][y] = 'X'
        if If_Win(Field, 'X'):
            print('Победил Крестик')
            show_Field(Field)
            break

    if count == 9:
        print('Ничья')
        show_Field(Field)
        break

    count += 1

















