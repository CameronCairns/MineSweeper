import random
import fileinput
import pdb

class Grid:

    def __init__(self, dimension=10, percent_bombs=30):
        self.dimension = dimension
        self.percent_bombs = percent_bombs
        self.grid = [[ Node(row, column) for column in range(dimension)] for row in range(dimension)]

    def test(self, row, column):
        pdb.set_trace()
        if self.grid[row][column].bomb == True:
            # tested a bomb so they lost
            return 'lost'
        else:
            # test if any bombs surround it
            self.grid[row][column].revealed == True
            self.discover(row, column)

    def discover(self, row, column):
        surrounding_bombs = 0
        for row, value in enumerate(self.grid[row-1:row+2]):
            for column, value in enumerate(self.grid[row-1:row+2]):
                if self.grid[row][column].revealed == False and self.grid[row][column].bomb == True:
                    surrounding_bombs += 1
        self.grid[row][column].surrounding_bombs == surrounding_bombs
        self.grid[row][column].revealed == True
        if surrounding_bombs == 0:
            # No bombs found
            for row, value in enumerate(self.grid[row-1:row+2]):
                for column, value in enumerate(self.grid[row-1:row+2]):
                    discover(row, column)


    def print(self):
        for row in self.grid:
            print('')
            for column in row:
                print(column, end=';')
            print('')

    def generate_bombs(self):
        random.seed()
        number_of_bombs = self.percent_bombs*.01*self.dimension**2
        while number_of_bombs > 0:
            row = random.randrange(self.dimension)
            column = random.randrange(self.dimension)
            if self.grid[row][column].bomb == False:
                self.grid[row][column].bomb = True
                number_of_bombs -= 1

class Node:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.bomb = False
        self.surrounding_bombs = 0
        self.revealed = False

    def __str__(self):
        if self.revealed:
            if self.bomb == True:
                # A bomb exists so print a marker
                return '!'.center(6)
            else:
                return str(self.surrounding_bombs).center(6)
        else:
            return '{}:{}'.format(self.row, self.column).center(6)


if __name__ == '__main__':
    # Create necessary objects for game to be played
    # Instantiate a grid object for player to use
    game_over = False
    grid = Grid()
    grid.generate_bombs() 

    # Begin Game
    print("""
            Welcome to Minesweeper!

            Please enter a node you wish to test for a bomb.
            Nodes are selected by typing the row number followed
            by a space and then the column number.

            For Example:
            12 3
            """)
    while not game_over:
        grid.print()
        row, column = (int(x) for x in input().split())
        if(row < grid.dimension and row > 0 and
           column < grid.dimension and column > 0):
            # Test the entered row, and column are valid for dimensions
            result = grid.test(row, column)
            if result == 'lost':
                print('You Lost! Please try again')
                game_over = True
            elif result == 'win':
                print('You Won!')
                game_over = True
            else:
                print('No mines found!, please test another square')
        else:
            # Player entered invalid numbers for row and column
            print('Please enter a row and column value less than'
                  ' {} and greater than 0'.format(grid.dimension))
