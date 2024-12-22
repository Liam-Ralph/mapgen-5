# IMPORTS
from math import ceil
import os
import random

# TEXT COLORS
ANSI_RED = "\u001b[38;5;1m"
ANSI_GREEN = "\u001b[38;5;2m"
ANSI_CYAN = "\u001b[38;5;6m"
ANSI_RESET = "\u001b[0m"
# MAP COLORS - PYTHON TURTLE
# Green
TURTLE_GREEN_LIGHT = (0, 102, 0)
TURTLE_GREEN_DARK = (0, 51, 0)
# Blue
TURTLE_BLUE_LIGHT = (0, 57, 160)
TURTLE_BLUE_NORMAL = (0, 0, 153)
TURTLE_BLUE_DARK = (0, 0, 102)
TURTLE_BLUE_DARKEST = (0, 0, 51)
# Grey
TURTLE_GREY_LIGHT = (102, 102, 102)
TURTLE_GREY_NORMAL = (77, 77, 77)
TURTLE_GREY_DARK = (64, 64, 64)
TURTLE_GREY_DARKEST = (38, 38, 38)
# Red
TURTLE_RED_LIGHTEST = (255, 90, 90)
TURTLE_RED_LIGHT = (219, 75, 75)
TURTLE_RED_NORMAL = (175, 60, 60)
TURTLE_RED_DARK = (100, 40, 40)
TURTLE_RED_DARKEST = (75, 25, 25)
# Aquamarine
TURTLE_AQUA_1 = (95, 105, 110)
TURTLE_AQUA_2 = (80, 88, 92)
TURTLE_AQUA_3 = (120, 210, 33)
TURTLE_AQUA_4 = (178, 193, 60)
TURTLE_AQUA_5 = (128, 255, 192)
TURTLE_AQUA_6 = (90, 220, 170)
TURTLE_AQUA_7 = (75, 190, 150)
# Other
TURTLE_WHITE = (220, 220, 220)
TURTLE_YELLOW = (153, 153, 0)
# MAP COLORS - ANSI TEXT COLORS
# Green
ANSI_GREEN_LIGHT = "\u001b[48;5;28m"
ANSI_GREEN_DARK = "\u001b[48;5;22m"
# Blue
ANSI_BLUE_LIGHT = "\u001b[48;5;21m"
ANSI_BLUE_NORMAL = "\u001b[48;5;19m"
ANSI_BLUE_DARK = "\u001b[48;5;18m"
ANSI_BLUE_DARKEST = "\u001b[48;5;17m"
# Grey
ANSI_GREY_LIGHT = "\u001b[48;5;236m"
ANSI_GREY_NORMAL = "\u001b[48;5;235m"
ANSI_GREY_DARK = "\u001b[48;5;234m"
ANSI_GREY_DARKEST = "\u001b[48;5;232m"
# Red
ANSI_RED_LIGHTEST = "\u001b[48;5;197m"
ANSI_RED_LIGHT = "\u001b[48;5;196m"
ANSI_RED_NORMAL = "\u001b[48;5;160m"
ANSI_RED_DARK = "\u001b[48;5;88m"
ANSI_RED_DARKEST = "\u001b[48;5;52m"
# Aquamarine
ANSI_AQUA_1 = "\u001b[48;5;243m"
ANSI_AQUA_2 = "\u001b[48;5;240m"
ANSI_AQUA_3 = "\u001b[48;5;82m"
ANSI_AQUA_4 = "\u001b[48;5;106m"
ANSI_AQUA_5 = "\u001b[48;5;87m"
ANSI_AQUA_6 = "\u001b[48;5;50m"
ANSI_AQUA_7 = "\u001b[48;5;36m"
# Other
ANSI_WHITE = "\u001b[48;5;254m"
ANSI_YELLOW = "\u001b[48;5;94m"
ANSI_BLACK = "\u001b[48;5;0m"

# FUNCTIONS
def get_choice(minimum, maximum):
    while True:
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print(ANSI_RED + "Input must be a whole number." + ANSI_RESET)
            continue
        if minimum <= choice <= maximum:
            break
        else:
            print(
                ANSI_RED + "Input must be greater than or equal to " +
                str(minimum) + " and less than or equal to " + str(maximum) +
                "." + ANSI_RESET
            )
    return choice

def clear_screen():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

# MAIN FUNCTION
def main():
    # INTRODUCTION AND SETUP
    # Getting user input to decide how the map is generated and shown
    clear_screen()
    print(
        ANSI_CYAN + "Welcome to MapGen 5!" +
        "\nThis is my best and most recent map generating project, and" +
        "\nmy second using Python Turtle. This project generates a map" +
        "\nbased on specifications you will choose. The way it generates" +
        "\nthe map is the same as MapGen 4, but there are new features in" +
        "\nthis version.\nPress enter to continue." + ANSI_RESET
    )
    input()
    clear_screen()
    print(
        ANSI_CYAN + "First, you must choose whether you would like the map" +
        "\nto be generated using Python Turtle or colored text. Python" +
        "\nTurtle looks better, but takes more time to generate. If you are" +
        "\nusing Replit, the console will close as soon as the Turtle" +
        "\nwindow opens (I have no idea why they do this)." +
        "\nPlease use fullscreen." +
        "\n[1] Use Python Turtle\n[2] Use colored text" + ANSI_RESET
    )
    use_turtle = False
    if get_choice(1, 2) == 1:
        use_turtle = True
    clear_screen()
    print(
        ANSI_CYAN + "Next, you must decide the map's width and height." +
        "\nMap Width: " + ANSI_RESET, end = ""
    )
    map_width = get_choice(10, 100)
    print(ANSI_CYAN + "Map Height: " + ANSI_RESET, end = "")
    map_height = get_choice(10, 100)
    clear_screen()
    print(
        ANSI_CYAN +
        "Now, you have to decide what colors you want the map to use." +
        "\nYou have many different color sets to choose from." +
        "\n[1] Normal\n[2] Normal - More Land\n[3] All Land" +
        "\n[4] Almost All Water\n[5] Martian\n[6] Lunar\n[7] Aquamarine" +
        "\n[8] Mountain" + ANSI_RESET
    )
    color_set = get_choice(1, 8)
    clear_screen()

    # MAP GENERATION
    # Generation Setup
    print(ANSI_CYAN + "Setup...", end = "\r")
    total_tiles = map_width * map_height
    tiles = []
    for i in range(total_tiles):
        tiles.append("blank")
    print(ANSI_GREEN + "Setup Complete")
    # Primary Generation - Land, Sand, and Water
    print(ANSI_CYAN + "Primary Generation...", end = "\r")
    # First Tile
    random_num = random.randint(1, 3)
    if random_num == 1:
        tiles[0] = 3
    elif random_num == 2:
        tiles[0] = 6
    else:
        tiles[0] = 4
    # First Line of Tiles
    for i in range(1, map_width):
        previous_tile = tiles[i - 1]
        random_num = random.randint(1, 100)
        if previous_tile == 3:
            if random_num <= 70:
                tiles[i] = 3
            else:
                tiles[i] = 4
        elif previous_tile == 4:
            if random_num <= 50:
                tiles[i] = 3
            else:
                tiles[i] = 6
        else:
            if random_num <= 80:
                tiles[i] = 6
            else:
                tiles[i] = 4
    for y in range(1, map_height):
        # First Tile in each line (except First Line)
        i = y * map_width
        above_tile = tiles[i - map_width]
        random_num = random.randint(1, 100)
        if above_tile == 3:
            if random_num <= 70:
                tiles[i] = 3
            else:
                tiles[i] = 4
        elif above_tile == 4:
            if random_num <= 50:
                tiles[i] = 3
            else:
                tiles[i] = 6
        else:
            if random_num <= 80:
                tiles[i] = 6
            else:
                tiles[i] = 4
        # Each Line (except First Line)
        for x in range(map_width - 1):
            i = (y * map_width) + x + 1
            previous_tile = tiles[i - 1]
            above_tile = tiles[i - map_width]
            random_num = random.randint(1, 100)
            if previous_tile == 3:
                if above_tile == 3:
                    if random_num <= 70:
                        tiles[i] = 3
                    else:
                        tiles[i] = 4
                elif above_tile == 4:
                    if random_num <= 70:
                        tiles[i] = 3
                    else:
                        tiles[i] = 4
                else:
                    if random_num <= 5:
                        tiles[i] = 3
                    elif random_num <= 95:
                        tiles[i] = 4
                    else:
                        tiles[i] = 6
            elif previous_tile == 4:
                if above_tile == 3:
                    if random_num <= 30:
                        tiles[i] = 4
                    else:
                        tiles[i] = 3
                elif above_tile == 4:
                    if x >= 2:
                        pre_previous_tile = tiles[i - 2]
                        if pre_previous_tile == 3 and random_num <= 50:
                            tiles[i - 2] = 6
                    if random_num <= 50:
                        tiles[i] = 3
                    else:
                        tiles[i] = 6
                else:
                    if random_num <= 30:
                        tiles[i] = 4
                    else:
                        tiles[i] = 6
            else:
                if above_tile == 3:
                    if random_num <= 5:
                        tiles[i] = 3
                    elif random_num <= 95:
                        tiles[i] = 4
                    else:
                        tiles[i] = 6
                elif above_tile == 4:
                    if random_num <= 70:
                        tiles[i] = 6
                    else:
                        tiles[i] = 4
                else:
                    if random_num <= 80:
                        tiles[i] = 6
                    else:
                        tiles[i] = 4
    print(ANSI_GREEN + "Primary Generation Complete")
    # Secondary Generation - Rock, Shallow Water, and Sand Replacement
    print(ANSI_CYAN + "Secondary Generation...", end = "\r")
    for i in range(len(tiles)):
        # Rock Generation
        if tiles[i] == 4:
            if i % map_width != 0:
                previous_tile = tiles[i - 1]
            else:
                previous_tile = 3
            if i % map_width != map_width - 1:
                next_tile = tiles[i + 1]
            else:
                next_tile = 3
            if i >= map_width:
                above_tile = tiles[i - map_width]
            else:
                above_tile = 3
            if i < (map_height - 1) * map_width:
                below_tile = tiles[i + map_width]
            else:
                below_tile = 3
            if((previous_tile != 6 and previous_tile != 5) and
            (next_tile != 6 and next_tile != 5) and
            (above_tile != 6 and above_tile != 5) and
            (below_tile != 6 and below_tile != 5)):
                tiles[i] = 1
            # Extra Sand Replacement
            if i % map_width != 0:
                previous_tile = tiles[i - 1]
            else:
                previous_tile = 6
            if i % map_width != map_width - 1:
                next_tile = tiles[i + 1]
            else:
                next_tile = 6
            if i >= map_width:
                above_tile = tiles[i - map_width]
            else:
                above_tile = 6
            if i < (map_height - 1) * map_width:
                below_tile = tiles[i + map_width]
            else:
                below_tile = 6
            count = 0
            # Checks for 75 %  water and no land or rock
            if previous_tile == 6:
                count += 1
            elif previous_tile != 4:
                count = -100
            if next_tile == 6:
                count += 1
            elif next_tile != 4:
                count = -100
            if above_tile == 6:
                count += 1
            elif above_tile != 4:
                count = -100
            if below_tile == 6:
                count += 1
            elif below_tile != 4:
                count = -100
            if count > 2:
                if random_num <= 65:
                    tiles[i] = 6
        # Shallow Water Generation
        if tiles[i] == 3 or tiles[i] == 4:
            if i % map_width != 0:
                previous_tile = tiles[i - 1]
            else:
                previous_tile = 3
            if i % map_width != map_width - 1:
                next_tile = tiles[i + 1]
            else:
                next_tile = 3
            if i >= map_width:
                above_tile = tiles[i - map_width]
            else:
                above_tile = 3
            if i < (map_height - 1) * map_width:
                below_tile = tiles[i + map_width]
            else:
                below_tile = 3
            if previous_tile == 6 and i % map_width != 0:
                random_num = random.randint(1, 100)
                if random_num <= 70:
                    tiles[i - 1] = 5
            if next_tile == 6 and i % map_width != map_width - 1:
                random_num = random.randint(1, 100)
                if random_num <= 70:
                    tiles[i + 1] = 5
            if above_tile == 6 and i >= map_width:
                random_num = random.randint(1, 100)
                if random_num <= 70:
                    tiles[i - map_width] = 5
            if below_tile == 6 and i < (map_height - 1) * map_width:
                random_num = random.randint(1, 100)
                if random_num <= 70:
                    tiles[i + map_width] = 5
    print(ANSI_GREEN + "Secondary Generation Complete")
    # Tertiary Generation - Darker Rock and Deep Water
    print(ANSI_CYAN + "Tertiary Generation", end = "\r")
    for i in range(len(tiles)):
        # Darker Rock Generation
        if tiles[i] == 1:
            if i % map_width != 0:
                previous_tile = tiles[i - 1]
            else:
                previous_tile = 3
            if i % map_width != map_width - 1:
                next_tile = tiles[i + 1]
            else:
                next_tile = 3
            if i >= map_width:
                above_tile = tiles[i - map_width]
            else:
                above_tile = 3
            if i < (map_height - 1) * map_width:
                below_tile = tiles[i + map_width]
            else:
                below_tile = 3
            if previous_tile == 3 and i % map_width != 0:
                random_num = random.randint(1, 100)
                if random_num <= 75:
                    tiles[i - 1] = 2
            if next_tile == 3 and i % map_width != map_width - 1:
                random_num = random.randint(1, 100)
                if random_num <= 75:
                    tiles[i + 1] = 2
            if above_tile == 3 and i >= map_width:
                random_num = random.randint(1, 100)
                if random_num <= 75:
                    tiles[i - map_width] = 2
            if below_tile == 3 and i < (map_height - 1) * map_width:
                random_num = random.randint(1, 100)
                if random_num <= 75:
                    tiles[i + map_width] = 2
        # Deep Water Generation
        elif tiles[i] == 6:
            if i % map_width != 0:
                previous_tile = tiles[i - 1]
            else:
                previous_tile = 6
            if i % map_width != map_width - 1:
                next_tile = tiles[i + 1]
            else:
                next_tile = 6
            if i >= map_width:
                above_tile = tiles[i - map_width]
            else:
                above_tile = 6
            if i < (map_height - 1) * map_width:
                below_tile = tiles[i + map_width]
            else:
                below_tile = 6
            if((previous_tile == 6 or previous_tile == 7) and
            (next_tile == 6 or next_tile == 7) and
            (above_tile == 6 or above_tile == 7) and
            (below_tile == 6 or below_tile == 7)):
                random_num = random.randint(1, 100)
                if random_num <= 85:
                    tiles[i] = 7
    print(ANSI_GREEN + "Tertiary Generation Complete")
    # Map Generation Complete
    print(
        "Map Generation Complete" + ANSI_CYAN + "\nPress enter to continue." +
        ANSI_RESET
    )
    input()
    clear_screen()

    # MAP STATS AND PRINTING
    # Map Stats
    print(
        ANSI_CYAN + "Map Stats" + "\nSome colors may have two percentages," +
        "\nadd them to get the total of that color." + ANSI_RESET
    )
    match(color_set):
        case 1:
            name_list = ["Lighter Rock", "Darker Rock", "Land", "Sand",
                         "Lighter Water", "Water", "Darker Water"]
        case 2:
            name_list = ["Lighter Rock", "Rock", "Darker Rock", "Darker Land",
                         "Lighter Land", "Sand", "Water"]
        case 3:
            name_list = ["Lighter Rock", "Rock", "Darker Rock", "Darker Land",
                         "Lighter Land", "Lighter Land", "Sand"]
        case 4:
            name_list = ["Lighter Rock", "Darker Rock", "Lighter Water",
                         "Water", "Water", "Darker Water", "Darkest Water"]
        case 5:
            name_list = ["Lightest Land", "Light Land", "Land", "Darker Land",
                         "Darkest Land", "Lighter Water", "Darker Water"]
        case 6:
            name_list = ["Lighter Rock", "Lighter Rock", "Rock",
                         "Darker Rock", "Darkest Rock", "Water",
                         "Darker Water"]
        case 7:
            name_list = ["Lighter Rock", "Darker Rock", "Land", "Sand",
                         "Lighter Water", "Water", "Darker Water"]
        case 8:
            name_list = ["Snow", "Lighter Rock", "Rock", "Darker Rock",
                         "Darkest Rock", "Darker Land", "Lighter Land"]
        case _:
            name_list = []
            for i in range(7):
                name_list.append("Unknown")
    max_length = len(max(name_list, key = len)) + 5
    print("Type" + (" " * (max_length - 4)) + "Percent")
    for i in range(7):
        spaces_string = " " * (max_length - len(name_list[i]))
        num_string = "%.2f" % (tiles.count(i + 1) * 100 / len(tiles))
        if float(num_string) < 10:
            num_string = " " + num_string
        print(
            name_list[i] + spaces_string + num_string + "%"
        )
    print(ANSI_CYAN + "Press enter to print map." + ANSI_RESET, end = "")
    input()
    # Map Printing
    if use_turtle:
        # Tile Size Computing
        if map_height > map_width:
            map_size = map_height
        else:
            map_size = map_width
        tile_size = 50
        while tile_size * map_size > 500:
            tile_size -= 1
        # Getting colors
        match(color_set):
            case 1:
                color_list = [TURTLE_GREY_NORMAL, TURTLE_GREY_DARK,
                              TURTLE_GREEN_LIGHT, TURTLE_YELLOW,
                              TURTLE_BLUE_LIGHT, TURTLE_BLUE_NORMAL,
                              TURTLE_BLUE_DARK]
            case 2:
                color_list = [TURTLE_GREY_LIGHT, TURTLE_GREY_NORMAL,
                              TURTLE_GREY_DARK, TURTLE_GREEN_DARK,
                              TURTLE_GREEN_LIGHT, TURTLE_YELLOW,
                              TURTLE_BLUE_LIGHT]
            case 3:
                color_list = [TURTLE_GREY_LIGHT, TURTLE_GREY_NORMAL,
                              TURTLE_GREY_DARK, TURTLE_GREEN_DARK,
                              TURTLE_GREEN_LIGHT, TURTLE_GREEN_LIGHT,
                              TURTLE_YELLOW]
            case 4:
                color_list = [TURTLE_GREY_NORMAL, TURTLE_GREY_DARK,
                              TURTLE_BLUE_LIGHT, TURTLE_BLUE_NORMAL,
                              TURTLE_BLUE_NORMAL, TURTLE_BLUE_DARK,
                              TURTLE_BLUE_DARKEST]
            case 5:
                color_list = [TURTLE_RED_LIGHTEST, TURTLE_RED_LIGHT,
                              TURTLE_RED_NORMAL, TURTLE_RED_DARK,
                              TURTLE_RED_DARKEST, TURTLE_BLUE_LIGHT,
                              TURTLE_BLUE_NORMAL]
            case 6:
                color_list = [TURTLE_GREY_LIGHT, TURTLE_GREY_LIGHT,
                              TURTLE_GREY_NORMAL, TURTLE_GREY_DARK,
                              TURTLE_GREY_DARKEST, TURTLE_BLUE_NORMAL,
                              TURTLE_BLUE_DARK]
            case 7:
                color_list = [TURTLE_AQUA_1, TURTLE_AQUA_2, TURTLE_AQUA_3,
                              TURTLE_AQUA_4, TURTLE_AQUA_5, TURTLE_AQUA_6,
                              TURTLE_AQUA_7]
            case 8:
                color_list = [TURTLE_WHITE, TURTLE_GREY_LIGHT,
                              TURTLE_GREY_NORMAL, TURTLE_GREY_DARK,
                              TURTLE_GREY_DARKEST, TURTLE_GREEN_DARK,
                              TURTLE_GREEN_LIGHT]
            case _:
                color_list = []
                for i in range(7):
                    color_list.append((0, 0, 0))
        # Printing with Python Turtle
        import turtle
        turtle.speed(0)
        turtle.colormode(255)
        turtle.title("MapGen 5")
        turtle.hideturtle()
        turtle.penup()
        turtle_size = 20
        screen = turtle.Screen()
        screen.setup(width = 600, height = 600, startx = 0, starty = 0)
        turtle.goto(
            turtle_size / 2 - screen.window_width() / 2,
            screen.window_height() / 2 - turtle_size / 2
        )
        turtle.pendown()
        for y in range(map_height):
            for x in range(map_width):
                i = y * map_width + x
                tile_color = color_list[tiles[i] - 1]
                turtle.pendown()
                turtle.pensize(1)
                turtle.color(tile_color)
                turtle.begin_fill()
                for i in range(2):
                    turtle.forward(tile_size)
                    turtle.right(90)
                    turtle.forward(tile_size)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
                turtle.forward(tile_size)
            turtle.right(90)
            turtle.forward(tile_size)
            turtle.right(90)
            turtle.forward(tile_size * map_width)
            turtle.right(180)
        turtle.Screen().exitonclick()
    else:
        # Getting colors
        match(color_set):
            case 1:
                color_list = [ANSI_GREY_NORMAL, ANSI_GREY_DARK,
                              ANSI_GREEN_DARK, ANSI_YELLOW, ANSI_BLUE_LIGHT,
                              ANSI_BLUE_NORMAL, ANSI_BLUE_DARK]
            case 2:
                color_list = [ANSI_GREY_LIGHT, ANSI_GREY_NORMAL,
                              ANSI_GREY_DARK, ANSI_GREEN_DARK,
                              ANSI_GREEN_LIGHT, ANSI_YELLOW, ANSI_BLUE_LIGHT]
            case 3:
                color_list = [ANSI_GREY_LIGHT, ANSI_GREY_NORMAL,
                              ANSI_GREY_DARK, ANSI_GREEN_DARK,
                              ANSI_GREEN_LIGHT, ANSI_GREEN_LIGHT, ANSI_YELLOW]
            case 4:
                color_list = [ANSI_GREY_NORMAL, ANSI_GREY_DARK,
                              ANSI_BLUE_LIGHT, ANSI_BLUE_NORMAL,
                              ANSI_BLUE_NORMAL, ANSI_BLUE_DARK,
                              ANSI_BLUE_DARKEST]
            case 5:
                color_list = [ANSI_RED_LIGHTEST, ANSI_RED_LIGHT,
                              ANSI_RED_NORMAL, ANSI_RED_DARK,
                              ANSI_RED_DARKEST, ANSI_BLUE_LIGHT,
                              ANSI_BLUE_NORMAL]
            case 6:
                color_list = [ANSI_GREY_LIGHT, ANSI_GREY_LIGHT,
                              ANSI_GREY_NORMAL, ANSI_GREY_DARK,
                              ANSI_GREY_DARKEST, ANSI_BLUE_NORMAL,
                              ANSI_BLUE_DARK]
            case 7:
                color_list = [ANSI_AQUA_1, ANSI_AQUA_2, ANSI_AQUA_3,
                              ANSI_AQUA_4, ANSI_AQUA_5, ANSI_AQUA_6,
                              ANSI_AQUA_7]
            case 8:
                color_list = [ANSI_WHITE, ANSI_GREY_LIGHT,
                              ANSI_GREY_NORMAL, ANSI_GREY_DARK,
                              ANSI_GREY_DARKEST, ANSI_GREEN_DARK,
                              ANSI_GREEN_LIGHT]
            case _:
                color_list = []
                for i in range(7):
                    color_list.append((0, 0, 0))
        # Printing with colored text
        for y in range(ceil(map_height / 2)):
            for x in range(map_width):
                i = y * 2 * map_width + x
                ii = (y * 2 + 1) * map_width + x
                tile_color1 = color_list[tiles[i] - 1]
                try:
                    tile_color2 = color_list[tiles[ii] - 1]
                except IndexError:
                    tile_color2 = ANSI_BLACK
                if tile_color1 == tile_color2:
                    print(tile_color1 + " ", end = "")
                else:
                    print(
                        tile_color1 + tile_color2.replace("48;", "38;") + "▄",
                        end = ""
                    )
                print(ANSI_RESET, end = "")
            print()

main()
