from reader import Reader



# creates an object of the reader class
# based upon given input values
x = Reader('input.txt')

x.instantiate()

x.placements()

x.update_board()

x.roam_and_kill()
