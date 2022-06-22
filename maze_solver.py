from itertools import count
from operator import truediv
import os
import yaml
from sys import stderr


def maze_check(_maze):
    dims = [len(_maze), len(_maze[0])]
    count_check = dims[0]*dims[1]
    symbol_count = 0
    symbols = load_config('symbols')
    for row in _maze:
        if row != dims:
            pass
        for col in row:
            symbol_count += 1
            if col in symbols.values():
                continue
            else:
                print('Invalid symbols found in maze.', file=stderr)
                exit(0)
    if symbol_count != count_check:
        print('Invalid maze dimensionality.', file=stderr)
        exit(0)


def load_config(mode:str=None):
    with open('config.yaml', 'r') as r:
        conf = yaml.safe_load(r)
        r.close()
    if mode is None:
        return conf
    else:
        try:
            return conf[mode]
        except:
            print('Invalid dict key.', file=stderr)
            exit(0)


def print_result(solved_maze, raw_maze, path_len):
    shortest_path_symbol = load_config('shortest_path_symbol')
    print('Original maze vs solved maze:\n')
    for row in zip(solved_maze, raw_maze):
        joined_row = ''.join(row[1].rstrip('\n')) + '\t' + '|' + '\t' + ''.join(row[0])
        print(joined_row)
    print(f'\nMaze solved - path is represented by "{shortest_path_symbol}" symbol defined in configuration file.' \
           f' Length of the shortest path is {path_len}.')


def forge_path(start, finish, travelled_path, maze):
    shortest_path = []
    symbols = load_config('symbols')
    shortest_path_symbol = load_config('shortest_path_symbol')
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


def prep_maze(maze:list):
    _maze = []
    symbols = load_config('symbols')
    start, finish = (), ()
    for line in maze:
        line = line.strip('\n')
        row = []
        for letter in line:
            row.append(letter)
        _maze.append(row)
    maze_check(_maze)

    for row in _maze:
        for symbol in row:
            if symbol == symbols['finish']:
                finish = (_maze.index(row), row.index(symbol))
            elif symbol == symbols['start']:
                start = (_maze.index(row), row.index(symbol))
    return _maze, start, finish


def load_maze(path):
    if os.path.exists(path):
        with open(path, 'r') as r:
            maze = r.readlines()
    else:
        print('Invalid path.', file=stderr)
        exit(0)
    return maze


def solve(path):
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