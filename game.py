# Tic Tac Toe
def gameboard():
    return ([[0,0,0],[0,0,0],[0,0,0]])

def playGame(board, user,x,y): 
    if(x>=len(board) or y>=len(board) or y<0 or x<0):
        print("Wrong Index inputs. Try again!")
        return None

    if(board[x][y] !=0):
        print('WrongInput! Try again')
        return None
    else:
        board[x][y] = user
    return board

def rowWin(board, user):    
    for x in range(len(board)):
        wins = True
        for y in range(len(board)):
            if(board[x][y] != user):
                wins = False  
                continue
        if(wins == True):
            return True        
    return wins

def colWin(board, user):   
    for x in range(len(board)):
        wins = True
        for y in range(len(board)):
            if(board[y][x] != user):
                wins= False 
                continue
        if(wins == True):
            return True         
    return wins

def diagWin(board, user):
    wins = True
    for x in range(len(board)):
        if(int(board[x][x]) != int(user)):
            wins= False  
    if(wins == True):
        return wins
    wins = True
    for x in range(len(board)):
        if(board[len(board)-x-1][x]!=user):
            wins = False      
    return wins
                   

def didPlayerWin(board, user):          
    return (rowWin(board,user) or colWin(board,user) or diagWin(board,user))    

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(str(board[i][j]), end =",")
        print()


def main():
    board = gameboard()
    win = False
    counter =0
    while(win == False):
        for user in [1,2]:
            print("Turn for user", str(user))
            print("The coordinates with 0 marked are available")
            printBoard(board)            
            print("Where do you want to place your sign? Enter x,y coordinates indexed from 0 to 2.")
            x = input("Enter x coordinate: ")
            y = input("Enter y coordinate: ")  
            board = playGame(board, user,int(x),int(y))
            if(board == None):
                return
            win = didPlayerWin(board,user)
            counter = counter+1
            if(win == True):
                printBoard(board)
                print("Player" + str(user) + "won!")
                break
            if(counter == 9):
                print("Game is a draw. No player won.")
                win = True
                break           
               
main()

