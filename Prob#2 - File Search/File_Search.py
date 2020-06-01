import json
all_path = []
pdic = {}
res = []
def explore(dic, parent,depth):
    if isinstance(dic,str):
        if dic in pdic:
            pdic[dic].append([depth+1,parent+'/'+dic])
        else:
            pdic[dic] = [[depth+1,parent+'/'+dic]]
        "print(parent+'/'+dic)"
        return
    for k,v in dic.items():
        if '{}/{}'.format(parent,k) not in all_path:
            all_path.append('{}/{}'.format(parent,k))
        if isinstance(v,dict):
            explore(v,parent+'/'+str(k),depth+1)
        if isinstance(v,list):
            for x in v:
                "explore(x,parent+'/'+str(k))"
                explore(x,parent,depth+1)
        else:
            pass
def fileSearch(fileToSearch,filesObj):
    with open(filesObj+'.json') as f:
        data = json.load(f)
    explore(data,'',-1)
    dop = pdic[fileToSearch]
    dop.sort()
    for depth,path in dop:
        res.append(path)
    print(res)
fileToSearch,filesObj = input().split()
fileSearch(fileToSearch,filesObj)
'''
file1 test2
'''