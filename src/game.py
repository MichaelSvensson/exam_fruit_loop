from .grid import Grid
from .player import Player
from .items import Item, randomize 
from .status import print_status
from .state import game_state
from .movement import handle_movement

# Skapa en spelare på position (18, 6) för att börja i mitten
player = Player(18, 6)

# Skapa en lista för spelarens inventarier
# inventory = []

# Skapa ett rutnät (spelvärld) och konfigurera det
g = Grid()  # Skapa en instans av spelvärlden
g.set_player(player)    # Placera spelaren i spelvärlden
g.make_walls()          # Lägg till väggar i rutnätet
g.make_half_vertical_wall() # Lägg till en ny vertikal vägg i mitten av spelplanen.

randomize(g)    # Placera föremål slumpmässigt som kan plockas upp

# print_status(g) # skriva ut spelarens status och spelvärlden

# Starta spelet med en standardkommando (t.ex. "a" som betyder vänster)
command = "a"

# Huvudloopen: fortsätt spelet tills användaren trycker q eller x
while not command.casefold() in ["q", "x"]: # casefold() gör jämförelsen skiftlägesokänslig
    print_status(g) # Visa spelarens status och spelvärlden

    # Be användaren om ett kommando (WASD för rörelse, Q/X för att avsluta)
    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]    # Gör kommandot skiftlägesokänsligt och ta bara första bokstaven

    if command == "w":
        handle_movement(0, -1, player, g)  # Uppåt
    elif command == "a":
        handle_movement(-1, 0, player, g)  # Vänster
    elif command == "s":
        handle_movement(0, 1, player, g)  # Nedåt
    elif command == "d":
        handle_movement(1, 0, player, g)  # Höger
    elif command == "i":
        print(game_state['inventory'])

# Hit kommer vi när while-loopen slutar, (spelaren har tryckt Q eller X)
print("Thank you for playing!")
