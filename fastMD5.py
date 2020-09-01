import requests
from bs4 import BeautifulSoup
import hashlib

url = 'http://docker.hackthebox.eu:30789/'
r=requests.session()
reqs = r.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
for heading in soup.find_all(["h3"]):
    hashStr = hashlib.md5(heading.text.strip().encode('utf-8')).hexdigest()
print(hashStr)
postobj = {'hash':hashStr}

x = requests.post(url,data=postobj)
print(x.text)