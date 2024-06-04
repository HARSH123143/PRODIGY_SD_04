def print_grid(grid):
    """Function to print the Sudoku grid with a user-friendly format."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()

def is_safe(grid, row, col, num):
    """Check if it's safe to place a number in the given position."""
    # Check the row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check the column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(grid):
    """Function to solve the Sudoku puzzle using backtracking."""
    empty_pos = find_empty_location(grid)
    if not empty_pos:
        return True  # No empty position is left, puzzle solved

    row, col = empty_pos

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            # Undo the current cell for backtracking
            grid[row][col] = 0

    return False

def find_empty_location(grid):
    """Function to find an empty location in the grid."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid_grid(grid):
    """Check if the initial grid is valid."""
    for i in range(9):
        for j in range(9):
            num = grid[i][j]
            if num != 0:
                grid[i][j] = 0  # Temporarily remove the number
                if not is_safe(grid, i, j, num):
                    return False
                grid[i][j] = num  # Restore the number
    return True

def read_sudoku_grid():
    """Function to read a Sudoku grid from the user."""
    grid = []
    print("Enter the Sudoku puzzle row by row (use 0 for empty cells):")
    for i in range(9):
        while True:
            row = input(f"Row {i + 1}: ")
            if len(row) == 9 and row.isdigit():
                grid.append([int(num) for num in row])
                break
            else:
                print("Invalid input. Please enter exactly 9 digits (0-9) for the row.")
    return grid

# Example usage
if __name__ == "__main__":
    # Read Sudoku puzzle from the user
    sudoku_grid = read_sudoku_grid()

    if is_valid_grid(sudoku_grid):
        print("\nInitial Sudoku grid:")
        print_grid(sudoku_grid)
        
        if solve_sudoku(sudoku_grid):
            print("\nSudoku puzzle solved successfully!")
            print_grid(sudoku_grid)
        else:
            print("\nNo solution exists for the given Sudoku puzzle.")
    else:
        print("The provided Sudoku grid is invalid.")