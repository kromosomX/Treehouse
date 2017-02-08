import random
import os

# draw grid
# pick random location for player
# pick random location for exit door
# pick random location fro the monster
# draw player in the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw grid

# CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
#         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
#         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
#         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
#         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
#         ]

CELLS = []
XX = 5
YY = 5


def build_maze():
    for y in range(XX):
        for x in range(YY):
            CELLS.append((x, y))

def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player["ZADNJI"]
    if move == "LEVO":
        x -= 1
    elif move == "DESNO":
        x += 1
    elif move == "GOR":
        y -= 1
    elif move == "DOL":
        y += 1
    return x, y


def get_moves(player):
    moves = ["LEVO", "DESNO", "GOR", "DOL"]
    x, y = player["ZADNJI"]
    if x == 0:
        moves.remove("LEVO")
    elif x == XX - 1:
        moves.remove("DESNO")
    if y == 0:
        moves.remove("GOR")
    elif y == YY - 1:
        moves.remove("DOL")

    return moves

def draw_map(player):
    print(" _" * XX)
    tile = "|{}"
    for cell in CELLS:
        x,y = cell
        if x < XX - 1:
            line_end=""
            if player["ZADNJI"] == cell:
                output = tile.format("X")
            elif cell in player:
                output = tile.format(".")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if player["ZADNJI"] == cell:
                output = tile.format("X|")
            elif cell in player:
                output = tile.format(".|")
            else:
                output = tile.format("_|")
        print(output, end = line_end)


def game_loop():
    build_maze()
    monster, door, player_start = get_locations()
    player = {player_start: ".", "ZADNJI": player_start, "POSAST": monster}
    while True:
        draw_map(player)
        moves = get_moves(player)
        print("Trenutno se nahajaš v prostoru {}".format(player["ZADNJI"]))  # fill with player position
        print("Lahko se premakneš v te smeri {}".format(", ".join(moves)))  # fill with available moves
        print("Napiši IZHOD za izhod")
        print(CELLS)
        move = input("> ")
        move = move.upper()

        if move == 'IZHOD':
            break
        elif move in moves:
            premik = move_player(player, move)
            player[premik] = "."
            player["ZADNJI"] = premik
        else:
            print("Napačna poteza!")
            continue
        if player["ZADNJI"] == door:
            print("Bravo zmagal si!")
            break
        if player["ZADNJI"] == monster:
            print("BRUHAHA!!! Pojedla te je pošast!")
            break
        print("\n" * 100)


print("\n" * 100)
print("Dobrodošel v grajski ječi!")
input("Pritisni 'Enter' za začetek igre")
game_loop()

    # good move? change the player position
    # bad move? don't change anything
    # on the door? they win
    # on the monster? they loose
    # otherwise, loop back around
