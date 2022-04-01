import os
import requests
from bs4 import BeautifulSoup



url = "https://web.stanford.edu/class/cs237b/"
res = requests.get(url)
html = res.content
soup = BeautifulSoup(html, "html.parser")


soup.prettify()
arr = soup.find_all('a')
download_url_lst = []
for e in arr:
    t = e['href']
    if t[-4:] == '.pdf':
        uri = url + t
        name = uri.split('/')[-1]
        print(uri)
        os.system("powershell wget " + uri + " -OutFile" + ' ' + name)


