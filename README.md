# Lord of the Rings LCG : making A4 pdfs for sets of playing cards

Code to generate A4 pdfs filled with playing cards belonging to a specific set.
Made to have backups of cards and sets.
Do not use to print as copying a set you do not have. Look for copyright issues before.

## Usage:

On file *get_images_set_py*, substitute the line:
set = "XXXXXXX" for the set you want to generate the card images. Example:
set = "The-Hunt-for-Gollum"

Once this is done, run *get_images_set.py*

On file cards_to_pds substitute the line beginning with
folder = "XXXXXXXXX"
with the set you want to generate. Example:
folder = "The-Hunt-for-Gollum"

Once this is done, run *cards_to_pdf.py*

This will generate a pdf file named as the set you are making, that contains the cards for that set. A4 format, 9 cards per sheet.

Use http://hallofbeorn.com/LotR/Products to find the names of the set you want to generate. Copy the exact path-name.  
Example: Clicking on the "Lost Realm Expansion" on http://hallofbeorn.com/LotR/Products you are directed to:  
http://hallofbeorn.com/LotR/Products/The-Lost-Realm?View=Browse
Copy then "The-Lost-Realm" as the set and folder as indicated above.  