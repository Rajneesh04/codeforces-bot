#! python3

import requests, sys, bs4, os
print('May the Force be with you')

def rem(s):
    n=len(s)
    n-=2
    for i in range(n):
        if(s[i:i+3]=="$$$"):
            s=s[:i]+s[i+3:]
    return s

def prob(contest, problem):
    url = contest+"/problem/"+problem
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    linkElems = soup.select('div[class="problem-statement"]')
    par = linkElems[0]
    pars = par.findAll('p')
    cfFile = open(problem+'.txt', 'w')
    cfFile.write("\n"+problem+"\n\n")
    for x in pars:
        s=x.text
        s=rem(s)
        n = len(s)
        n = int(n/100)
        for i in range(n):
            s=s[:100*(i+1)]+"\n"+s[100*(i+1):]
        cfFile.write(s)
        cfFile.write('\n')

    inp = par.select('div[class="input"]')
    cfFile.write(inp[0].text)

    out = par.select('div[class="output"]')
    cfFile.write(out[0].text)
    cfFile.close()


res = requests.get(''.join(sys.argv[1:]))
url = ''.join(sys.argv[1:])
folder = url[-4:]
curr_dir = os.getcwd()
final_dir = os.path.join(curr_dir,folder)
if not os.path.exists(final_dir):
    os.makedirs(final_dir)
os.chdir(final_dir)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features="html.parser")

linkElems = soup.select('div[class="datatable"]')
links = linkElems[0].findAll('a')
tempc = ''
for link in links:
    s = link.get('href')
    c = s[-1]
    if(tempc != c):
        prob(''.join(sys.argv[1:]),c)
    tempc = c
