import pandas as pd

index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('Images\colors.csv', names=index, header=None)


def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

