from PIL import Image
im=Image.open("meme.jpg")
im.show()
im.getdata()

data=list(im.getdata())
data2=[]
for element in data:
    color=sum(element)
    if color <182:
       data2.append((0,51,76))
    elif color < 364:
        data2.append((217,26,33))
    elif color < 546:
        data2.append((112,150,158))
    else:
        data2.append((252,227,166))

im.putdata(data2)
im.show(2)



