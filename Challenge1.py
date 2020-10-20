import tkinter as tk
from tkinter import ttk
from  tkinter import *
from tkinter import font
import random

root = tk.Tk()
root.title("Change Background")
root.resizable(400, 100)


def clickMe():
    dictt = {'#FAF0E6': 'Linen', '#FAFAD2': 'Light goldenrod yellow', '#FDF5E6': 'Old lace', '#FF0000': 'Red',
             '#FF00FF': 'Fuchsia', '#FF1493': 'Deep pink', '#FF4500': 'Orange red', '#FF6347': 'Tomato',
             '#FF69B4': 'Hot pink', '#FF7F50': 'Coral', '#FF8C00': 'Dark orange', '#FFA07A': 'Light salmon',
             '#FFA500': 'Orange', '#FFB6C1': 'Light pink', '#FFC8CB': 'Pink', '#FFD700': 'Gold',
             '#FFDAB9': 'Peach puff', '#FFDEAD': 'Navajo white', '#FFE4B5': 'Moccasin', '#FFE4C4': 'Bisque',
             '#FFE4E1': 'Misty rose', '#FFEBCD': 'Blanched almond', '#FFEFD5': 'Papaya whip',
             '#FFF0F5': 'Lavender blush', '#FFF5EE': 'Sea shell', '#FFF8DC': 'Cornsilk', '#FFFACD': 'Lemon chiffon',
             '#FFFAF0': 'Floral white', '#FFFAFA': 'Snow', '#FFFF00': 'Yellow', '#FFFFE0': 'Light yellow',
             '#FFFFF0': 'Ivory', '': '', '#BDB76B': 'Dark khaki', '#C0C0C0': 'Silver', '#C71585': 'Medium violet red',
             '#CD5C5C': 'Indian red', '#CD853F': 'Peru', '#D2691E': 'Chocolate', '#D2B48C': 'Tan',
             '#D3D3D3': 'Light grey', '#D8BFD8': 'Thistle', '#DA70D6': 'Orchid', '#DAA520': 'Goldenrod',
             '#DB7093': 'Pale violet red', '#DC143C': 'Crimson', '#DCDCDC': 'Gainsboro', '#DDA0DD': 'Plum',
             '#DEB887': 'Burlywood', '#E0FFFF': 'Light cyan', '#E6E6FA': 'Lavender', '#E9967A': 'Dark salmon',
             '#EE82EE': 'Violet', '#EEE8AA': 'Pale goldenrod', '#F08080': 'Light coral', '#F0E68C': 'Khaki',
             '#F0F8FF': 'Alice blue', '#F0FFF0': 'Honeydew', '#F0FFFF': 'Azure', '#F4A460': 'Sandy brown',
             '#F5DEB3': 'Wheat', '#F5F5DC': 'Beige', '#F5F5F5': 'Whitesmoke', '#F5FFFA': 'Mint cream',
             '#F8F8FF': 'Ghost white', '#FA8072': 'Salmon', '#6A5ACD': 'Slate blue', '#6B8E23': 'Olive drab',
             '#778899': 'Light slate gray', '#7B68EE': 'Medium slate blue', '#7CFC00': 'Lawn green',
             '#7FFF00': 'Chartreuse', '#7FFFD4': 'Aquamarine', '#800000': 'Maroon', '#800080': 'Purple',
             '#808080': 'Gray', '#87CEEB': 'Sky blue', '#87CEFA': 'Light sky blue', '#8A2BE2': 'Blue violet',
             '#8B0000': 'Dark red', '#8B008B': 'Dark magenta', '#8B4513': 'Saddle brown', '#8DBC8F': 'Dark seagreen',
             '#90EE90': 'Light green', '#9370DB': 'Medium purple', '#9400D3': 'Dark violet', '#98FB98': 'Pale green',
             '#9932CC': 'Dark orchid', '#9ACD32': 'Yellow green', '#A0522D': 'Sienna', '#A52A2A': 'Brown',
             '#A9A9A9': 'Dark gray', '#ADD8E6': 'Light blue', '#ADFF2F': 'Green yellow', '#AFEEEE': 'Pale turquoise',
             '#B0C4DE': 'Light steel blue', '#B0E0E6': 'Powder blue', '#B22222': 'Firebrick',
             '#B8860B': 'Dark goldenrod', '#BA55D3': 'Medium orchid', '#000000': 'Black', '#000080': 'Navy',
             '#00008B': 'Dark blue', '#0000CD': 'Medium blue', '#0000FF': 'Blue', '#006400': 'Dark green',
             '#008000': 'Green', '#008080': 'Teal', '#008B8B': 'Dark cyan', '#00BFFF': 'Deep sky blue',
             '#00DED1': 'Dark turquoise', '#00FA9A': 'Medium spring green', '#00FF00': 'Lime',
             '#00FF7F': 'Spring green', '#00FFFF': 'Cyan', '#191970': 'Midnight blue', '#1E90FF': 'Dodger blue',
             '#20B2AA': 'Light sea green', '#228B22': 'Forest green', '#2E8B57': 'Seagreen',
             '#2F4F4F': 'Dark slate gray', '#32CD32': 'Lime green', '#3CB371': 'Medium sea green',
             '#40E0D0': 'Turquoise', '#4169E1': 'Royal blue', '#4682B4': 'Steel blue', '#483D8B': 'Dark slate blue',
             '#48D1CC': 'Medium turquoise', '#4B0082': 'Indigo', '#556B2F': 'Dark olive green', '#5F9EA0': 'Cadet blue',
             '#6495ED': 'Cornflower blue', '#66CDAA': 'Medium aquamarine', '#BC8F8F': 'Rosy brown', '#FFFFFF': 'White',
             '#696969': 'Dim gray', '#FAEBD7': 'Antique white'}
    a = list(dictt.keys())
    bgcolors = random.choice(a)
    color_name = dictt[bgcolors]
    root.configure(background=bgcolors)
    fonts = font.families()
    random_font =random.choice(fonts)
    bgcolors_label = "The code of this color is " + str(bgcolors) + " and name is " + str(color_name) +'\n\n'+"The font family is "+str(random_font)
    label.configure(text=str(bgcolors_label), background=bgcolors,font=(str(random_font),"23"))


label = ttk.Label(font=("tahoma", "23", "normal"))
btn = ttk.Button(text="Change Color", command=clickMe)
btn.grid(column=0, row=0)
label.grid(column=3, row=5, pady=50)

root.mainloop()
