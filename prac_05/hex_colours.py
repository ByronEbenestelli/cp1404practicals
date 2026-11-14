COLOUR_TO_HEX_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                      "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00",
                      "amethyst": "	#9966cc", "antiquewhite": "	#faebd7"}

colour = input("Enter a colour name: ").lower()
while colour != "":
    try:
        print(f"{colour} has hex code {COLOUR_TO_HEX_CODE[colour]}")
    except KeyError:
        print("Invalid colour name!")
    colour = input("Enter a colour name: ").lower()
