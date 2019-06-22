driver.py to be run in the terminal window for full effect


full effect: 

Example input:
(changeable in input.txt which a python file reads and interprets)

10 x 10 grid
Fish, strength 9, Male, baby.    coord: 9,0
Bear, strength 4, Female   coord: 0,0
Fish, strength 9, Female   coord: 9,9
Bear, strength 8, Male, baby   coord: 0,9

b - - - - - - - - F (9,9)
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
B - - - - - - - - f (0,9)
(0,0)



the grid resets, in place, in the intermin windows.. around every .5 seconds, but this again is configurable. It gives the appearance of the Fs and Bs actually moving around.

The Fs and Bs can go up, left, right, down, or stay still. if they land on another animal, they may fight. the higher strength wins. TODO:introduce probability
