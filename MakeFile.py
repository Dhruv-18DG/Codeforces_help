import os
import requests
num = '1888'
alpha = 'D1'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
link = f"https://codeforces.com/problemset/problem/{num}/{alpha}"
r = requests.get(link, headers=headers)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
divs = soup.find("div", class_="input")
# for div in divs:
pres = divs.find('pre')
divss = pres.find_all('div')
# print(divss)
s = []
# for d in divss:
#     print(d.get_text())
if(len(divss)==0):
    s.append(pres.get_text())
else:
    for d in divss:
        s.append(d.get_text())

divs = soup.find("div", class_="output")
# for div in divs:
pres = divs.find('pre')
divss = pres.find_all('div')
# print(divss)
otp = []
# for d in divss:
#     print(d.get_text())
if(len(divss)==0):
    otp.append(pres.get_text())
else:
    for d in divss:
        otp.append(d.get_text())

# print(s)
# print(otp)

with open(f'{num}{alpha}.cpp', 'w') as fp:
    str = f'''#include<bits/stdc++.h>
using namespace std;
#define int long long int

signed main()'''
    fp.write(f"/* \n")
    fp.write("sample input \n")
    # fp.writelines(s)
    for line in s:
        fp.write(line)
        fp.write('\n')

    fp.write("Sample Output\n")
    for line in otp:
        fp.write(line)
        fp.write('\n')
    fp.write("*/ \n")
    fp.write(str)
    
    fp.close()
