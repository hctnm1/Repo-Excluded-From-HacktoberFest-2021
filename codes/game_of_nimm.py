# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:11:11 2021

@author: Narayan soni
"""

"""
A game of nimm program which can be played again and again until we want with a simple Y input(for YES) and also, making 
error in between the game restarts it so we dont have to run the program again and again .
"""

def The_real_game():
    stones=20               #defaults to 20 stones
    player=1                #defaults player to player 1
    other_player=2          #defaults other player to player 2
    while stones>0:         #game begins
        print(f'There are {stones} stones left')
        x=int(input(f'Player {player} would you like to remove 1 or 2 stones? '))
        while x!=1 and x!=2:#while inputisinvalid
            x = int(input("Please enter 1 or 2: "))
        stones-=x           #remaining stones count
        if stones==0 or stones==-1:
            print(f'\nPlayer {other_player} wins!')
            break
        player,other_player=other_player,player    #swapping the players if game hasn't concluded
        print()                 #taking good care of the space between turns of players
def Game_of_Nimm():
    try:
        The_real_game()
    except:
        print('Bad input')
        Z=input('Would you like to try again ? Y/N : ')
        if Z=='Y':
            Game_of_Nimm()
    else:
        X=input('Would you like to play again? Y/N : ')
        if X=='Y':
            Game_of_Nimm()
if __name__ == '__main__':
    Game_of_Nimm()
