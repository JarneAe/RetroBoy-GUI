import pandas as pd
import PIL.ImageGrab

index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('F:\RetroBoy-GUI\Images\colors.csv', names=index, header=None)

def find_colors():
    rgb = PIL.ImageGrab.grab().load()[1069,749]

    delimiter = ','
    rgb_str = delimiter.join([str(value) for value in rgb])

    rgbsplit = rgb_str.split(',')
    R = int(rgbsplit[0])
    G = int(rgbsplit[1])
    B = int(rgbsplit[2])
    return R,G,B

def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

