## get images from website.
## crawls 2 levels and get images links.

from bs4 import BeautifulSoup
import urllib.request
import re
import requests


set = "The-Hunt-for-Gollum"
#set = "Conflict-at-the-Carrock"
#set = "A-Journey-to-Rhosgobel"
#set = "The-Hills-of-Emyn-Muil"
#set = "The-Hobbit-Over-Hill-and-Under-Hill"
#set  = "The-Hobbit-On-the-Doorstep"

base_url = "http://hallofbeorn.com/LotR/Products/"
root_url = "http://hallofbeorn.com/"
detail_base_url = "http://hallofbeorn.com/LotR/Details/"
folder = "cards"
#print("Enter the link \n")
#link = input()

link = base_url + set 
url = urllib.request.urlopen(link)
content = url.read()
soup = BeautifulSoup(content)
links = [a['href'] for a in soup.find_all('a',href=re.compile('/LotR/Details/*'))]
print (len(links))
#print (links)
print("\n".join(links))

details = []

for lk in links:
    hl = root_url + lk
    details.append(hl)

print("\n".join(details))

for card in details:
    print(card)
    url = urllib.request.urlopen(card)
    content = url.read()
    soup = BeautifulSoup(content)
    image = [im['src'] for im in soup.find_all('img',class_='card-image')][0]
    repeat = [span.text for span in soup.find_all('span', style="margin-left:8px;display:inline-block;" )][0]
    pattern = re.compile(r"\(x(\d)\)")
    pattern2 = re.compile(r"\(x(\d)/x\d\)")
    print(repeat)
    rep = pattern.findall(repeat)
    rep2 = pattern2.findall(repeat)
    #print(rep2)
    #print(len(rep2))
    nrep = 1
    if len(rep) == 1:
        nrep = int(rep[0])
    else:
        if len(rep2) == 1:
            nrep = int(rep2[0])        
    file_name = image.split('/')[-1]
    r = requests.get(image)
    if nrep == 1:
        with open(set + "---" + file_name,'wb') as f:
            f.write(r.content)
            print(file_name)
        f.close()
    if nrep > 1:
        for num in range(nrep):
            file_name2 = set + "---" + file_name.replace(".jpg", "") + "-" + str(num) + ".jpg"
            with open(file_name2,'wb') as f:
                f.write(r.content)
                print(file_name)
            f.close()
    
