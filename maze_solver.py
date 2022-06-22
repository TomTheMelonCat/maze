import os
import yaml
from sys import stderr


def maze_check(maze):
    '''
    Check the maze for errors or invalid symbols.

    :param maze: A 2d array containing the maze.
    '''
    dimensions = [len(maze), len(maze[0])]
    count_check = dimensions[0] * dimensions[1]
    symbol_count = 0
    symbols = load_config('symbols')
    for symbol in symbols.values():
        if len(symbol) > 1 or len(symbol) == 0:
            print('Some of the specified symbols are invalid. Please check your config file.', file=stderr)
            exit(-1)

    for row in maze:
        if row != dimensions:
            pass
        for col in row:
            symbol_count += 1
            if col in symbols.values():
                continue
            else:
                print('Invalid symbols found in maze.', file=stderr)
                exit(-1)

    if symbol_count != count_check:
        print('Invalid maze dimensionality.', file=stderr)
        exit(1)


def load_config(specified_param = None):
    '''
    Loads configuration file.

    :param specified_param: Is either None by default, returning the entire configuration file, or
    has a parameter specified, defining what part of the configuration file to return. 
    '''
    with open('config.yaml', 'r') as r:
        config = yaml.safe_load(r)
        r.close()
    
    if specified_param is None:
        return config
    else:
        try:
            return config[specified_param]
        except KeyError as err:
            print(f'Invalid dict key - {err}', file=stderr)
            exit(1)


def print_result(solved_maze, raw_maze, path_len):
    '''
    Prints original and modified (with shortest path) maze. Also prints a message containing how many
    steps are in an actual shortest path.

    :param solved_maze: Modified maze containing the shortest path. 
    :param raw_maze: Original unchanged maze. 
    :param path_len: Length of the shortest path. 
    '''
    symbols = load_config('symbols')
    shortest_path_symbol = symbols['shortest_path_symbol']
    print('Original maze vs solved maze:\n')
    for row in zip(solved_maze, raw_maze):
        joined_row = ''.join(row[1].rstrip('\n')) + '\t' + '|' + '\t' + ''.join(row[0])
        print(joined_row)

    print(f'\nMaze solved - path is represented by "{shortest_path_symbol}" symbol defined in configuration file.' \
           f' Length of the shortest path is {path_len}.')


def forge_path(start, finish, travelled_path, maze):
    '''
    Forges (constructs) the shortest path and inserts it into the original maze.

    :param start: Start of the maze. 
    :param finish: Finish of the maze. 
    :param travelled_path: The path which has been pivotted through. 
    :param maze: A 2d array containing the maze. 

    :return: Shortest path and a maze in which has been the shortest path marked by a specified symbol.
    '''
    shortest_path = []
    symbols = load_config('symbols')
    shortest_path_symbol = symbols['shortest_path_symbol']
    for idx in range(len(travelled_path.keys())):
        for point in travelled_path.items():
            if point[0] == finish:
                shortest_path.append(finish)
                if maze[finish[0]][finish[1]] != symbols['finish']:
                    maze[finish[0]][finish[1]] = shortest_path_symbol
                finish = point[1]
                break
            else:
                continue

        if finish == start:
            break
    
    return shortest_path, maze


def prep_maze(maze):
    '''
    Removes trailing endlines from each of the lines of a particular maze, checks the maze for errors or
    undefined symbols and defines start and finish.

    :param maze: A 2d array containing the maze. 

    :return: A maze checked through, start and finish
    '''
    maze_ = []
    symbols = load_config('symbols')
    start, finish = (), ()
    for line in maze:
        line = line.strip('\n')
        row = []
        for letter in line:
            row.append(letter)
        maze_.append(row)

    maze_check(maze_)
    for row in maze_:
        for symbol in row:
            if symbol == symbols['finish']:
                finish = (maze_.index(row), row.index(symbol))
            elif symbol == symbols['start']:
                start = (maze_.index(row), row.index(symbol))

    return maze_, start, finish


def load_maze(path):
    '''
    Loads maze from a specified path

    :param path: A string path of the maze. 
    '''
    if os.path.exists(path):
        with open(path, 'r') as r:
            maze = r.readlines()
    else:
        print('Invalid path.', file=stderr)
        exit(1)
    return maze


def solve(path):
    '''
    Solves a .txt maze by finding the shortest path.

    :param path: A string path of the maze. 
    '''
    symbols = load_config('symbols')
    raw_maze = load_maze(path)
    maze, start, finish = prep_maze(raw_maze)
    queue = [start]
    mapped = [start]
    travelled_path = {}
    while queue is not None:
        current_pos = queue.pop(0)
        if current_pos == finish:
            break

        north = maze[current_pos[0]-1][current_pos[1]]
        south = maze[current_pos[0]+1][current_pos[1]]
        west = maze[current_pos[0]][current_pos[1]-1]
        east = maze[current_pos[0]][current_pos[1]+1]
        # North
        if north != symbols['wall'] and (current_pos[0]-1, current_pos[1]) not in mapped:
            queue.append((current_pos[0]-1, current_pos[1]))
            mapped.append((current_pos[0]-1, current_pos[1]))
            travelled_path[(current_pos[0]-1, current_pos[1])] = current_pos
        # South
        if south != symbols['wall'] and (current_pos[0]+1, current_pos[1]) not in mapped:
            queue.append((current_pos[0]+1, current_pos[1]))
            mapped.append((current_pos[0]+1, current_pos[1]))
            travelled_path[(current_pos[0]+1, current_pos[1])] = current_pos
        # West
        if west != symbols['wall'] and (current_pos[0], current_pos[1]-1) not in mapped:
            queue.append((current_pos[0], current_pos[1]-1))
            mapped.append((current_pos[0], current_pos[1]-1))
            travelled_path[(current_pos[0], current_pos[1]-1)] = current_pos
        # East
        if east != symbols['wall'] and (current_pos[0], current_pos[1]+1) not in mapped:
            queue.append((current_pos[0], current_pos[1]+1))
            mapped.append((current_pos[0], current_pos[1]+1))
            travelled_path[(current_pos[0], current_pos[1]+1)] = current_pos

    shortest_path, maze = forge_path(start, finish, travelled_path, maze)
    print_result(maze, raw_maze, len(shortest_path)-1)


if __name__ == '__main__':
    solve(load_config('maze_path'))    