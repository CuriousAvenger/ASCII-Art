from PIL import Image
import ArtCond as logic

im = Image.open('Image.jpg','r')
pix_val = list(im.getdata())
width, height = im.size
print("[*] Reading Your Image & Converting to ASCII")

image = [[]]
row = 0
count = 1
try:
    for i in pix_val:
        logic.char_assign(image, row, i)
        count += 1

        if count == width+1:
            count = 1
            row += 1
            image.append([])
except TypeError:
    print("[!] Error: Corrupted File")
    exit()

print("[!] 0 <Normal Scaling> 1+ <Enlarged> -1+ <Reduced>")
scale = input("[+] Enter Your Scaling [Ex: -5]: ")
print("[*] Success! Follow Instruction to View Image")
if int(scale) <= -1:
    scale = abs(int(scale))
    with open("Image.txt", "w") as f:
        for i in range(len(image)):
            if i % int(scale) == 0:
                j = 0
                while j <= len(image[i]):
                    try:
                        if image[i][j] == image[i][j+1]: 
                            f.write(image[i][j])
                            j+= int(scale)
                        else:
                            logic.char_scale(image, i, j, f)
                            j+= int(scale)
                    except IndexError:
                        f.write("0")
                    j += 1
                f.write("\n")
            else:
                continue
elif int(scale) >= 1:
    scale = abs(int(scale))
    with open("Image.txt", 'w') as f:
        for i in image:
            for j in i:
                for _ in range(scale):
                    f.write(j)
            f.write("\n")
    f.close()
else:
    with open("Image.txt", 'w') as f:
        for i in image:
            for j in i:
                f.write(j)
            f.write("\n")
    f.close()