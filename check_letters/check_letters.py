import random
def hangman():
    new_list = {3, 6, 9]
    randomdifficulty = random.randint(0, 3)
    
    difficulty = new_list[randomdifficulty]
    
    if difficulty == 9:
        print "Easy"
    elif difficulty == 6:
        print = "Medium"
    else:
        print = "Hard"      
    return difficulty

def word():
    the_word = input("what is the word?")
    return the_word

def letter_guess():
def main():
    print('test')
    print(hangman())

if __name__ == "__main__":
    main()
