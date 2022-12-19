class Grid:
    def __init__(self, WIDTH=0, HEIGHT=0):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = self.create_empty_grid()

    def print_attributes(self):
        '''Debug function; Prints the object's Width and Height.'''
        print(self.WIDTH, self.HEIGHT)

    def print_grid(self):
        '''Prints every horizontal row of the grid under each other.'''
        for row in self.screen:
            print(*row, sep="")
        # Print every row's values in the self.screen array with no extra makeup.

    def create_empty_grid(self):
        '''Creates an array of Y size containing multiple arrays of X size.'''
        return [[' '] * self.WIDTH for _ in range(self.HEIGHT)]
        # Initialise the main width array every slot stores a vertical row of the grid.

    def verify_picture_file(self, X, Y, screen):
        '''Checks if the screen will fit in our grid instance in it's specified location.'''
        if X >= 0 and Y >= 0:
            # Filters non allowed coordinate inputs.
            if len(screen) + Y <= self.HEIGHT and len(screen) + Y >= 0:
                if len(screen[0]) + X <= self.WIDTH and len(screen[0]) + X >= 0:
                    # Checks if the given screen wil fit into the current screen with simple math.
                    return True
        return False

    def load_picture_file(self, X, Y, file):
        '''Converts a txt file containing ascii art into arrays/lists that then replace self.screen.  Also removes buggy characters such as newlines'''
        REAL_Y = len(self.screen) - (Y + 1)
        # Calculate the real Y values converted to a coordinate grid in math.
        with open(f'Visuals/{file}') as f:
            fresh_screen = f.read().split('\n')
            # Load the file into an array containing a string with newline removed for each line in the file.
        if self.verify_picture_file(X, REAL_Y, fresh_screen) == False:
            return False
            # Return if it won't fit.
        for i, line in enumerate(fresh_screen):
            self.screen[REAL_Y+i][X:X+len(line)] = list(line)
            # 1. Select the current line by taking the parameter Y and adding the current step.
            # 2. Make a slice starting from the value of parameter X untill X + the length of the current line.
            # 3. Replace the contents of the slice with the string converted to a char list.


def push_up(space):
    '''Prints X amount of newlines so the previous messages get pushed up.'''
    for _ in range(space):
        print()


if __name__ == "__main__":
    print("Wrong file!")
