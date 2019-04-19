# This program is a tic tac toe game
from IPython.display import clear_output

# Compare values
def compareValues(valueList, value):
    return all([iterator == value for iterator in valueList])

# Print out the board
def print_board(coorArray):
    print(f"------|-------|------")
    print(f"      |       |      ")
    print(f"   {coorArray[0]}  |   {coorArray[1]}   |   {coorArray[2]}   ")
    print(f"------|-------|------")
    print(f"      |       |      ")
    print(f"   {coorArray[3]}  |   {coorArray[4]}   |   {coorArray[5]}   ")
    print(f"------|-------|------")
    print(f"      |       |      ")
    print(f"   {coorArray[6]}  |   {coorArray[7]}   |   {coorArray[8]}   ")
    print(f"------|-------|------")

def win_check(coorArray, letter):
    for i in range(7):
        if compareValues([coorArray[i], coorArray[i+1], coorArray[i+2]], letter) and i % 3 == 0: return True
    for i in range(3):
        if compareValues([coorArray[i], coorArray[i+3], coorArray[i+6]], letter): return True
    if compareValues([coorArray[0], coorArray[4], coorArray[8]], letter) or compareValues([coorArray[2], coorArray[4], coorArray[6]], letter): return True

def inputAndPlacing(coorArray, valueInput, letter):
    clear_output()
    coorArray[valueInput - 1] = letter
    print_board(coorArray)

while True:
    #while xOrO.lower() != 'x' and xOrO.lower() != 'o': xOrO = input("Please choose whether you want to be x or o\n")
    # List for the coordinates
    xInput = 0
    oInput = 0
    coorList = [' ' for number in range(9)]
    
    clear_output()
    print("Welcome to Tic Tac Toe!")
    print_board(coorList)
    
    for moves in range(5):
        while xInput < 1 or xInput > 9 or coorList[xInput - 1] != ' ':
            xInput = int(input("Please input a number between 1-9 for X\n")) if xInput < 1 or xInput > 9 else int(input(f'Square {xInput} is already taken. Choose another.'))
        
        inputAndPlacing(coorList, xInput, "x")
        
        if win_check(coorList, 'x'):
            print("X has won the game!")
            break
        
        if moves == 4:
            print("There is a tie.")
            break 
        
        while oInput < 1 or oInput > 9 or coorList[oInput - 1] != ' ':
            oInput = int(input("Please input a number between 1-9 for O\n")) if oInput < 1 or oInput > 9 else int(input(f'Square {oInput} is already taken. Choose another.'))
        
        inputAndPlacing(coorList, oInput, 'o')
        
        if win_check(coorList, 'o'):
            print("O has won the game!")
            break
        
        # Refresh the inputs
        xInput = 0
        oInput = 0

    if input("Do you want to restart? Enter y for yes\n").lower() != 'y': break
    userInput = 0
