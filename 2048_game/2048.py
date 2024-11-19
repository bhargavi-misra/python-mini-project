import random
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Clear console function
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

# ASCII Art for Title Screen
def display_title():
    clear_console()
    print(Fore.YELLOW + Style.BRIGHT)
    print("""
{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
{}   ___       __   __ __       __      {}
{} /'___`\   /'__`\/\ \\\\ \    /'_ `\    {}
{}/\_\ /\ \ /\ \/\ \ \ \\\\ \  /\ \L\ \   {}
{}\/_/// /__\ \ \ \ \ \ \\\\ \_\/_> _ <_  {}
{}   // /_\ \\\\ \ \_\ \ \__ ,__\/\ \L\ \ {}
{}  /\______/ \ \____/\/_/\_\_/\ \____/ {}
{}  \/_____/   \/___/    \/_/   \/___/  {}
{}                                      {}
{}                                      {}
{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}""")
    
    print(Fore.CYAN + Style.BRIGHT + "Press Enter to start the game!" + Style.RESET_ALL)
    print(Fore.RED + "Use W/A/S/D to move, and Q to quit to the title screen.")
    print(Fore.RED + "Combine the tiles to reach 2048!\n")
    input()  # Waits for Enter to start

# Initialize the game grid
def initialize_game():
    grid = [[0] * 4 for _ in range(4)]
    add_new_tile(grid)
    add_new_tile(grid)
    return grid

# Add a new tile (2 or 4) to the grid
def add_new_tile(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])

# Display the grid with grid lines and centered numbers
def display_grid(grid):
    clear_console()
    print(Fore.MAGENTA + "Current Grid:")
    print("+------+------+------+------+")  # Top border

    for row in grid:
        row_display = "|"
        for num in row:
            if num == 0:
                cell = " " * 4  # Empty cell
            elif num == max(max(row) for row in grid):
                cell = Fore.GREEN + f"{num:^4}"  # Highlight the highest tile
            else:
                cell = Fore.WHITE + f"{num:^4}"  # Regular tile
            row_display += f" {cell} |"
        print(row_display)
        print("+------+------+------+------+")  # Bottom border of row

# Slide a single row to the left
def slide_row_left(row):
    new_row = [num for num in row if num != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [num for num in new_row if num != 0]
    return new_row + [0] * (4 - len(new_row))

# Move the grid left
def move_left(grid):
    return [slide_row_left(row) for row in grid]

# Move the grid right
def move_right(grid):
    return [slide_row_left(row[::-1])[::-1] for row in grid]

# Move the grid up
def move_up(grid):
    transposed = list(zip(*grid))
    moved = move_left([list(row) for row in transposed])
    return [list(row) for row in zip(*moved)]

# Move the grid down
def move_down(grid):
    transposed = list(zip(*grid))
    moved = move_right([list(row) for row in transposed])
    return [list(row) for row in zip(*moved)]

# Check if the game is over
def is_game_over(grid):
    if any(0 in row for row in grid):
        return False
    for i in range(4):
        for j in range(4):
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False
    return True

# Main game loop
def game_loop():
    grid = initialize_game()
    while True:
        display_grid(grid)
        if is_game_over(grid):
            print(Fore.RED + "Game Over! No moves left.")
            break

        move = input(Fore.YELLOW + "Your move (W/A/S/D/Q): ").strip().upper()
        if move not in "WASDQ":
            print(Fore.RED + "Invalid input! Use W/A/S/D to move, or Q to quit.")
            continue

        if move == "Q":
            return  # Return to title screen

        if move == "W":
            new_grid = move_up(grid)
        elif move == "A":
            new_grid = move_left(grid)
        elif move == "S":
            new_grid = move_down(grid)
        elif move == "D":
            new_grid = move_right(grid)

        if new_grid != grid:
            grid = new_grid
            add_new_tile(grid)
        else:
            print(Fore.RED + "Move not possible. Try a different direction.")

# Main function
def main():
    while True:
        display_title()
        game_loop()

if __name__ == "__main__":
    main()


