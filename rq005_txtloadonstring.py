
import re

txt='''
&nbsp;
&nbsp;
Law.
අක්‍රොශ කරනවා
n.
අනිසි ලෙස යෙදීම
vt.
අනිසි ලෙස යොදනවා
Soc.
අනිසිපාවිච්චිය
Law.
අපයෙදුම
n.
අපවාදය
Soc.
අයථාභාවිතය
v.
අයුතු ප්‍රයෝජන ගන්නවා
n.
අයුතු ප්‍රයෝජනය
Law.
ආක්‍රොශය
n.
ආක්‍රෝශය
Aes.
දුෂ්ප්‍රයුක්ත කිරීම
Aes.
දුෂ්ප්‍රයුක්තිය
vt.
දූෂ්‍ය කරනවා
n.
නින්දාව
v.
පරිභව කරනවා
n.
පරිභවය
vt.
බනිනවා
v.
බැණ දොඩවනවා
Law.
බැණ වැදෙනවා
n.
බැණුම
n.
බැනීම
n.
වහස
&nbsp;
&nbsp;

'''
className='td'
als=re.compile(r'n')
matches=als.finditer(txt)

for m in matches:
    print(m)
    #startPoint=m.span()[0]
    #endPoint=m.span()[1]
    #print(m.group(0))
    #print(txt[startPoint+1:endPoint-1])
