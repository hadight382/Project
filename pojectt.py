#Hadi Ghodrati
#ID = 401130683
###############

from random import randint

while 1 :
    
    winning_you = 0
    winning_computer = 0
    winning_streak_point_computer = 0
    winning_streak_point_you = 0
    winning_streak_you = 1 
    winning_streak_computer = 1
    win_counter_computer = 0
    win_counter_you = 0


    while 1 :

    
        print(f"computer : {winning_computer} | you : {winning_you} ")
        if winning_streak_computer>1 :
            print(f"Computers winning streak: {winning_streak_computer} ")
        elif winning_streak_you>1 :
            print(f"Your winning streak: {winning_streak_you} ")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")

        if winning_computer-winning_you > 49:
            break;
        elif winning_you-winning_computer > 49:
            break;
        if winning_streak_computer==5:
            break;
        elif winning_streak_you==5:
            break;


        
        player = input("make your move(sang,kaghaz,gheychi)  (press q to end the game) : ").lower()
        if player == "q":
            break;
        
        computer=randint(1,3)
        if computer == 1 :
            computer_move="sang"
        elif computer == 2 :
            computer_move="kaghaz"
        elif computer == 3 :
            computer_move="gheychi"
        print(f"computer_move : {computer_move}")
        
        
        
        

        if player == computer_move :
            print("tied")
        elif player == "sang":
            if computer_move == "kaghaz" :
                print("computer won!")
                if winning_streak_point_computer > 0 :
                    winning_streak_point_computer *= 2
                    winning_streak_computer+=1
                    winning_computer += winning_streak_point_computer
                else:
                    winning_streak_you = 1
                    winning_streak_point_you=0
                    winning_computer += 1
                    winning_streak_point_computer += 1
            elif computer_move == "gheychi" :
                print("you won!")
                if winning_streak_point_you > 0 :
                    winning_streak_point_you *= 2
                    winning_streak_you += 1
                    winning_you += winning_streak_point_you
                else:
                    winning_streak_computer = 1
                    winning_streak_point_computer = 0
                    winning_you += 1
                    winning_streak_point_you += 1
        elif player == "kaghaz" :
            if computer_move == "sang" :
                print("you won!")
                if winning_streak_point_you > 0 :
                    winning_streak_point_you *= 2
                    winning_streak_you += 1
                    winning_you += winning_streak_point_you
                else :
                    winning_streak_computer = 1
                    winning_streak_point_computer = 0
                    winning_you += 1
                    winning_streak_point_you += 1
            elif computer_move == "gheychi" :
                print("computer won!")
                if winning_streak_point_computer > 0 :
                    winning_streak_point_computer *= 2
                    winning_streak_computer += 1
                    winning_computer += winning_streak_point_computer
                else:
                    winning_streak_you = 1
                    winning_streak_point_you=0
                    winning_computer += 1
                    winning_streak_point_computer += 1
        elif player == "gheychi" :
            if computer_move == "sang" :
                print("computer won!")
                if winning_streak_point_computer > 0 :
                    winning_streak_point_computer *= 2
                    winning_streak_computer += 1
                    winning_computer += winning_streak_point_computer
                else :
                    winning_streak_you = 1 
                    winning_streak_point_you = 0
                    winning_computer += 1
                    winning_streak_point_computer += 1
            elif computer_move == "kaghaz" :
                print("you won!")
                if winning_streak_point_you > 0 :
                    winning_streak_point_you *= 2
                    winning_streak_you += 1
                    winning_you += winning_streak_point_you
                else :
                    winning_streak_computer = 1
                    winning_streak_point_computer=0
                    winning_you += 1
                    winning_streak_point_you += 1
        
        else :
            print ("something went wrong")
        
                
    print(f"final scores: computer ---> {winning_computer} | you ---> {winning_you} ")        

    if winning_you-winning_computer > 49 or winning_streak_you==5 :
        win_counter_you += 1 
        print("you are the champion!!!") 
        if winning_streak_you==5:
            print ("You won 5 times in a row.")
    elif winning_computer-winning_you > 49 or winning_streak_computer==5 :
        win_counter_computer += 1
        print("you are the loser!!!")
        if winning_streak_computer==5:
            print("The computer won 5 times in a row.")
    else :
        if winning_computer > winning_you :
            print("the game is not over but computer won!")
        elif winning_computer < winning_you :
            print("the game is not over but you won!")
        else :
            print("the game is not over but you tied!")

    Ans=input("If you want to play again press R and if you want to end the game press Q. ").lower()
    if Ans == "r" :
        continue
    elif Ans == "q":
        print("----------------------------------------------------")
        print(f"You won {win_counter_you} times. ")
        print(f"Computer won {win_counter_computer} times. ")
        print("----------------------------------------------------")
        break
    
