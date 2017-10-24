import requests
import re
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

# regular expression to retrieve url from html tags
regPat = '.{,}.pdf.{,}'
res = requests.get('http://talktomeinkorean.com/curriculum/')
soup = BeautifulSoup(res.text, "lxml")

# save urls into articles list
articles = []
divs = soup.find_all('a')
for link in divs:
	strlink = str(link.get('href'))
	pat = re.compile(regPat, re.UNICODE)
	text = re.findall(pat, strlink)
	if not text:
		continue
	text = ''.join(text)
	articles.append(text)

# download pdf with urlretrieve
download_path = './TTMK'
for item in articles:
	url = item
	filename = 'ttmk' + str(articles.index(item)) + '.pdf'
	fullfilename = os.path.join(download_path, filename)
	urlretrieve(url, fullfilename)
	print(filename + ' downloaded!')