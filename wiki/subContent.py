import re
import os
import sys
# info=os.getcwd()
# listfile=os.listdir(os.getcwd())

info = u"I:/1st Year/First_Year_Summer_Semester/Program/HTML/hw/hw/wiki"
listfile = os.listdir(info)

for fileName in listfile:
    if fileName[-1] == "l":
        f = open(fileName)
        tempString = f.read()
        f.close()
        f = open(fileName, "w")
        tempString = re.sub("<p>", "<p class = 'col-md-8'>", tempString)
        f.write(tempString)
        f.close()
