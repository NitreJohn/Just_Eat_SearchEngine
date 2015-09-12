# encoding=utf-8
import Image
import os

info = "I:/1st Year/First_Year_Summer_Semester/Program/Python/Web Bug/Practice/Images"
listfile = os.listdir(info)
print listfile

for line in listfile:
    if (line[-4:] == '.jpg'):
        im = Image.open(line.encode('utf-8'), "r")
        width = im.size[0]
        height = im.size[1]
        if width * 3 >= height * 4:
            im = im.resize((300 * width / height + 1, 300))
        else:
            im = im.resize((400, 400 * height / width + 1))
        im = im.crop((0, 0, 400, 300))
        im.save("converted/" + line, "JPEG")
        print line
