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

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
         ]


def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player
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
    x, y = player
    if x == 0:
        moves.remove("LEVO")
    elif x == 4:
        moves.remove("DESNO")
    if y == 0:
        moves.remove("GOR")
    elif y == 4:
        moves.remove("DOL")
    return moves

def draw_map(player):
    print(" _"*5)
    tile = "|{}"
    for cell in CELLS:
        x,y = cell
        if x<4:
            line_end=""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end = line_end)


def game_loop():
    monster, door, player = get_locations()
    while True:
        draw_map(player)
        moves = get_moves(player)
        print("Trenutno se nahajaš v prostoru {}".format(player))  # fill with player position
        print("Lahko se premakneš {}".format(", ".join(moves)))  # fill with available moves
        print("Napiši IZHOD za izhod")

        move = input("> ")
        move.upper()

        if move == 'IZHOD':
            break
        elif move in moves:
            player = move_player(player, move)
        else:
            print("Napačna poteza!")
            continue
        if player == door:
            print("Bravo zmagal si!")
            break
        if player == monster:
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
