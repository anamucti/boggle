
import random
import time


def main():
    '''This is the main function that gets executed when calling boggle.py'''
    print("Hello World!")

def greet_user(name):
    '''Greet the user'''
    '''name arg of the user'''
    print(f'Guatsup {name}')

def generate_dummy_board():
    '''Generate a dummy board'''
    print(' ----- ----- ----- -----')
    print('|  A  |  I  |  N  |  Q  |')
    print('----- ----- ----- -----')
    print ('|  B  |  P  |  U  |  R  |')
    print('----- ----- ----- -----')
    print('|  T  |  M  |  A  |  E  |')
    print('----- ----- ----- -----')
    print('|  X  |  G  |  U  |  D  | ')
    print('----- ----- ----- -----')

def generate_random_board():
    '''Generate a random board'''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(random.choice(letters))
    print(' ----- ----- ----- -----')
    print(f'|  {random.choice(letters)}  |  {random.choice(letters)}  |  {random.choice(letters)}  |  {random.choice(letters)}  |')
    print(' ----- ----- ----- -----')
    print(f'|  {random.choice(letters)}  |  {random.choice(letters)}  |  {random.choice(letters)}  |  {random.choice(letters)}  |')
    print(' ----- ----- ----- -----')
    print(f'|  {random.choice(letters)}  |  {random.choice(letters)}  |  {random.choice(letters)}  |  {random.choice(letters)}  |')
    print(' ----- ----- ----- -----')
    print(f'|  {random.choice(letters)}  |  {random.choice(letters)}  |  {random.choice(letters)}  |  {random.choice(letters)}  |')
    print(' ----- ----- ----- -----')   

def generate_random_board_loop_row():
    '''Generate a random board'''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(1,5):
        print(' ----- ----- ----- -----')
        print(f'|  {random.choice(letters)}  |  {random.choice(letters)}  |  {random.choice(letters)}  |  {random.choice(letters)}  |')
    print(' ----- ----- ----- -----')

def generate_random_board_loop():
    '''Generate a random board'''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(1,5):
        print(' ----- ----- ----- -----')
        row = ''
        for col in range (1,5):
            row = row + f'|  {random.choice(letters)}  ' 
        row = row + '|'
        print(row)
    print(' ----- ----- ----- -----')
       
    
def random_dice_list_first():
    '''Get random list of 16 dices with valid random letters'''
    dices = ['ARHSDE','FUAARB','IOTALG','UOEEOC','FOMTUI','OODBLG','RPSZTL','EBIOUA','CAREME','RSJEFI','NSXJAH','UVDQBC','NBIMEE','BAANIT','EPVOCU','SCAAPT']
    random.shuffle(dices)
    for r in range(1,5):
        print(' ----- ----- ----- -----')        
        row = ''
        for col in range (1,5):
            diceNumber = int((r-1)*4+col-1)
            row = row + f'|  {random.choice(dices[diceNumber])}  '
        row = row + '|'
        print(row)
        
    print(' ----- ----- ----- -----')

def random_dice_list():
    '''Get random list of 16 dices with valid random letters'''
    dices = ['ARHSDE','FUAARB','IOTALG','UOEEOC','FOMTUI','OODBLG','RPSZTL','EBIOUA','CAREME','RSJEFI','NSXJAH','UVDQBC','NBIMEE','BAANIT','EPVOCU','SCAAPT']
    random.shuffle(dices)
    for r in range(1,5):
        print(' ----- ----- ----- -----')        
        row = ''
        for col in range (1,5):
            # Use dices as a bag, and remove each time one dice from the bag
            # ['AB', 'CD'].pop() --> returns 'CD' and the list is now only ['AB']
            row = row + f'|  {random.choice(dices.pop())}  '
        row = row + '|'
        print(row)
        
    print(' ----- ----- ----- -----')

# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('\n\n\n\n\n\n\n\n\n\n\n\nTIME IS OVER!!!\n\n\n**********')
  
  



if __name__ == "__main__":
    #main()
    greet_user('Ana' + ' Guerro')
    #generate_random_board()
    # generate_random_board_loop()
    # input time in seconds
    t = input("Enter the time in seconds: ")    
    # function call    
    random_dice_list()
    countdown(int(t))



    