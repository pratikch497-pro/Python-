score=0 #In every code starting it will be at zero. 
a = str(input('what is your name:  '))
print(f'{a}! welcome to game.')
while True:    
    import random #random is a built-in module is use to pick randomly.
    list_of_the_game_stone_paper_scissor=(['stone','paper','scissor']) #it is the list of the game.
    c = random.choice(list_of_the_game_stone_paper_scissor) #it the random.choice who will choose the string.
    print ('i have choosed.') #computer choice.
    d = str(input('what you have choosed: ')) #for input what you choosed.
    if  d==' ' or d!=(list_of_the_game_stone_paper_scissor):
          #it is for the person if some one doesn't give any input or given wrong input according to list.
        print('ERROR')
        print ('run again.')
        break 

    else:
        if d==c:
            #it will say you win the game.
            print('YOU WIN🏆.')
            score+=1#it will add up the score how much you win.
        else:
            #it will say you lose the game.
            print('YOU LOSE.')  
     
        if d=='exit':
              #it will break when type exit and imparts accuracy.
            print('--------:the accuracy-------')
            print(f'{a}! score is {score}.')
            print ('thanks for playing it')
            break #it is for stop and break the continuously path.