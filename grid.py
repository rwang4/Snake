def sum_of_neighbors(grid):
    neighbors_grid = []
    for r in range(0, len(grid)):
        row = []
        for c in range(0, len(grid[r])):
            neighbors_list = find_neighbors(r, c, grid)
            row.append(neighbors_list)
        neighbors_grid.append(row)

    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            grid[r][c] = sum(neighbors_grid[r][c])
    return grid


def find_neighbors(row_index, col_index, grid):
    neighbors = []
    if row_index-1 >= 0:
        neighbors.append(grid[row_index-1][col_index])
        if col_index-1 >= 0:
            neighbors.append(grid[row_index-1][col_index-1])
        if col_index+1 < len(grid[0]):
            neighbors.append(grid[row_index-1][col_index+1])
    if col_index-1 >= 0:
        neighbors.append(grid[row_index][col_index-1])
    if row_index+1 < len(grid):
        neighbors.append(grid[row_index+1][col_index])
        if col_index-1 >= 0:
            neighbors.append(grid[row_index+1][col_index-1])
        if col_index+1 < len(grid[0]):
            neighbors.append(grid[row_index+1][col_index+1])
    if col_index+1 < len(grid[0]):
        neighbors.append(grid[row_index][col_index+1])
    return neighbors


def display_grid(grid):
    for row in grid:
        string = '| '
        for num in row:
            string += str(num)
            string += ' | '
        print(string)


def create_grid(filename):
    file = open(filename, 'r')
    row_n = int(file.readline())
    col_n = int(file.readline())
    grid = []
    for r in range(0, row_n):
        row = []
        for c in range(0, col_n):
            num = int(file.readline())
            row.append(num)
        grid.append(row)
    return grid


def main():
    filename = "data_2.txt"
    grid = create_grid(filename)
    print("This is out grid:")
    display_grid(grid)
    print("\nThis is our newly calculated grid:")
    new_grid = sum_of_neighbors(grid)
    display_grid(new_grid)


main()
