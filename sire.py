#   
#   Image API used in SonoBouy
#   David Kroell
#

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
    # This method takes a photo and flips it in
    # the field so that we get a mirror image copy
    # of the image in the current object.
    #
    def flip(self, image_normal):
        pass
        
