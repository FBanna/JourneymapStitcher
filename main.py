from PIL import Image, ImageDraw
from os import *
import math

directory = "day"
outputfile = "out"

################
#              #
#   CREATION   #
#              #
################

def creation(startingx, startingy, width, height, out):
    print("creation callled with: ", startingx,startingy,width,height, "saving to:", out)
    name = str()
    filename2 = str()
         
    img = Image.new(mode = "RGB", size = (width*512, height*512), color = "white")

    for xaxis in range(0, width):
        
        
        for yaxis in range(0, height):

            x = xaxis + startingx

            y = yaxis + startingy

            #print(x,y)

          
            targetfile = directory + "/" + str(x) + "," + str(y) + ".png"

            
            if path.exists(targetfile):
                print(targetfile, "exists")
                tempimg = Image.open(targetfile)
                img.paste(tempimg, ((xaxis)*512,(yaxis)*512))

    img.save(out + ".jpg", quality=100)

#############
#           #
#   INPUT   #
#           #
#############


style = int(input("1) span, one point to another\n2) center, center point and equal radius\nenter style number: "))

if style == 1:
    startx = int(input("x coord 1: "))
    starty = int(input("y coord 1: "))

    endx = int(input("x coord 2: "))
    endy = int(input("y coord 2: "))

    #important
    xsize = round(abs((startx - endx)/512))
    ysize = round(abs((starty - endy)/512))

    if startx < endx:
        startxtile = round(startx/512)
    else:
        startxtile = round(endx/512)

    if starty < endy:
        startytile = round(starty/512)
    else:
        startytile = round(endy/512)

    print("\n("+str(startx) + ", " + str(starty) + ")\nto\n("+str(endx) + ", " + str(endy) + ")\n")

    
elif style == 2:
    centerx = int(input("center x coord: "))
    centery = int(input("center y coord: "))
    radius = int(input("radius in blocks: "))

    #important
    xsize = round((radius*2)/512)
    ysize = round((radius*2)/512)

    startxtile = round((centerx-radius)/512)
    startytile = round((centery-radius)/512)

    print("\n("+str(centerx-radius)+ ", "+ str(centery-radius)+")\nto\n"+str(centerx + radius)+", " + str(centery+radius)+")\n")

else:
    print("please enter valid style!")
    exit()


print("starting at:", str(startxtile) + ", " + str(startytile) + "\n")
print("x width =", xsize, "tiles\n")
print("y width =", ysize, "tiles\n")
input("press enter to start :)")

###############
#             #
#   Calling   #
#             #
###############

if xsize > 127 or ysize > 127:
    print("image too large! SPLITTING")


    #FIND CENTER

    midx = startxtile+round(xsize/2)
    midy = startxtile+round(ysize/2)

    imagesizex = round(midx-startxtile)
    imagesizey = round(midy-startytile)
    

    #neededx = xsize/127
    #neededy = xsize/127
    print(midx,midy)

    if(midx-startxtile>127):
        while(imagesizex>127):
            print(imagesizex, "xsize too big halved!")
            imagesizex = round(imagesizex/2)
        print("xsize is now", imagesizex)

    if(midy-startytile>127):
        while(imagesizey>127):
            print(imagesizey, "ysize too big halved!")
            imagesizey = round(imagesizey/2)
        print("ysize is now", imagesizey)

    neededx = xsize/imagesizex
    neededy = ysize/imagesizey
    print("split into", math.ceil(neededx*neededy), "different images, each with size of:", str(imagesizex)+", "+ str(imagesizey))

    input("press enter to start :) (again)")    
        

    
    
    #neededx = math.ceil(xsize/127)
    #neededy = math.ceil(xsize/127)
    #print("spit into", neededx*neededy, "images")

    for ximages in range(0, math.ceil(neededx)):
        for yimages in range(0,math.ceil(neededy)):

            
            
            x = ximages*imagesizex + startxtile
            y = yimages*imagesizey + startytile
            savename = str("out" + str(ximages) + ", " + str(yimages))

            print("calling creation with", x,y,127,127,str(savename))
            creation(x,y,imagesizex,imagesizey, str(savename))
     
    

    exit()

creation(startxtile, startytile, xsize, ysize, outputfile)
    
    








