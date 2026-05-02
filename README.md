# Projet: Kamisado
This project is developed by NOLLET Jean-François 24087 and JURQUET Florian 24092

<p align="center">
<img src="Projet-Kamisado/public/Kamisado-image.png" width="300" height="300" />
</p>

This IA is design to play autonomously and make the best move possible in the board game Kamisado. Kamisado is a turn-based game where the goal is to arrive at the opponent's starting line while respecting [these rules](https://www.yucata.de/en/Rules/Kamisado)

## Requirements
Pre-installed python libraries that we use: 
- `json`
- `random`
- `socket`
- `struct`
- `time`

You can intall the pytest testing package with this command:

```python
pip install -r requirements.txt
```
## Algorithm
Our AI uses the Negamax algorithm with alpha beta pruning and limited depth search to find the best move possible while minimizing the opponent's progression.

Firstly, the algorithm read the board and find all the legal moves that our pawn can do. Then, by identifying the color of the tile on which we place our pawn, we can find the opponenet's pawn and predict its moves. 

By evaluating the distance from the winning line, we can minimize our distance from the targete position and maximize the ennemy distance. The AI calculates the cost of each move according to these distances. It takes into account all of our possible moves and the opponent’s responses, and use the alpha beta prunning to find the best move as fast as possible. We limited our depth search to a 3 second limit imposed on us.

Our algorithm repeats this process for each position played and picks the move with the highest positive score.

## Setup
### Server

Start the server that will take care of the board interactions by cloning this [repository](https://github.com/qlurkin/PI2CChampionshipRunner) in VScode where you can find the general instructions. 
There you can have the general instructions but if you want more informations relative to the game click [here](https://github.com/qlurkin/PI2CChampionshipRunner/tree/main/games/kamisado)

type this command in the terminal to start the server (must be in PI2CChampionShipRunner folder):
```python
python server.py kamisado
```

### Algorithm

In ai_starter.py:
- Set the IP of the server
- Set an available clientPort
- Indicate if you want the smart (True) or rnadom bot (False)

type this command in the terminal to start the first AI (must be in Projet-Kamisado folder):
```python
python ai_starter.py
```
In ai2_starter.py:
- Set the same IP of the server
- Set another available clientPort
- Indicate if you want the smart (True) or rnadom bot (False)

type this command in another terminal to start the second AI (must be in Projet-Kamisado folder):
```python
python ai2_starter.py
```

You will normally see the two IA connected on the server
