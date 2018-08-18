from reader import Reader


x = Reader('input.txt')
x.instantiate()
x.placements()
x.update_board()
x.roam_and_kill()



# print('Type in two different integers, separated by spaces, to represent the x and y lengths of a grid')
# gridsize = input()
# print('Type how many moves you would like the program to execute')
# moves = input()
# print('Type B or F (for bear or fish) followed by 3 numbers separated by spaces (x-location, y-location, and strength). type stop to stop.')
# longstring = ''
# creatures = ''
# while input:
#     creatures = input()
#     if creatures is '':
#         break
#     longstring = creatures + '\n'
# f = open('document.txt', 'w')
# f.write(gridsize)
# f.write('\n')
# f.write(moves)
# f.write('\n')
# f.write(longstring)
