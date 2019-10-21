# imageManipulation
Uses the Pillow library's image module to manipulate the input image (the logo of the University of San Francisco) and create new png files.

Each function first takes in the original dimensions and creates a blank image to place pixels on.
The pixels are placed onto the blank using nested for loops, where i is the column and j is the row.

copyImage uses the original dimensions and colors to make a copy.

flipHorizontal places the pixels with the same vertical position but has the horizontal position in reverse order.

flipVertical places the pixels with the same horizontal position but has the vertical position in reverse order.

makeGrayscale takes in each RGB value in a tuple and multiplies red by .3, green by .59, blue by .11.
  The new color values are added up and placed with the original pixel positions.
(adjustments taken from https://en.wikipedia.org/wiki/Grayscale)

rotate takes the original dimensions and creates a canvas with reversed height and width. The pixels are placed with the 
  height in the width position and the width placed in reverse order.

swapCorners uses four nested loops. Each loop takes in pixels from each quadrant and places them in the opposite corner.

blur takes in the RGB values of each pixel and its surrounding 8 (3x3 grid) and averages the value out for placement.

scaleLarger creates a blank image with twice the dimensions and places each pixel in 2x2 grids.
