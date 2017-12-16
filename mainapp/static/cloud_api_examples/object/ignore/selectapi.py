# -*- coding:utf-8 -*-  
import re
import os
import codecs
import yaml

type = 3
out = 1

def getp():
    inputfilename = "1.html"
    outputfilename = "temp.yaml"
    t = {}
    tl = []
    html = ""
    inputfile = codecs.open(inputfilename, "r", 'utf-8')
    while 1:
        line = inputfile.readline()
        if not line:
            break
        line = line.replace("\n", "")
        line = line.replace("\r", "")
        html += line
    inputfile.close()
    pattern = re.compile("<td>(.+?)</td>")
    li = pattern.findall(html)
    for i in range(0, len(li)):
        if i % type != 0:
            continue
        para = {}
        para['name'] = li[i]
        para['type'] = li[i+1].lower()
        if(para['type'] == 'int' or para['type'] == 'number'):
            para['type'] = 'integer'
        if(para['type'] == 'datetime'):
            para['type'] = 'string'
        if(para['type'] == 'bool'):
            para['type'] = 'boolean'
        if(type == 4):
            if(li[i+2] == u'是'):
                para['required'] = True
            else:
                para['required'] = False
        para['description'] = li[i+type-1]
        #para['in'] = 'query'
        t[li[i]] = para
        para1 = para
        #para1['in'] = 'query'
        tl.append(para1)
    
    outputfile = codecs.open(outputfilename, "w", 'utf-8')
    if out == 1:
        yaml.dump(t, default_flow_style=False,stream=outputfile,indent=4,encoding='utf-8',allow_unicode=True, width=1000)
    if out == 2:
        yaml.dump(tl, default_flow_style=False,stream=outputfile,indent=4,encoding='utf-8',allow_unicode=True, width=1000)
    return t

if __name__ == "__main__":
    getp()