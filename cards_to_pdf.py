import os
from fpdf import FPDF
from math import ceil

#folder = "The-Hills-of-Emyn-Muil"
folder = "The-Hunt-for-Gollum"
#folder = "A-Journey-to-Rhosgobel"
#folder =  "The-Hobbit-Over-Hill-and-Under-Hill"
#folder = "The-Hobbit-On-the-Doorstep"

cardWidth = 63.5
cardHeight = 88.0
leftPadding = 4.0
spacer = 4.0

cards  = []

cards += [each for each in os.listdir(folder) if each.endswith('.jpg')]

images =  [each for each in cards if not each.__contains__("QUEST")]
quests =  [each for each in cards if each.__contains__("QUEST")]

# put quests at the end::
for quest in quests:
    images.append(quest)

ln = len(images)
idx = 0

pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
#pdf.add_page()

pages = int(ceil(ln/9.0))
print "pages: ", pages
page = 0
print_quests = 0

fi =  0
fj =  0

while idx < ln :
    if print_quests == 0:
        pdf.add_page()
    else:
        pdf.add_page("L")
    for i in range(3):
        #if idx == ln:
        #    break
        for j in range(3):
            if idx == ln:
                break
            quest = False
            img = folder + "/" + images[idx]
            if images[idx].__contains__("QUEST"):
                quest = True
                print "found Quest !!", i, j, idx
                if print_quests == 0:
                    pdf.add_page("L")
                    print_quests = 1
                    #fj = 0
                    #fi = 0
            if not quest:
                fi =  i
                fj =  j
                x = leftPadding+spacer*(fj+1)+cardWidth*fj
                y = spacer*(fi+1)+cardHeight*fi
                w = cardWidth
                h = cardHeight
            else:
                fi = i
                fj = j
                x = leftPadding+spacer*(fj+1)+cardHeight*fj
                y = spacer*(fi+1)+cardWidth*fi
                w = cardHeight
                h = cardWidth

            print "# ", idx 
            
            idx = idx + 1
            
            if idx <= ln:
                print(x,y,w,h)
                print(img)
                pdf.image(img, x, y, w, h)
                print "printed image: ", idx , "/ ", ln 
                print "----"
               
    page += 1
            
    print "printed page: ", page , "of " , pages

pdf.output(folder + '.pdf', 'F')
            
