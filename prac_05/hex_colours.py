"""Hex Colour
designed to the hex colour code when the colour is given
"""

HEX_COLOURS = {"aliceblue": "#f0f8ff", "blue1": "#0000ff", "black": "#000000",
               "green1": "#00ff00", "pink": "#ffc0cb", "purple": "#9b30ff",
               "red": "#ff0000", "white": "#ffffff", "yellow": "#ffff00",
               "gray50": "#828282"}

colour = input("Please pick a colour: ").lower()
while colour != "":
    if colour in HEX_COLOURS:
        print("The hex code is: {}".format(HEX_COLOURS[colour]))
    else:
        print("Invalid Response")
    colour = input("Please pick a colour: ").lower()
print("Thank you")
