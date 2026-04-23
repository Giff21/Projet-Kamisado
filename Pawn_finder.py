import random
# JF, you can put your stuff here in order to find the tile to play
#1)find the position of all the pawn, light or dark and if we are dark(0) or light(1)
#2)the fonction must return a list of the pawn we want to play [initial_rows, initial_column] first and then the pawn we must play according 
# to the color the enemy ended
#3)later give me the color of the ennemis to pervent Flo to tell our pawn to go on the color that will get the will to the ennemi

def FindPawn(boardState) -> list:
    playerPawn = []
    ennemiPawn = []
    iniState = boardState['board']
    headColor = boardState['color']
    current = Find_current(boardState)
    if current == 0:
        Pawncolor = 'dark'
        ennemi = boardState['players'][1]
    else:
        Pawncolor = 'light'
        ennemi = boardState['players'][0]

    if headColor == None or headColor == 'n':
        if current == 0:
            a =random.randint(0,7)
            print(f"[7,{a}]")
            return [7,a]
        else:
            a = random.randint(0,7)
            print(f"[0,{a}]")
            return [0,a]
        
    for i in range(8):
        for j in range(8):
            case = iniState[i][j][1]
            if isinstance(case, list):
                color, pawn = case
                if headColor == color and Pawncolor == pawn :
                    print(f"[{i},{j}] is {headColor} and {Pawncolor}")
                    pos =[i,j]
                if Pawncolor == pawn:
                    playerPawn.append(iniState[i][j])
                if Pawncolor != pawn and Pawncolor != 'n':
                    ennemiPawn.append(iniState[i][j])

                
    return pos
                
    raise ValueError("no Pawn found :(")

def Find_current(boardState):
    current = boardState['current']
    return current

def Ennemi_finder():
    pass