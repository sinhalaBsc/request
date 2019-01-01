# make tag

import re


txt='''
samadhi laksahan
class="sama"
pasindu piyasiri rathnayaka

'''
classname='sam'
als=re.compile(r'class=[\'"]'+classname+'[\'"]')
matches=als.finditer(txt)

if matches:
    print('match')

for m in matches:
    print(m)


# job successful 

