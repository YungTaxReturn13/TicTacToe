import numpy as np
import functions

boardsize = 3

total_positions = []
for i in range(boardsize):
    for n in range(boardsize):
        total_positions.append([i,n])
print(total_positions)
df, list_of_ocupied_spots = functions.create_board(boardsize)

main_flag = True


random = np.random.randint(1,3)
player = random
computers_move = functions.computers_move(total_positions)
if random == 1:
    print('You are player X!')
    print(df)
    initial_move = input('X goes first. Enter in the row then column separated by a comma:')
    value = functions.move(df,initial_move.split(','),player,list_of_ocupied_spots,total_positions)
    print(f'{df}\n'
          f'---------------------------------------------------------------------------------------------------')
else:
    print('you are player O')


while main_flag == True:
    while True:
        player +=1
        if player %2 ==0:
            move = input(f'It is your turn. Please enter the row and column separated by a comma').split(',')
        else:
            move = functions.computers_move(total_positions)
        if move in list_of_ocupied_spots:
            while True:
                move = input(f'It is your turn. Please enter a valid row and column separated by a comma').split(',')
                value = functions.move(df,move,player,list_of_ocupied_spots,total_positions)
                if value == 0:
                    pass
                else:
                    break
        else:
            functions.move(df,move,player,list_of_ocupied_spots,total_positions)
            print(f'{df}\n'
          f'---------------------------------------------------------------------------------------------------')
            break

    if functions.check_winner(df) == 1:
        print('X WINS')
        break
    elif functions.check_winner(df) == -1:
        print('O WINS')
        break
    elif functions.check_winner(df) == 'tie':
        print('TIE GAME')
        break
    else:
        pass
#




