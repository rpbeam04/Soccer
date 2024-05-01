# Beam Brackets Soccer Simulation

# Imports

# Initial Phase

# Formation
print("Input a custom formation in the format n-n-n-n...")
valid_formation = False
while not valid_formation:
    formation = input("Formation: ")
    formation = formation.split("-")
    if len(formation) < 2:
        print("ERROR: Formation must have at least 2 rows.")
        continue
    flag = False
    for i,row in enumerate(formation):
        try:
            formation[i] = int(row)
        except:
            print("ERROR: Only type integers and dashes, with integer ends.")
            flag = True
            break
    if flag:
        continue
    if sum(formation) != 10:
        print("ERROR: Formation must be for 10 players.")
        continue
    valid_formation = True
print(formation)

def print_soccer_formation(formation):
    # Define the positions of players in the formation
    goalkeeper = "GK"
    defenders = ["igqprioh", "CB", "iqpguohiqhihb", "RB"]
    midfielders = ["LM", "CM", "RM"]
    attackers = ["LW", "ST", "RW"]

    # Print the formation with absolute positions
    print("Soccer Formation:", formation)
    print(f"{'':<10}{'':<5}{'':<5}{'':<5}{'':<5}{'':<5}")
    print(f"{'':<10}{attackers[0]:<5}{attackers[1]:<5}{attackers[2]:<5}{'':<5}{'':<5}{'':<5}")
    print(f"{defenders[0]:<10}{defenders[1]:<5}{defenders[2]:<5}{defenders[3]:<5}{goalkeeper:<5}{'':<5}")
    print(f"{'':<10}{midfielders[0]:<5}{midfielders[1]:<5}{midfielders[2]:<5}{'':<5}{'':<5}{'':<5}")

# Example usage
print_soccer_formation("4-3-3")

import os

def center_text(text):
    # Get the size of the terminal window
    terminal_width = os.get_terminal_size().columns

    # Calculate the amount of padding needed to center the text
    padding = (terminal_width - len(text)) // 2

    # Construct the centered text with padding
    centered_text = ' ' * padding + text + ' ' * padding

    # Adjust for odd terminal widths
    if len(centered_text) < terminal_width:
        centered_text += ' ' * (terminal_width - len(centered_text))

    return centered_text

# Example usage
centered = center_text("Centered Text")
print(centered)
