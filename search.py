import re
import os
import codecs
from django.shortcuts import render_to_response, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt


fp = codecs.open("id.txt", "r", "utf-8")
ids = fp.read()
idsList = re.split("\n", ids)
idDictionary = {}
for i in range(0, len(idsList) - 2, 3):
    idDictionary[int(idsList[i])] = (idsList[i + 1], idsList[i + 2])
f = codecs.open("Dict.txt", "r")
content = f.read()
contentList = re.split("\n", content)
dictionary = {}
for i in range(0, len(contentList) - 1, 2):
    idList = re.split(" ", contentList[i + 1])
    if("" in idList):
        idList.remove("")
    dictionary[contentList[i]] = idList


@csrf_exempt
def findID(request):
    address = []
    tempSetList = []
    flag = False
    tempStr = request.POST.get('eat', "sdftewrewezxc").encode("utf-8")
    if(tempStr == "sdftewrewezxc"):
        tempStr = request.GET.get('search').encode('utf-8')
    templist = re.split(" ", tempStr)
    for i in range(0, len(templist)):
        templist[i] = templist[i].lower()
    if(len(templist) == 1 and not dictionary.has_key(templist[0])):
        templist[0] = templist[0].lower()
        for string in dictionary.keys():
            if(templist[0] in string):
                tempSet = set()
                for ids in dictionary[string]:
                    tempSet.add(ids)
                tempSetList.append(tempSet)
                flag = True
    else:
        for string in templist:
            string = string.lower()
            if(dictionary.has_key(string)):
                tempSet = set()
                for ids in dictionary[string]:
                    tempSet.add(ids)
                tempSetList.append(tempSet)
    totalSet = set()
    if(len(tempSetList) > 0):
        totalSet = tempSetList[0]
    if(flag):
        for tempSet in tempSetList:
            totalSet = totalSet | tempSet
    else:
        for tempSet in tempSetList:
            totalSet = totalSet & tempSet
    for ids in totalSet:
        tempSss = re.sub(" ", "_", idDictionary[int(ids)][0])
        tempSss = re.sub("\r", "", tempSss)
        if(not os.path.exists('%s%s%s' % ("hw/food/search/static/images/", tempSss, ".jpg"))):
            tempSss = "NoPic"
        address.append({"id": idDictionary[int(ids)][0], "url": re.sub(" ", "_", idDictionary[int(ids)][0]), "jpg": tempSss})
    page_address = Paginator(address, 8)
    page = request.GET.get('page')
    table = request.GET.get('table', 'none')
    try:
        if table == '1':
            pageofaddress = page_address.page(page)
        else:
            pageofaddress = page_address.page(1)
    except PageNotAnInteger:
        pageofaddress = page_address.page(1)
    except EmptyPage:
        pageofaddress = page_address.page(page_address.num_pages)
    return render_to_response('result.html', {'address': pageofaddress, 'postContent': tempStr}, context_instance=RequestContext(request))
