# Beam Brackets Soccer Simulation

# Imports
import os
from pprint import pprint
from textwrap import wrap

# Initial Phase
terminal_width = os.get_terminal_size().columns

# Formation
keyword_names = ["narrow","wide","wingbacks","fullbacks","false-9"]
position_names = ["LWB","LB","CB","RB","RWB",
             "DM","CDM","LM","CM","RM","AM","CAM",
             "LW","LF","CF","ST","RF","RW"]

print(*wrap("To choose formation, input the desired formation followed by optional keywords. To specify a certain position, include the position as a keyword. Separate keywords by spaces.", terminal_width), sep='\n')
print(*wrap("Notes: 3-back formations default to no fullbacks/wingbacks, 5-back formations default to wingbacks, 3-row formations default to all CMs in the midfield.", terminal_width), sep='\n')
print(*wrap("Ex: 4-3-3, 3-4-1-2, 5-5, 3-5-2 wingbacks, 4-2-3-1 narrow, 5-3-2 fullbacks CAM", terminal_width), sep='\n')
print(*wrap(f"Possible keywords: {', '.join(keyword_names)}", terminal_width), sep='\n')

valid_formation = False 
while not valid_formation:
    formation = input("Select Formation: ")
    formation = formation.split(" ")
    keyw = formation[1:]
    kflag = False
    for kw in keyw:
        if kw not in keyword_names and kw not in position_names:
            print("ERROR: Unrecognized keyword.")
            kflag = True
            break
    if kflag:
        continue
    formation = formation[0].split("-")

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
        print("ERROR: Formation must be for 10 outfield players.")
        continue
    valid_formation = True

def assign_positions(formation: list[int], keyw: list):
    """
    docstring
    """
    assert(isinstance(formation, list)), "ERROR: Formation must be list"
    positions = []

    for i,row in enumerate(formation):
        if i == 0:
            if row <= 3:
                positions.append(["CB"]*row)
            elif row == 4:
                positions.append(["LB", "CB", "CB", "RB"])
            else:
                positions.append(["LWB"]+["CB"]*(row-2)+["RWB"])
        elif i == len(formation) - 1:
            if row <= 2:
                positions.append(["ST"]*row)
            else:
                positions.append(["LW"]+["ST"]*(row-2)+["RW"])
        elif i == 1 and len(formation) > 3:
            positions.append(["CDM"]*row)
        elif i == len(formation) - 2 and len(formation) > 3:
            if row > 3:
                positions.append(["LM"]+["CAM"]*(row-2)+["RM"])
            else:
                positions.append(["CAM"]*row)
        else:
            if row > 3:
                positions.append(["LM"]+["CM"]*(row-2)+["RM"])
            else:
                positions.append(["CM"]*row)

    keyw = [x for x in keyw if x in keyword_names]
    pos = [x for x in keyw if x in position_names]
    flat = [x for row in positions for x in row]

    for p in pos:
        if p not in flat:
            pass

    for kw in keyword_names:
        if kw in keyw:
            if kw == "fullbacks":
                lwb = find_position("LWB", positions)
                rwb = find_position("RWB", positions)
                if lwb and rwb:
                    positions[lwb[0]][lwb[1]] = "LB"
                    positions[rwb[0]][rwb[1]] = "RB"

    return positions

def print_formation(positions: list):
    print(*positions)
    return

def find_position(pos: str, positions: list):
    for i,row in enumerate(positions):
        for j,p in enumerate(row):
            if pos == p:
                return (i,j)
    return False

print_formation(assign_positions(formation, keyw))