
import re

txt='''
<td class="td">samadhi</td>
<td class="td">අනිසි ලෙස යෙදීම</td>
<td class="td">අනිසි ලෙස යොදනවා</td>
<td class="td">අනිසිපාවිච්චිය</td>
<td class="td">අපයෙදුම</td>

'''
className='td'
als=re.compile(r'>.+<')
matches=als.finditer(txt)

for m in matches:
    startPoint=m.span()[0]
    endPoint=m.span()[1]
    #print(m.group(0))
    print(txt[startPoint+1:endPoint-1])
