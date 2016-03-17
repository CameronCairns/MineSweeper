# Minesweeper
# By Cameron Cairns
# Inspired by Microsoft's Minesweeper

# Challenge, spec and write this code within 1 hour

import pdb
import random

class MineGrid:

    def traverse_nodes(self, x, y, surrounding_bombs):
        if grid[x][y].bomb == True:
            return 1
        for sur_x in range(x-1, x+1):
            for sur_y in range(y-1, y+1):
                surrounding_bombs += traverse_nodes(grid[sur_x], grid[sur_y])

        

    def __init__(self, *args, **kwargs):
        self.dimension = kwargs.get('dimension')
        self.percent_bombs = kwargs.get('percent_bombs')
        # Create an array for each x index of grid
        self.grid = [ [] for index in range(self.dimension)]
        for y_index in range(self.dimension):
            for x_index in range(self.dimension):
                self.grid[y_index].append(Node(x=x_index,y=y_index)) 
                
    def populate_bombs(self):
        bombs = self.dimension*self.dimension*.01*self.percent_bombs
        while bombs > 0:
            random.seed()
            random_x_index = random.randrange(self.dimension)
            random_y_index = random.randrange(self.dimension)
            if self.grid[random_x_index][random_y_index].bomb == False:
                self.grid[random_x_index][random_y_index].bomb = True
                bombs -= 1
            

    # Messed up here because __str__ requires you to return something
    # also cannot just use @static decorator
    def print_grid(self):
        for y_index in range(self.dimension): 
            print(*self.grid[y_index], sep=', ')

    def choose_node(self, x, y):
        if grid[x][y].bomb == True:
            print('Game Over!')
        else:
            self.traverse_nodes(grid[x][y])

class Node:

    def __init__(self, *args, **kwargs):
        self.bomb = False
        self.position = (kwargs.get('x'), kwargs.get('y'))
        self.surrounding_bombs = None

    def __str__(self, *args, **kwargs):
        if self.bomb:
            # Node has been found to have a bomb
            return '!'
        elif self.surrounding_bombs:
            # Node has been discovered to have
            # surrounding bombs
            return str(self.surrounding_bombs)
        else:
            # Cannot print a tuple?
            return str(self.position[0]) + ':' + str(self.position[1])
