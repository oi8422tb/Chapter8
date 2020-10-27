from images import Image
def sepia(image):
    # converting image to grayscale
    grayscale(image)
    #now looping through each row and column
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            #adjusting r and b components as needed
            if r<63:
                r=int(r*1.1)
                b=int(b*0.9)
            elif r<192:
                r = int(r * 1.15)
                b = int(b * 0.85)
            else:
                r = min(int(r * 1.08),255)
                b = int(b * 0.93)
            #setting the adjusted values
            image.setPixel(x, y, (r, g, b))

def grayscale(image):
    #Converts an image to grayscale
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    sepia(image)
    image.draw()

if __name__ == "__main__":
    main()