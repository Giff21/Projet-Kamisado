import random
recu ={
   "request": "play",
   "lives": 3,
   "errors": "list_of_errors",
   "state":{
  "board": [[
      ["orange", ["pink", "light"]],
      ["blue", ["orange", "light"]],
      ["purple", ["green", "light"]],
      ["pink", ["red", "light"]],
      ["yellow", ["purple", "light"]],
      ["red", ["blue", "light"]],
      ["green", ["brown", "light"]],
      ["brown", ["yellow", "light"]]
    ],
    [
      ["red", "null"],
      ["orange", "null"],
      ["pink", "null"],
      ["green", "null"],
      ["blue", "null"],
      ["yellow", "null"],
      ["brown", "null"],
      ["purple", "null"]
    ],
    [
      ["green", "null"],
      ["pink", "null"],
      ["orange", "null"],
      ["red", "null"],
      ["purple", "null"],
      ["brown", "null"],
      ["yellow", "null"],
      ["blue", "null"]
    ],
    [
      ["pink", "null"],
      ["purple", "null"],
      ["blue", "null"],
      ["orange", "null"],
      ["brown", "null"],
      ["green", "null"],
      ["red", "null"],
      ["yellow", "null"]
    ],
    [
      ["yellow", "null"],
      ["red", "null"],
      ["green", "null"],
      ["brown", "null"],
      ["orange", "null"],
      ["blue", "null"],
      ["purple", "null"],
      ["pink", "null"]
    ],
    [
      ["blue", "null"],
      ["yellow", "null"],
      ["brown", "null"],
      ["purple", "null"],
      ["red", "null"],
      ["orange", "null"],
      ["pink", "null"],
      ["green", "null"]
    ],
    [
      ["purple", "null"],
      ["brown", "null"],
      ["yellow", "null"],
      ["blue", "null"],
      ["green", "null"],
      ["pink", "null"],
      ["orange", "null"],
      ["red", "null"]
    ],
    [
      ["brown", ["yellow", "dark"]],
      ["green", ["green", "dark"]],
      ["red", ["orange", "dark"]],
      ["yellow", ["purple", "dark"]],
      ["pink", ["red", "dark"]],
      ["purple", ["brown", "dark"]],
      ["blue", ["blue", "dark"]],
      ["orange", ["pink", "dark"]]
    ]
  ],
  "color": 'red',
  "current": 0,
  "players": ["LUR", "FKY"]
}
}

def FindPawn(headColor: str, iniState:list,pawnColor : str)  : #  str) -> tuple : 
    for i in range(8):
        for j in range(8):
            if iniState[i][j][1] != 'null' :
                #print(iniState[i][j][1])
                if headColor == 'null':
                    a =random.randint(0,8)
                    return print('start'), print((8,a))
                elif headColor in  iniState[i][j][1][0] and Pawncolor in  iniState[i][j][1][1] :
                    print(i,j)
                    pos =[i,j+1]
                    return print(pos)


def Sendmove(s,the_move_played):
    Move ={
   "response": "move",
   "move": the_move_played,
   "message": "Fun message"
    }
    return print(Move)


print('PLAY')
print(f"il reste {recu["lives"]} vie ")
iniState = recu['state']['board']
headColor = recu['state']['color']
print("current:",recu['state']['current'])
print(f"headColor is {headColor}, and type {type(headColor)}")
if recu['state']['current'] == 0: # ==name of AI
    Pawncolor = 'dark'
    print(f"PawnColor is {Pawncolor}, and type type(Pawncolor)")
else:
    Pawncolor = 'light'
    print(f"PawnColor is {Pawncolor}, and type {type(Pawncolor)}")
FindPawn(headColor,iniState,Pawncolor)

#FindPawn(headColor,iniState,Pawncolor)