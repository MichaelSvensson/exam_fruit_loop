from .state import game_state  

# Funktion för att skriva ut spelarens status och spelvärlden
def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {game_state['score']} points.")  # Visa spelarens aktuella poäng
    print(game_grid)    # Visa spelvärlden