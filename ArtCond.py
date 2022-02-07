def char_assign(image, row, i):
    if i[0] >= 200 and i[1] >= 200 and i[2] >= 200:
        image[row] += "."
    elif i[0] <= 200 and i[0] >= 175 and i[1] <= 200 and i[1] >= 175 and i[2] <= 200 and i[2] >= 175:
        image[row] += "+"
    elif i[0] <= 175 and i[0] >= 150 and i[1] <= 175 and i[1] >= 150 and i[2] <= 175 and i[2] >= 150:
        image[row] += "|"
    elif i[0] <= 150 and i[0] >= 125 and i[1] <= 150 and i[1] >= 125 and i[2] <= 150 and i[2] >= 125:
        image[row] += "X"
    elif i[0] <= 125 and i[0] >= 100 and i[1] <= 125 and i[1] >= 100 and i[2] <= 125 and i[2] >= 100:
        image[row] += "0"
    elif i[0] <= 100 and i[0] >= 75 and i[1] <= 100 and i[1] >= 75 and i[2] <= 100 and i[2] >= 75:
        image[row] += "#"
    elif i[0] <= 100 and i[0] >= 75 and i[1] <= 100 and i[1] >= 75 and i[2] <= 100 and i[2] >= 75:
        image[row] += "%"
    elif i[0] <= 75 and i[0] >= 50 and i[1] <= 75 and i[1] >= 50 and i[2] <= 75 and i[2] >= 50:
        image[row] += "$"
    elif i[0] <= 50 and i[0] >= 25 and i[1] <= 50 and i[1] >= 25 and i[2] <= 50 and i[2] >= 25:
        image[row] += "&"
    elif i[0] <= 25 and i[1] <= 25 and i[2] <= 25:
        image[row] += "@"
    else:
        image[row] += "O"

def char_scale(image, i, j, f):
    if image[i][j] == "&" and image[i][j+1] == "@" or image[i][j] == "@" and image[i][j+1] == "&" :
        f.write("&")
    elif image[i][j] == "&" and image[i][j+1] == "O" or image[i][j] == "O" and image[i][j+1] == "&" :
        f.write("O")
    elif image[i][j] == "$" and image[i][j+1] == "@" or image[i][j] == "@" and image[i][j+1] == "$" :
        f.write("$")
    elif image[i][j] == "$" and image[i][j+1] == "&" or image[i][j] == "&" and image[i][j+1] == "$" :
        f.write("&")
    elif image[i][j] == "$" and image[i][j+1] == "O" or image[i][j] == "O" and image[i][j+1] == "$" :
        f.write("$")
    elif image[i][j] == "$" and image[i][j+1] == "#" or image[i][j] == "#" and image[i][j+1] == "$" :
        f.write("#")
    elif image[i][j] == "0" and image[i][j+1] == "#" or image[i][j] == "#" and image[i][j+1] == "0" :
        f.write("0")
    elif image[i][j] == "@" and image[i][j+1] == "O" or image[i][j] == "O" and image[i][j+1] == "@" :
        f.write("@")
    elif image[i][j] == "&" and image[i][j+1] == "#" or image[i][j] == "#" and image[i][j+1] == "&" :
        f.write("#")
    elif image[i][j] == "@" and image[i][j+1] == "#" or image[i][j] == "#" and image[i][j+1] == "@" :
        f.write("&")
    elif image[i][j] == "0" and image[i][j+1] == "&" or image[i][j] == "&" and image[i][j+1] == "0" :
        f.write("0")
    elif image[i][j] == "0" and image[i][j+1] == "$" or image[i][j] == "$" and image[i][j+1] == "0" :
        f.write("$")
    elif image[i][j] == "#" and image[i][j+1] == "O" or image[i][j] == "O" and image[i][j+1] == "#" :
        f.write("#")
    elif image[i][j] == "X" and image[i][j+1] == "$" or image[i][j] == "$" and image[i][j+1] == "X" :
        f.write("X")
    elif image[i][j] == "X" and image[i][j+1] == "&" or image[i][j] == "&" and image[i][j+1] == "X" :
        f.write("X")
    else:
        f.write("/")