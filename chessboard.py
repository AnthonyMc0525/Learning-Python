from sys import argv

script, size = argv

def chessboard(size):
    new_size = int(size / 2)
    i = 0
    while i < new_size: 
        print(' #' * new_size + '\n')
        print('# '* new_size + '\n')
        i += 1
    if size % 2 == 1:
        print(' #' * new_size + '\n')

chessboard(int(size))
