import bs4            
import requests
import re
import sys

# url = input('Enter url - ' )
print("This script downloads hyper-linked files from a given URL.")

# Input: URL to parse & type of file formats for downloading from a URL 
url=input("Enter URL with downloadable files- ")
fileformat = input("Enter file formats-(e.g.: .pdf)")

# Get hyperlinks 
html = requests.get(url)
soup = bs4.BeautifulSoup(html.text, "html.parser")

# Download! 
for link in soup.find_all('a', href=True):
    href = link['href']

    if any(href.endswith(x) for x in [fileformat]):
        print("Downloading '{}'".format(href))
        remote_file = requests.get(url + href)

        with open(href, 'wb') as f:
            for chunk in remote_file.iter_content(chunk_size=1024): 
                if chunk: 
                    f.write(chunk)       