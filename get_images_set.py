## get images from website.
## crawls 2 levels and get images links.

from bs4 import BeautifulSoup
import urllib.request
import re
import requests
from os import mkdir, path
from io import BytesIO
from PIL import Image

#set = "The-Dark-of-Mirkwood"
#set = "The-Hunt-for-Gollum"
#set = "Conflict-at-the-Carrock"
#set = "A-Journey-to-Rhosgobel"
#set = "The-Hills-of-Emyn-Muil"
set = "The-Hobbit-Over-Hill-and-Under-Hill"
#set  = "The-Hobbit-On-the-Doorstep"

base_url = "http://hallofbeorn.com/LotR/Products/"
root_url = "http://hallofbeorn.com/"
detail_base_url = "http://hallofbeorn.com/LotR/Details/"
folder = "cards"
#print("Enter the link \n")
#link = input()

# create directory:
# working directoy should be the one of this file...
dir_ = path.join("cards", set)
mkdir(dir_)
print("Directory '% s' created" % set)


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

    images = [im['src'] for im in soup.find_all('img',class_='card-image')]
    ln = len(images)
    if ln > 1:
        print("detected more than one image: ", ln)

    for image in images:
        file_name = image.split('/')[-1]
        r = requests.get(image)
        # find width and height ::
        img = Image.open(BytesIO(r.content))
        width, height = img.size
        ratio = height / width
        if ratio >= 1:
            quest = False
        else:
            quest = True
        
        if nrep == 1:
            fn = path.join(dir_, set + "---" + file_name)
            if quest:
                print("Quest detected: changing name ")
                filename_ = file_name.replace(".jpg", "") + "-QUEST.jpg"
                fn = path.join(dir_, set + "---" + filename_)

            with open(fn,'wb') as f:
                f.write(r.content)
            print(file_name)
            f.close()
            
        if nrep > 1:
            for num in range(nrep):
                file_name2 = set + "---" + file_name.replace(".jpg", "") + "-" + str(num) + ".jpg"
                if quest:
                    file_name2 = set + "---" + file_name.replace(".jpg", "") + "-" + str(num) + "-QUEST.jpg"
                    
                fn = path.join(dir_,file_name2)
                with open(fn,'wb') as f:
                    f.write(r.content)
                print(file_name)
                f.close()
    
