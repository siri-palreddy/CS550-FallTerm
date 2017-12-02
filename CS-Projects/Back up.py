# import the libraries you'll need
import tkinter
from tkinter import *
import random

# recursive mandelbrot function gives us the number of iterations to escape
def mandelbrot(z, c, count):
         # calculate z squared plus c to get our new z value
         z = z*z + c

         # update iteration counter
         count = count + 1

         # if we escape or we hit the max number of iterations
         # stop executing and return the number of iterations
         if ((count>=maxIt) or (abs(z) > 2)):
                 return count


         # otherwise, since we didn't escape or hit the max iterations,
         # calculate a new z again (call mandelbrot function again)

         return mandelbrot(z, c, count)


# variables we will use throughout the program
WIDTH = 640 # width and height of our picture in pixels
HEIGHT = 640
maxIt = 255 # max iterations; corresponds to color

# create a new Tkinter window
window = Tk()

# create a canvas, and place it in the window
canvas = Canvas(window, width = 3 * WIDTH, height = HEIGHT, bg = "#000000")

#Create a set to store images
Imgs = []
totalFractals = 3

# Itarate to generate multiple fractals
for curFractal in range(totalFractals):
     # loop through all the pixels in the image
     a = random.uniform(-1, 1)
     j = random.uniform(-1, 1)
     #a = 0.285
     #j = 0.01
     randR = random.randint(2,8)
     randG = random.randint(4,16)
     randB = random.randint(9,32)
     img = PhotoImage(width = WIDTH, height = HEIGHT)

     # Use center image with normal zoom
     if (curFractal == 1):
         xmin = -2
         ymin = -2
     else:
         xmin = random.uniform(-2, -0.5)
         ymin = xmin

     xmax = abs(xmin)
     ymax = abs(ymin)

     for row in range(HEIGHT):
         for col in range(WIDTH):
             # calculate Color for each pixel
             z = complex(xmin + (xmax - xmin) * col / (WIDTH), ymin + 
(ymax - ymin) * row / (HEIGHT))

             c = complex(a,j)
             # execute the mandelbrot calculation
             mandelVal =mandelbrot(z, c,0)

             rd = hex(mandelVal % randR * 32)[2:].zfill(2)
             gr = hex(mandelVal % randG * 16)[2:].zfill(2)
             bl = hex(mandelVal % randB  * 8)[2:].zfill(2)


             # update the pixel at the current position to hold
             # the color we created with the mandelbrot result
             img.put("#" + rd + gr + bl, (col, row))
     Imgs.append(img)

# update the canvas and display our drawing
k = 0
for img in Imgs:
     canvas.create_image(640*k,0, image = img, state = "normal", anchor 
= tkinter.NW)
     k+= 1

canvas.pack()

mainloop()


