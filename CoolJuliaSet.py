# import the libraries you'll need
import tkinter
from tkinter import *
import random

# recursive mandelbrot function gives us the number of iterations to escape
def mandelbrot(z, c, count):
        # the calculations that follow are how you would do it
        # if you didn't use complex numbers in python;
        # like we did on your worksheet.

        

        # calculate z squared
        

        # calculate z squared plus c to get our new z value
        z = z*z + c

        # update iteration counter
        count = count + 1

        # if we escape or we hit the max number of iterations
        # stop executing and return the number of iterations
        if ((count>=maxIt) or (abs(z) >= 2)):
                return count


        # otherwise, since we didn't escape or hit the max iterations,
        # calculate a new z again (call mandelbrot function again)

        return mandelbrot(z, c, count)


# variables we will use throughout the program
WIDTH = 640 # width and height of our picture in pixels
HEIGHT = 640
xmin = -2.0 # the zoom we want to see
xmax = 2
ymin = -2.0
ymax = 2.0
maxIt = 255 # max iterations; corresponds to color
#xvalues = linspace(-2, 2, 1000)
#yvalues = linspace(-2, 2, 1000)

# create a new Tkinter window
window = Tk()

# create a canvas, and place it in the window
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "#000000")

# set up the canvas so it can hold a picture
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)

# loop through all the pixels in the image
for row in range(HEIGHT):
    for col in range(WIDTH):
        # calculate C for each pixel
        z = complex(xmin + (xmax - xmin) * col / WIDTH, ymin + (ymax - ymin) * row / HEIGHT)
        # set z to 0
        #z = complex(xvalues[row],yvalues[col])
        a = random.randint(-1, 0)
        j = random.randint(-1, 0)

        c = complex(a, j)

        # execute the mandelbrot calculation
        mandelVal =mandelbrot(z, c,0)

        # use the mandelbrot result to create a color
        rd = hex(mandelVal % 7 * 20)[2:].zfill(2)
        gr = hex(mandelVal % 9 * 10)[2:].zfill(2)
        bl = hex(mandelVal % 15 * 15)[2:].zfill(2)


        # update the pixel at the current position to hold
        # the color we created with the mandelbrot result
        img.put("#" + rd + gr + bl, (col, row))

# update the canvas and display our drawing
canvas.pack()
mainloop()