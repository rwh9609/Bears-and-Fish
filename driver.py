from reader import Reader



# creates an object of the reader class
# based upon given input values
x = Reader('input.txt')

# creates an empty matrix based on inputted values
x.instantiate()

# places the animals in spots specified by the input file
x.placements()

# updates board after the placement of animals have been assigned
x.update_board()


# updates the board continuously based on the number of moves inputted from the data file
x.roam_and_kill()
