import re
import os
import codecs
import json
import urllib.parse
import urllib.request
import yaml

def getmd(type):
    dir0 = "../"+type
    dirl = os.listdir(dir0)
    totaltext = ""
    for apiname in dirl:
        inputmdname = "../"+ type +"/"+ apiname + "/" + apiname + '.md'
        try:
            mdtext = ""
            inputfile = codecs.open(inputmdname, "r", 'utf-8')
            while 1:
                line = inputfile.readline()
                if not line:
                    break
                mdtext += line
            inputfile.close()
            mtext = "## " + apiname + "\n\n" + mdtext
            totaltext = totaltext + "\n\n" + mtext
        except:
            pass
    return totaltext

if __name__ == "__main__":

    typelist = ['Instance', 'Disk', 'Snapshot', 'Image', 'Net', 'SecurityGroup', 'Regions', 'Monitor', 'Other']
    mdtext = ""
    for x in typelist:
        mdtext = mdtext + getmd(x)
    
    outputmdname = "../instance.md"
    outputmdfile = codecs.open(outputmdname, "w", 'utf-8')
    outputmdfile.write(mdtext)
