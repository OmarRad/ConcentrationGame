import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    print("Shuffling the deck...\n")
    Done = []
    New = []
    x = len(deck)
    while len(New) < x:
        y = random.randint(0,x-1)
        if y not in Done:
            New.append(deck[y])
            Done.append(y)
    for i in range(len(New)):
        deck[i] = New[i]
    return None
    # YOUR CODE GOES HERE

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')
    print('\n')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    discovered = [int(i) for i in discovered]
    for i in range(len(original_board)):
        if i in discovered:
            print('{0:4}'.format(original_board[i]), end=' ')
        elif (i == p1 - 1 or i == p2 - 1) and p1 != p2:
            print('{0:4}'.format(original_board[i]), end=' ') 
        else:
            print('{0:4}'.format('*'), end=' ')
    print()
    for i in range(len(original_board)):
        print('{0:4}'.format(str(i+1)), end=' ')
    print('\n')
    # YOUR CODE GOES HERE
    
def ascii_name_plaque(name:str)->str:
    '''This is a function that takes a name(a string) inputted by the user and
    returns a plaque in the form of a string showcasing the name inputted by the user.'''
    return print("*" * 10 + "*"*len(name) + "\n*" + " " * (len(name) + 8) + "*\n*  __" + name + "__  *\n*" + " " * (len(name) + 8) + "*\n" + "*" * 10 + "*"*len(name))
#############################################################################
#   FUNCTIONS FOR OPTION 2 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarily be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]
    playable_board = l.copy()
    x = 0
    y = 0
    m = l.count('*')
    while x < m:
        playable_board.remove("*")
        x += 1
    while y < len(playable_board):
        if playable_board.count(playable_board[y]) % 2 == 1:
            playable_board.remove(playable_board[y])
        else:
            y += 1
    playable_board.sort()
    # YOUR CODE GOES HERE
    
    return playable_board


def is_rigorous(l):
    '''list of str->bool
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''
    if len(l) == 0:
        return True
    for i in l:
        if l.count(i) > 2:
            return False
    return True
        
    # YOUR CODE GOES HERE
 
                
        

####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")

    # this is the funciton that plays the game
    # YOUR CODE GOES HERE
    
    discovered = []
    p1,p2 = 1,1
    num_guesses = 0
    print_revealed(discovered,p1,p2,board)
    while len(discovered) < len(board):
        p1 = int(input("\nEnter two distinct positions that you want revealed.\ni.e two integers in the range [1, " + str(len(board)) + "]\nEnter position 1: "))
        p2 = int(input("Enter position 2: "))
        discovered = [int(i) for i in discovered]
        if (p1 - 1 in discovered or p2 - 1 in discovered) and p1 == p2:
            print("One or both of your chosen positions has already been paired.\nYou chose the same positions.\nPlease try again. This guess did not count. Your current number of guesses is " + str(num_guesses) + '.')
        elif p1 - 1 in discovered or p2 - 1 in discovered:
            print("One or both of your chosen positions has already been paired.\nPlease try again. This guess did not count. Your current number of guesses is " + str(num_guesses) + '.')
        elif p1 == p2:
            print("You chose the same positions.\nPlease try again. This guess did not count. Your current number of guesses is " + str(num_guesses) + '.')
        elif p1 != p2 and p1-1 not in discovered and p2 - 1 not in discovered:
            if board[p1-1] == board[p2-1]:
                discovered.append(p1-1)
                discovered.append(p2-1)
            num_guesses += 1
            discovered = [str(i) for i in discovered]
            print_revealed(discovered,p1,p2,board)
            wait_for_player()
            print("\n"*40)
            discovered = [str(i) for i in discovered]
            p1,p2 = 1,1
            print_revealed(discovered,p1,p2,board)
    
    best_guess = len(board)/2
    print("\n" * 30 + "Congratulations! You completed the game with " + str(num_guesses) + " guesses. That is " + str(int(num_guesses - best_guess)) + " more than the best possible")
        
        
        
    



#main
if __name__ == "__main__":  
# YOUR CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE
    ascii_name_plaque("Welcome to my Concentration Game")
    choice = int(input("Would you like (enter 1 or 2 to indicate your choice):\n(1) me to generate a rigorous deck of cards for you\n(2) or, would you like me to read a deck from a file?\n"))
    while choice != 1 and choice != 2:
        choice = int(input(str(choice) + " is not an existing option. Please try again. Enter 1 or 2 to indicate your choice\n"))


# YOUR CODE FOR OPTION 1 GOES HERE
# In option 1 somewhere you need to and MUST have a call like this:
# board=create_board(size)
    if choice == 1:
        print("You chose to have a rigorous deck generated for you")
        size = int(input("\nHow many cards do you want to play with?\nEnter an even number between 0 and 52: "))
        while size % 2 != 0 or size <= 0 or size > 52:
            size = int(input("\nHow many cards do you want to play with?\nEnter an even number between 0 and 52: "))
        board = create_board(size)
        shuffle_deck(board)
        wait_for_player()
        print("\n"*40)
        if len(board) == 0:
            print("The resulting board is empty.\nPlaying Concentration game with an empty board is impossible.\nGood bye")
        else:
            play_game(board)




# YOUR CODE FOR OPTION 2 GOES HERE
# In option 2 somewhere you need to and MUST have the following 4 lines of code one after another
#
    elif choice == 2:
        print("You chose to load a deck of cards from a file")
        file=input("Enter the name of the file: ")
        file=file.strip()
        board=read_raw_board(file)
        board=clean_up_board(board)
        if is_rigorous(board) == False:
            ascii_name_plaque("This deck now playable but not rigorous and it has " + str(len(board)) + " cards.")
        else:
            ascii_name_plaque("This deck now playable and rigorous and it has " + str(len(board)) + " cards.")
        wait_for_player()
        print("\n"*40)
        shuffle_deck(board)
        wait_for_player()
        print("\n"*40)
        if len(board) == 0:
            print("The resulting board is empty.\nPlaying Concentration game with an empty board is impossible.\nGood bye")
        else:
            play_game(board)
