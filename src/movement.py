from .player import Player
from .items import Item
from .grid import Grid
from .state import game_state

def handle_movement(dx, dy, player, grid):
    if player.can_move(dx, dy, grid):
        if player.can_move(dx, dy, grid):  # Kolla kollision först. Vid kollision returneras false och spelarens position uppdateras ej.
            maybe_item = grid.get(player.pos_x + dx, player.pos_y + dy)
        # G. The floor is lava 
        game_state['score'] -= 1
        player.move(dx, dy)
        if isinstance(maybe_item, Item):
            # Add item to inventory
            game_state['inventory'].append(maybe_item.name)
            if maybe_item.name in ["carrot", "radish", "meatball"]:
                game_state['score'] += maybe_item.value
                print(f"You found a {maybe_item.name}, +{maybe_item.value} points.") 
            elif maybe_item.name in ["apple", "strawberry", "cherry", "watermelon", "cucumber"]:
                game_state['score'] += maybe_item.value + 10
                print(f"You found a {maybe_item.name}, +{(maybe_item.value+10)} points.")
            grid.clear(player.pos_x, player.pos_y)

