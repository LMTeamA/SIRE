#   
#   Image API used in SonoBouy
#   David Kroell
#

from Tkinter import *
from PIL import Image, ImageTk

class Image():
    def __init__(self, path):
        self.image_path = path
        self.image_mutations = []

        # Import image and hold it.
        self.img = Image.open(self.image_path)

        # Record rotational state of the image.
        self.recordRotationalMutations()

        
    #
    # This method rotates the image and records the image
    # at each rotation state.
    #
    def recordRotationalMutations(self):
        # Specify which angles we are holding images at
        ANGLES = [45, 90, 135, 180, 225, 270, 315, 360]

        # Loop through and record the image at each angle
        for angle in ANGLES:
            tempimg = self.img.rotate(angle)
            self.image_mutations.append(tempimg)
        
    #
    # This method takes the inverse of the image and
    # records it at each rotational stage.
    #
    def recordInverseState(self):
        tempImg = self.img
        self.img

    #
    # This method opens up the image on a window pop
    # up on the user's desktop.
    #
    def show(self, height=1000, width=1000):

        h=height
        w=width
        
        root = Tk()
        
        dimensions = str(h)+"x"+str(w)
        root.geometry(dimensions)
        
        canvas = Canvas(root,width=(w-1),height=(h-1))
        canvas.pack()
        
        image = ImageTk.PhotoImage(self.img)
        imagesprite = canvas.create_image(h,w,image=image)
        root.mainloop()
        
        
        
