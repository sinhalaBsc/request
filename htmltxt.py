import requests
import time
import re
#import rq


htmltxt='''
<div>

    <div> name
        <div> samadhi </div>
    </div>

    <div> age
        <div>28 </div>
    </div>

</div>
'''

print(htmltxt)

als=re.compile(r'<div|</div>')

matches=als.finditer(htmltxt)


anav=[]
var=[]
for m in matches:
    print(m.group(0))
    if m.group(0)=='<div':
        var.append(1)
    else:
        var.append(-1)
    anav.append(m.span()[0])

print(anav)
print(var)


'''
[92,1, 12, 31, 74, 92,1]
[45, 58, 100, 111, 123]

[1, 12, 31, 74, 92]
[45, 58, 100, 111, 123]
[[1,123], [12,58], [31,45], [74,111], [92,100]]
[1, 12, 31, 45, 58, 74, 92, 100, 111, 123]
[1, 1,  1,  -1, -1,  1,  1,  -1,  -1,  -1]
[[1, 123], [12, 58], [31, 45], [45, 92], [58, 74], [74, 111], [92, 100]]
'''
print('*************************************')
s=0
closePoint=0
tag=[]
for s in range(len(var)):
    closePoint=0
    if not var[s]>0:
        continue     # no point to close a close brackets
    for i in range(s,len(var)):
        print(var[i])
        if var[i]>0:
            closePoint+=1
        else:
            closePoint-=1
        print('closePoint value ',closePoint)
        if not closePoint:
            print('close ',anav[s],' ',anav[i])
            tag.append([anav[s],anav[i]])
            break

print(tag)
