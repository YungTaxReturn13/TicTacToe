import numpy as np
import pandas as pd

def create_board(boardsize):
    x = np.zeros((boardsize, boardsize),dtype='int')
    df=pd.DataFrame(x)
    list_of_ocupied_spots = []
    return df,list_of_ocupied_spots

def move(df,c,player,list_of_occupied_spots,total_positions):
    if player % 2 == 0:
        multiplier = -1
    else:
        multiplier = 1
    y = c[0]
    x= c[1]
    if [y,x] in list_of_occupied_spots:
        print('PLACE ALREADY TAKEN')
        return 0
    else:
        df[int(x)][int(y)] = 1*multiplier
        list_of_occupied_spots.append([y,x])
        total_positions.remove([int(y),int(x)])
        return 1

#now need to see if there is a winner

def check_winner(df):
    if (
        (df.iloc[0].sum() == 3) | (df.iloc[1].sum() == 3) | (df.iloc[2].sum() == 3) |
        (df.iloc[:,0].sum() == 3) | (df.iloc[:,1].sum() == 3) | (df.iloc[:,2].sum() == 3) |
        ((df*np.eye(3)).to_numpy().sum() ==3) | ((df*np.eye(3)[::-1]).to_numpy().sum() ==3)):
        return 1
    elif (
        (df.iloc[0].sum() == -3) | (df.iloc[1].sum() == -3) | (df.iloc[2].sum() == -3) |
        (df.iloc[:,0].sum() == -3) | (df.iloc[:,1].sum() == -3) | (df.iloc[:,2].sum() == -3) |
        ((df*np.eye(3)).to_numpy().sum() ==-3) | ((df*np.eye(3)[::-1]).to_numpy().sum() == -3)):
        return -1
    elif 0 not in df.values:
        return 'tie'
    else:
        return 0


def computers_move(total_positions):
    return total_positions[np.random.randint(len(total_positions))]