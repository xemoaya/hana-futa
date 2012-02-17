from itertools import permutations
from itertools import combinations
import json
#fin=file('t2')
#line = fin.readline()
#cou=[]
#while line:
#    cou.append(line.strip() )
#    line = fin.readline()
#print '"'+','.join(cou) + '",'
#for com in combinations(cou, 4) :
#    print '"' + ','.join(com) + '",'
#for com in combinations(cou, 3) :
#    print '"' + ','.join(com) + '",'
#

#fin = file("card.cfg")
#line = fin.readline() 
#res = [{}]
#name = ''
#cnt = 0
#while line :
#    if line.startswith('[') or line.startswith('{') or not line.strip() :
#        pass
#    if line.startswith('\"pic') :
#        cnt += 1
#        res[-1][name][-1]['pic'] = '%s%d.jpg' % (name, cnt)
#        if cnt == 4 :
#            res.append({})
#            cnt = 0
#    elif line.startswith('\"name') :
#        res[-1][name].append({'name' : line.strip()[8:-1] })
#
#    elif line.startswith('"') and line.strip().endswith('"') :
#        name = line.strip()[1:-1]
#        res[-1] = {name : []} 
#
#    line = fin.readline()
#print res
#json.dump(res, file('cart','w'))
#fin.close()

res = []
dt = json.load(file('card.json'))
for sec in dt :
    res.append({})
    for mon in sec :
        res[-1]['name'] = mon
        res[-1]['cards'] = []
        arr = sec[mon]
        for card in arr:
            vec = card['name'].split(',')
            name = card['pic'][:-4]
            res[-1]['cards'].append({'id':name, 'pic_name':card['pic'], 'type':vec})
json.dump(res, file('card','w') )
