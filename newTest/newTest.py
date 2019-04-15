import random
def RockPaperScissors():
    shoot = random.randint(0,2)
    theList = ['Rock', 'Paper', 'Scissors']
    newHand = input("Rock, Paper, Scissors?")
    newVar = theList[shoot]
    print ('They had', newVar, 'You had ',  newHand)
    if newHand == 'Rock' and newVar == 'Scissors':
        print("You win!")
    elif newHand == 'Rock' and newVar == "Paper":
        print("Computer Wins!")
    else:
        print("Tie!")    


def main():
    RockPaperScissors()



if __name__ == "__main__":
    main()   
