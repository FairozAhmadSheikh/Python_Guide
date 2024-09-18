"""Closure is a function that has access to the scope of its  parent function, after the function has returned """


# Example of closure

def parent_function(player_name,coins):
    def play_game():
        nonlocal coins
        coins-=1
        
        if coins>1:
            print("Coins left for ", player_name,": ", coins)
        elif coins==1:
            print("Single coin left for ",player_name)
        else:
            print("Out of coins You need to recharge ",player_name)
    return play_game
feroz=parent_function("Fairoz",5)
sameer=parent_function("Sameer",3)
feroz()
feroz()
feroz()
sameer()
feroz()
feroz()
sameer()
sameer()