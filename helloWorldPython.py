#!/usr/bin/env python

# Hello World in GIMP Python

from gimpfu import *

def create_rectangle(image, drawable, x, y, width, height):
    ## Set the foreground color to black
    pdb.gimp_context_set_foreground((0, 0, 0, 255))

    ## Create a new layer for the rectangle
    layer = pdb.gimp_layer_new(image, width, height, RGBA_IMAGE, "Rectangle", 100, NORMAL_MODE)
    pdb.gimp_image_insert_layer(image, layer, None, 0)

    ##set the position of the layer
    layer.set_offsets(20, 20)

    ##Create a selection in the shape of the rectangle
    pdb.gimp_rect_select(image, x, y, width, height, CHANNEL_OP_REPLACE, False, 0)

    ##Edit the selection to add a border
    pdb.gimp_selection_border(image, 3)

    ## Fill the selection with the foreground color to create the border
    pdb.gimp_edit_fill(layer, FOREGROUND_FILL)

    ## Clear the selection
    pdb.gimp_selection_none(image)

    ## Refresh the display
    gimp.displays_flush()

def hello_world(initstr, font, size, color) :
    ## Maddie Notes:
    ## I removed the comic sans check 
    ##also changed the image size
    ##it's no longer the size of the text
    ##it is now 250 x 350, (a standard playing card is 2.5 x 3.5 inches)

    # Make a new image. Size 10x10 for now -- we'll resize later.
    img = gimp.Image(250, 350, RGB)

    # Save the current foreground color:
    pdb.gimp_context_push()

    # Set the text color
    gimp.set_foreground(color)

    # Create a new text layer (-1 for the layer means create a new layer)
    layer = pdb.gimp_text_fontname(img, None, 10, 25, initstr, 10,
                                   True, size, PIXELS, font)

    # Resize the image to the size of the layer
    ##I commented this out because it changes the size of the image
   # img.resize(layer.width, layer.height, 0, 0)

    # Background layer.
    # Can't add this first because we don't know the size of the text layer.
    ##yes we can because we do know that information bc its hardcoded now
    background = gimp.Layer(img, "Background", 250, 350,
                            RGB_IMAGE, 100, NORMAL_MODE)
    background.fill(BACKGROUND_FILL)
    img.add_layer(background, 1)

    create_rectangle(img, layer, 20, 20, 210, 310)

    # Create a new image window
    gimp.Display(img)
    # Show the new image window
    gimp.displays_flush()

    # Restore the old foreground color:
    pdb.gimp_context_pop()

register(
    "python_fu_hello_world",
    "Hello world image",
    "Create a new image with your text string",
    "Akkana Peck (edits by Maddie Mayans)",
    "Akkana Peck",
    "2010",
    "Hello world (Py)...",
    "",      # Create a new image, don't work on an existing one
    [
        (PF_STRING, "string", "Text string", 'Hello, world!'),
        (PF_FONT, "font", "Font face", "Sans"),
        (PF_SPINNER, "size", "Font size", 50, (1, 3000, 1)),
        (PF_COLOR, "color", "Text color", (1.0, 0.0, 0.0))
    ],
    [],
    hello_world, menu="<Image>/File/Create")

main()
