# -*- coding:utf-8 -*-  
import re
import os
import codecs
import json
import urllib.parse
import urllib.request
import yaml

urlbase = "https://southeastasia.api.cognitive.microsoft.com/luis/v2.0/apps/5b8c7ae0-e07f-41ea-952f-df4650a8e3a3?subscription-key=33ef89021a6946159ab04663b4b78874&verbose=true&timezoneOffset=0&q="
mode = 2
apitype = u'组管理接口'

def getp(html, type, out, inq):   #表格处理
    
    outputfilename = "para" + str(type) + str(out) + ".yaml"
    t = {}
    tl = []
    #print(html)
    pattern = re.compile("<h[3-5](.*?)</ul>")
    ul = pattern.findall(html)
    #print(len(li))

    for x in ul:
        pattern = re.compile("<li>(.*?)</li>")
        li = pattern.findall(x)
        
        para = {}
        pattern = re.compile(">([a-zA-Z0-9.]*?)</h[3-5]>")
        na = pattern.findall(x)
        para['name'] = na[0]
        otherword = ""
        for y in li:
            if u"：" not in y:
                #print(y)
                continue
            index = y.find(u"：")
            yt = y[0:index]
            word = y[index+1:]

            word = word.replace('<code>', "")
            word = word.replace('</code>', "")
            
            if u'类型' in yt:
                para['type'] = word.lower()
            elif u'名称' in yt:
                pass
            elif u'必须' in yt:
                para['required'] = word
            elif u'描述' in yt:
                para['description'] = word
            elif u'格式' in yt:
                para['pattern'] = word
            elif u'默认' in yt:
                para['default'] = word
            else:
                otherword = otherword+";"+ y
        para['description'] = para['description'] + otherword
        if(para['type'] == 'int'):
            para['type'] = 'integer'
        if(para['type'] == 'datetime'):
            para['type'] = 'string'
        if(para['type'] == 'bool'):
            para['type'] = 'boolean'
        if(para['type'] == 'float' or para['type'] == 'double'):
            para['type'] = 'number'
        try:
            if(u'是' in para['required']):
                para['required'] = True
            else:
                para['required'] = False
        except:
            pass
        if(len(inq)>0):
            para['in'] = inq
        t[para['name']] = para
        tl.append(para)
    outputfile = codecs.open(outputfilename, "w", 'utf-8')
    if out == 1:
        if mode == 2:
            for x in t:
                t[x] = getsentence(t[x])
        yaml.dump(t, default_flow_style=False,stream=outputfile,indent=4,encoding='utf-8',allow_unicode=True, width=1000)
        return t
    if out == 2:
        yaml.dump(tl, default_flow_style=False,stream=outputfile,indent=4,encoding='utf-8',allow_unicode=True, width=1000)
        return tl
    return
def gete(html, err):   #错误码表
    er = {}
    outputfilename = "err" + ".yaml"
    
    pattern = re.compile("<h[3-5](.*?)</ul>")
    ul = pattern.findall(html)
    #print(ul)
    #print(len(li))

    for x in ul:
        pattern = re.compile("<li>(.*?)</li>")
        
        li = pattern.findall(x)
        para = {}
        pattern = re.compile(">(.*?)</h[3-5]>")
        #print(x)
        na = pattern.findall(x)
        if len(li) == 0:
            continue
        index = li[0].find(u"：")
        key = int(li[0][index+1:])
        if key not in er:
            er[key] = ""
        er[key] = er[key] + "{code: " + na[0]
        index = li[1].find(u"：")
        description = li[1][index+1:]
        er[key] = er[key] + ", describeen: " + description
        er[key] = er[key] + "}, "

    for x in er:
        if x in err:
            err[x]['description'] = err[x]['description'] + ',' + er[x]
            err[x]['description'] = err[x]['description'][:-2]
        else:
            err[x] = {}
            err[x]['description'] = er[x][:-2]

    outputfile = codecs.open(outputfilename, "w", 'utf-8')
    yaml.dump(err, default_flow_style=False,stream=outputfile,indent=4,encoding='utf-8',allow_unicode=True, width=1000)
    return err
def getsentence(z):    #NLP提取
    #print(z)
    sentence = z['description']
    while "  " in sentence:
        sentence = sentence.replace("  ", "")
    z['description'] = sentence
    sentences = sentence.split(u"。")
    for y in sentences:
        
        p = re.compile("<.*?>")
        yy = re.sub(p, "", y)
        if len(y) > 0:
            if re.search(u'[a-zA-Z0-9空无]', yy):
                url = urlbase + urllib.parse.quote(y) 
                response = urllib.request.urlopen(url)
                page = response.read()
                page = page.decode('utf-8')
                mes = json.loads(page)
                
                for x in mes['entities']:
                    try:
                        if x['score'] < 0.5:
                            continue
                    except Exception as e:
                        continue

                    start = x['startIndex']
                    end = x['endIndex'] + 1

                    #提取结束 
                    word = y[start:end]
                    #print(word)
                    try:
                        if x['type'] == u'默认值':
                            if word != u'无':
                                if z['type'] == "integer":
                                    z['default'] = int(word)
                                elif z['type'] == "boolean":
                                    if word.lower() == 'true':
                                        z['default'] = True
                                    else:
                                        z['default'] = False
                                else:
                                    z['default'] = word
                        if x['type'] == u'可选值':
                            enums = []
                            if "enum" in z.keys():
                                enums = z['enum']
                            if z['type'] == "integer":
                                enums.append(int(word))
                            elif z['type'] == "boolean":
                                if word.lower() == 'true':
                                    enums.append(True)
                                else:
                                    enums.append(False)
                            else:
                                enums.append(word)
                            z['enum'] = enums
                        
                        if x['type'] == u'最大值':
                            if(z['type'] == 'string'):
                                z['maxLength'] = int(word)
                            elif ('.N' in z['name'] or '.n' in z['name']):
                                z['maxItems'] = int(word)
                            else :
                                z['maximum'] = int(word)
                        if x['type'] == u'最小值':
                            if(z['type'] == 'string'):
                                z['minLength'] = int(word)
                            elif ('.N' in z['name'] or '.n' in z['name']):
                                z['minItems'] = int(word)
                            else :
                                z['minimum'] = int(word)
                    except:
                        pass
    return z
def init():
    summary = {}

    inputfilename = "summary.html"
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

    pattern = re.compile("<td>(.*?)</td>")
    li = pattern.findall(html)
    for i in range(0, len(li)):
        if i % 2 != 0:
            continue
        pattern = re.compile(">(.+?)<")
        #print(li[i])
        l = pattern.findall(li[i])
        apiname = l[0]
        apisum = li[i+1]
        summary[apiname] = apisum
    return summary 
def initer():
    inputfilename = "publicer.html"
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
    err = {}
    er = {}
    err = gete(html, er)
    return err
def getmd(html):
    er = []
    
    pattern = re.compile("<td.*?>(.*?)</td>")
    li = pattern.findall(html)
    #print(len(li))
    for i in range(0, len(li)):
        if i % 4 != 0:
            continue
        er.append(li[i])

    inputfilename = "errdif.txt"
    html = ""
    inputfile = codecs.open(inputfilename, "r", 'utf-8')
    
    erd = []
    line = inputfile.readline()
    while 1:
        line = inputfile.readline()
        if not line:
            break
        line = line.replace("\n", "")
        line = line.replace("\r", "")
        line = line.replace(" ", "")
        if len(line) > 0:
            erd.append(line)
    inputfile.close()
    
    text = "### 阿里文档与项目文档差别\n\n错误码表中差异见下表，其他部分一致\n\n|阿里文档|项目文档|\n|:-:|:-:|\n"
    #print(erd)
    for x in er:
        text = text + "|" + x + '|'
        if x in erd:
            text = text + x
            erd.remove(x)
        text = text + '|\n'
    for x in erd:
        text = text + "||" + x + '|\n'
    return text

def work(html, err, summary):
    global apitype
    
    pattern = re.compile("<h1>(.+?)</h1>")
    hli = pattern.findall(html)
    apiname = hli[0]
    inputfile = codecs.open("sample.yaml", "r", "utf8")
    data = yaml.load(inputfile)
    dpath = data['paths']
    
    pattern = re.compile("(<h2.+?)<h2")        #获取第一块
    hli = pattern.findall(html)
    apidescribe = hli[0]
    
    index = html.find("<h2")                   #去除第一块标志
    html = html[index+3:]
    
    pattern = re.compile("<h2(.+?)<h2")        #获取第二块
    hli = pattern.findall(html)
    hreq = hli[0]
    #outtemp.write(hreq)
    requestp = getp(hreq, 4, 2, 'query')
    requestpn = []
    for x in requestp:
        requestpn.append(getsentence(x))

    index = html.find("<h2")                   #去除第二块标志
    html = html[index+3:]
    
    
    pattern = re.compile("<h2(.+?)<h2")        #获取第三块
    hli = pattern.findall(html)
    #print(summary)
    
    if u'权限' in hli[0]:
        dpath['/sample']['x-access'] = []
        pattern = re.compile("<h4(.*?)</blockquote>")
        ha = pattern.findall(html)
        for ac in ha:
            pattern = re.compile(">(.*?)</h4>")
            ha = pattern.findall(ac)
            name = ha[0]
            pattern = re.compile("<p>(.*?)</p>")
            hd = pattern.findall(ac)
            des = hd[0]
            dpath['/sample']['x-access'].append({'key': name, 'value': des})

        index = html.find("<h2")                   #去除本块标志
        html = html[index+3:]

    pattern = re.compile("<h2(.+?)<h2")
    hli = pattern.findall(html)
    hres = hli[0]
    
    responsep = getp(hres, 3, 1, '')
    
    index = html.find("<h2")                   #去除第三块标志
    html = html[index+3:]
                                               #获取第四块  
    
    pattern = re.compile("<h2(.+?)<h2")
    ht = pattern.findall(html)
    if len(ht) > 0 and u'权限' in ht[0]:
        dpath['/sample']['x-access'] = []
        pattern = re.compile("<h4(.*?)</blockquote>")
        ha = pattern.findall(html)
        for ac in ha:
            pattern = re.compile(">(.*?)</h4>")
            ha = pattern.findall(ac)
            name = ha[0]
            pattern = re.compile("<p>(.*?)</p>")
            hd = pattern.findall(ac)
            des = hd[0]
            dpath['/sample']['x-access'].append({'key': name, 'value': des})

        index = html.find("<h2")                   #去除本块标志
        html = html[index+3:]
                                               #获取第五块
    
    pattern = re.compile("<h2(.+?)<h2")
    ht = pattern.findall(html)
    herr = ""
    if(len(ht)>0):
        herr = ht[0]
    errorcode = gete(herr, err)
    mdtext = getmd(herr)

    pattern = re.compile("<pre.+?</pre>")
    hex = pattern.findall(html)

    

    dpath['/sample']['get']['description'] = apidescribe
    dpath['/sample']['get']['parameters'] = requestpn
    dpath['/sample']['get']['responses'][200]['schema']['properties'] = responsep

    for x in errorcode:
        dpath['/sample']['get']['responses'][x] = errorcode[x]
    try:
        e0 = hex[0]
        ex1in = {'description' : e0, 'id' : 1}
        dpath['/sample']['x-requestsample'] = []
        dpath['/sample']['x-requestsample'].append(ex1in)

        pattern = re.compile("<p>(.+?)</pre>")
        hfor = pattern.findall(html)

        e1 = hex[1]
        ex1out = {}
        if 'XML' in hfor[0]:
            ex1out = {'description' : e1, 'id' : 1, 'note' : u'XML格式'}
        else:
            ex1out = {'description' : e1, 'id' : 1, 'note' : u'JSON格式'}
        dpath['/sample']['x-responsesample'] = []
        dpath['/sample']['x-responsesample'].append(ex1out)
        try:
            e2 = hex[2]
            ex2out = {'description' : e2, 'id' : 2, 'note' : u'JSON格式'}
            dpath['/sample']['x-responsesample'].append(ex2out)
            ex2in = {'description' : e0, 'id' : 2}
            dpath['/sample']['x-requestsample'].append(ex2in)
        except:
            pass
    except:
        pass
    pars = dpath['/sample']['get']['parameters']
    for x in pars:
        if x['name'] == 'Action':
            apiname = x['enum'][0]
    if apiname in summary:
        dpath['/sample']['summary'] = summary[apiname]
    else:
        dpath['/sample']['summary'] = ''
        print(apiname)
    dpath['/' + apiname] = dpath['/sample']
    dpath.pop('/sample')
    data['paths'] = dpath

    outputdir = "../"+apitype
    try:
        os.makedirs(outputdir)
    except:
        pass
    outputpath = outputdir+"/"+apiname
    try:
        os.makedirs(outputpath)
    except:
        pass
    outputname = outputpath + "/" + apiname + '.yaml'
    outputmdname = outputpath + "/" + apiname + '.md'
    outputfile = codecs.open(outputname, "w", 'utf-8')
    #outputmdfile = codecs.open(outputmdname, "w", 'utf-8')
    yaml.dump(data, default_flow_style=False,stream=outputfile,indent=4,encoding='utf-8',allow_unicode=True, width=1000)
    #outputmdfile.write(mdtext)

if __name__ == "__main__":
    summary = init()
    err = initer()

    inputfilename = "1.html"
    html = ""
    inputfile = codecs.open(inputfilename, "r", 'utf-8')
    output = "temp.html"
    outtemp = codecs.open(output, "w", "utf-8")

    apidoc = {}
    ty = "z"
    while 1:
        line = inputfile.readline()
        if not line:
            break
        line = line.replace("\n", "")
        line = line.replace("\r", "")
        if mode == 2 or mode == 3:
            html += line
        
        if mode == 1:
            if "javascript" in line:
                pattern = re.compile("title=\"(.*?)\"")
                li = pattern.findall(line)
                ty = li[0]
                print(ty)
                apidoc[ty] = []
            if "document_detail" in line:
                pattern = re.compile("href=\"(.*?)\"")
                li = pattern.findall(line)
                tl = "https://help.aliyun.com"+li[0]
                #print(ty)
                apidoc[ty].append(tl)
            
    inputfile.close()

    if mode == 2:
        par = getp(html, 3, 1, "")
    
    if mode == 3:
        pattern = re.compile("<div class=\"help-body-box-detail-title\">.*?<!-- 评论 -->")
        li = pattern.findall(html)
        html = li[0]
        work(html, err, summary)    
    
    #'''
    if mode == 1:
        for typ in apidoc:
            apitype = typ
            for x in apidoc[typ]:
                if True:
                    print("work "+x)
                    request = urllib.request.Request(x)
                    response = urllib.request.urlopen(request)   
                    html = response.read().decode('utf-8')
                    html = html.replace("\n", "")
                    html = html.replace("\r", "")
                    pattern = re.compile("<div class=\"help-body-box-detail-title\">.*?<!-- 评论 -->")
                    li = pattern.findall(html)
                    html = li[0]
                    work(html, err, summary)
            '''
            except:
                outtemp.write(x)
                print("error "+x)
            '''
    #'''