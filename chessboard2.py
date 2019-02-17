def make_board(size)
string = ''
for line in range(0, size):
    for char in range(0, size):
        if line % 2 == 0:
            string += ' ' if char % 2 == 0 else '#'
        else:
            string += '#' if char % 2 == 0 else ' 

            
