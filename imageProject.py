# Import the Pillow library to allow us to open and manipulate images.
from PIL import Image

def main():
    
    # The parameter of the open function specifies
    # the location of the image you will manipulate.
    inputImage = Image.open('usfca_logo.png')
    imageWidth, imageHeight = inputImage.size
    
    #print(imageWidth)
    #print(imageHeight)

    copyImage(inputImage, imageWidth, imageHeight)
    flipHorizontal(inputImage, imageWidth, imageHeight)
    flipVertical(inputImage, imageWidth, imageHeight)
    makeGrayscale(inputImage, imageWidth, imageHeight)
    rotate(inputImage, imageWidth, imageHeight)
    swapCorners(inputImage, imageWidth, imageHeight)
    blur(inputImage, imageWidth, imageHeight)
    scaleLarger(inputImage, imageWidth, imageHeight)

def flipHorizontal(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel(((imageWidth-1-i), j), pixelColors)

    copyImageOutput.save('horizontalflip.png')

# Flips the image along the horizontal axis, effectively turning
# it upside down. The new image will be saved in a file called
# verticalFlip.png

def flipVertical(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((i, (imageHeight-1-j)), pixelColors)

    copyImageOutput.save('verticalflip.png')

# Converts the image to "black and white" by setting the red,
# green, and blue value for each pixel to be 30% of the old
# red value + 59% of the old green value + 11% of the old
# blue value for that pixel. The new image will be saved to a file 
# grayscale.png.

def makeGrayscale(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    
    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i,j))
            inputImageRed = pixelColors[0]
            inputImageGreen = pixelColors[1]
            inputImageBlue = pixelColors[2]
            newColor = int(inputImageRed*.3) + int(inputImageGreen*.59) + int(inputImageBlue*.11)
            newPixel = (newColor, newColor, newColor)
            copyImageOutput.putpixel((i,j), newPixel)
    copyImageOutput.save('grayscale.png')

# Rotates the image counter clockwise by 90 degrees. The new
# image will be saved in a file called 
# rotate.png.
def rotate(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageHeight, imageWidth), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((j,(imageWidth-1-i)), pixelColors)

    copyImageOutput.save('rotate.png')

# Creates a copy of an image given the image variable, its width, and height
def copyImage(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    
    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((i, j), pixelColors)

    copyImageOutput.save('copy.png')

def blur(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    #Handling the non-border
    for i in range(1, (imageWidth-1)):
        for j in range(1, (imageHeight-1)):
            pixelColors1 = inputImage.getpixel((i,j))
            pixelColors2 = inputImage.getpixel((i-1,j-1))
            pixelColors3 = inputImage.getpixel((i,j-1))
            pixelColors4 = inputImage.getpixel((i+1,j-1))
            pixelColors5 = inputImage.getpixel((i-1,j))
            pixelColors6 = inputImage.getpixel((i+1,j))
            pixelColors7 = inputImage.getpixel((i-1,j+1))
            pixelColors8 = inputImage.getpixel((i,j+1))
            pixelColors9 = inputImage.getpixel((i+1,j+1))
            pixelColorsAverageRed = (pixelColors1[0]+pixelColors2[0]+pixelColors3[0]+pixelColors4[0]+pixelColors5[0]+pixelColors6[0]+pixelColors7[0]+pixelColors8[0]+pixelColors9[0])/9
            pixelColorsAverageGreen = (pixelColors1[1]+pixelColors2[1]+pixelColors3[1]+pixelColors4[1]+pixelColors5[1]+pixelColors6[1]+pixelColors7[1]+pixelColors8[1]+pixelColors9[1])/9
            pixelColorsAverageBlue = (pixelColors1[2]+pixelColors2[2]+pixelColors3[2]+pixelColors4[2]+pixelColors5[2]+pixelColors6[2]+pixelColors7[2]+pixelColors8[2]+pixelColors9[2])/9

            blurRed = pixelColorsAverageRed
            blurGreen = pixelColorsAverageGreen
            blurBlue = pixelColorsAverageBlue

            blurColors = (int(blurRed), int(blurGreen), int(blurBlue))

            copyImageOutput.putpixel((i,j), blurColors)


    copyImageOutput.save('blur.png')

def swapCorners(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    #Top Left --> Bottom Right :)

    for i in range(0, int(imageWidth/2)):
        for j in range(0, int(imageHeight/2)):
            pixelColors = inputImage.getpixel((i,j))
            copyImageOutput.putpixel( ((int(imageWidth/2)+i), (int(imageHeight/2)+j)), pixelColors)
    #copyImageOutput.save('cornerswap.png')

    #Top Right --> Bottom Left :)

    for i in range(int(imageWidth/2), imageWidth):
        for j in range(0,int(imageHeight/2)):
            pixelColors = inputImage.getpixel((i,j))
            copyImageOutput.putpixel(( ( abs(int(imageWidth/2)-i)), int(imageHeight/2+j)) , pixelColors)
    #copyImageOutput.save('cornerswap2.png')

    #Bottom Left --> Top Right :)

    for i in range(0, int(imageWidth/2)):
        for j in range(int(imageHeight/2), imageHeight):
            pixelColors = inputImage.getpixel((i,j))
            copyImageOutput.putpixel( ((int(imageWidth/2))+i, abs(int(imageHeight/2)-j)), pixelColors)
    #copyImageOutput.save('cornerswap3.png')

    #Bottom Right --> Top Left :)

    for i in range(int(imageWidth/2), imageWidth):
        for j in range(int(imageHeight/2), imageHeight):
            pixelColors = inputImage.getpixel((i,j))
            copyImageOutput.putpixel( ((abs(int(imageWidth/2)-i)), abs(int(imageHeight/2-j))) , pixelColors)
    copyImageOutput.save('cornerswap.png')

def scaleLarger(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (2*imageWidth, 2*imageHeight), 'white')

    for i in range(1, (imageWidth-1)):
        for j in range(1,(imageHeight-1)):
            pixelColors = inputImage.getpixel((i,j))
           
            copyImageOutput.putpixel((i+i,j+j), pixelColors)
            copyImageOutput.putpixel((i+i+1,j+j), pixelColors)
            copyImageOutput.putpixel((i+i,j+j-1), pixelColors)
            copyImageOutput.putpixel((i+i+1,j+j-1), pixelColors)

    copyImageOutput.save('scaleLarger.png')

main()

