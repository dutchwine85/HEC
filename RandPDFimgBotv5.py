# rPiB ---->

# FLUSH OLD imgs_dir :
import shutil
shutil.rmtree("/Users/tomweston/PycharmProjects/HEC/z_img_output/")
# BUILD NEW imgs_dir :
from pathlib import Path
Path("/Users/tomweston/PycharmProjects/HEC/z_img_output").mkdir(parents=True, exist_ok=True)
# FLUSH OLD chosen_dir :
import shutil
shutil.rmtree("/Users/tomweston/PycharmProjects/HEC/z_img_chosen/")
# BUILD NEW chosen_dir :
from pathlib import Path
Path("/Users/tomweston/PycharmProjects/HEC/z_img_chosen").mkdir(parents=True, exist_ok=True)

import random
import string

def acronym(y=3):
    return ''.join(random.choice(string.ascii_uppercase) for x in range(y))
print()
randAcronym = (acronym(3))
print("Looking for " + randAcronym + " manual ...")
print()

#SEARCH POINT
from googlesearch import search
def pdfGrab():
    return search("filetype:pdf manual"+randAcronym, num_results=0)
print()
pdfName = pdfGrab()

import requests
PDFurl = pdfGrab()[0]
r = requests.get(PDFurl, allow_redirects=True)
print(PDFurl)
print("\n")
#if list empty pdfGrab[] then loop back to SEARCH POINT

import io
for i in range(1):
    with io.open("/Users/tomweston/PycharmProjects/HEC/z_img_thePDF/thePDF_" + str(i) + ".pdf", 'w', encoding='utf-8') as f:
        f = open("/Users/tomweston/PycharmProjects/HEC/z_img_thePDF/thePDF_"+str(i)+".pdf","w")

open("/Users/tomweston/PycharmProjects/HEC/z_img_thePDF/thePDF_"+str(i)+".pdf", "wb").write(r.content)
"/Users/tomweston/PycharmProjects/HEC/z_img_thePDF/thePDF_%s.pdf" % i
"/Users/tomweston/PycharmProjects/HEC/z_img_thePDF/thePDF_{}.pdf".format(i)

import fitz
from PIL import Image
import os
import fnmatch

file = "/Users/tomweston/PycharmProjects/HEC/z_img_thePDF/thePDF_0.pdf"

pdf_file = fitz.open(file)

for page_index in range(len(pdf_file)):

    page = pdf_file[page_index]
    image_list = page.getImageList()

    if image_list:
        print(f"PAGE",page_index,"contains", [len(image_list)],"images")
    else:
        print("PAGE",page_index,"is EMPTY")
    for image_index, img in enumerate(page.getImageList(),start=1):

        xref = img[0]

        base_image = pdf_file.extractImage(xref)
        image_bytes = base_image["image"]

        image_ext = base_image["ext"]
        image = Image.open(io.BytesIO(image_bytes))
        image.save(open(f"/Users/tomweston/PycharmProjects/HEC/z_img_output/pic{page_index+1}_{image_index}.{image_ext}","wb"))

#if fitz error then loop back to SEARCH POINT
##########
def chosen():
    return random.choice(os.listdir(r"/Users/tomweston/PycharmProjects/HEC/z_img_output"))

def size(fn):
    return os.path.getsize(r"/Users/tomweston/PycharmProjects/HEC/z_img_output/"+fn)
##########
print("\n")
i=1
threshold = 6000
while True:
    z_file = chosen()
    file_size = size(z_file)
    if file_size < threshold:
        print(z_file + " is too small")
    else:
        break
print(z_file + " is at least 6KB")

z_file

src_path = r"/Users/tomweston/PycharmProjects/HEC/z_img_output/"+z_file
dst_path = r"/Users/tomweston/PycharmProjects/HEC/z_img_chosen"
shutil.move(src_path, dst_path)
print(z_file," is ready to tweet!")

import os
head, tail = os.path.split(str(pdfName))
docName = tail
print()
print("---> "+docName[:-6]+" <---")
print()

########################################
# twitter ---->
import tweepy

API_key = "pwIYlJhhW89yuNDKHFfefIPDG"
API_secret = "AwkpCFOaWpW6cSRG7MLywAupsHNi0s7H8mUT6PMUIIez8nDmP2"
Access_token = "1462802761783947271-u1Z0JFo8e1db7DAsk0vEXNAwmc51YA"
Access_token_secret = "Q1OU6aDOgB9NgaW4A02jJy0Ns5qEbCKA1KkHKTvzylDME"

callback_uri = "oob"

auth = tweepy.OAuthHandler(API_key, API_secret, callback_uri)
auth.set_access_token(Access_token, Access_token_secret)

redirect_url = auth.get_authorization_url()
print(redirect_url)

userPIN = input("Add PIN -> ")
print("\n")
auth.get_access_token(userPIN)

API = tweepy.API(auth)
print(z_file)
print(docName)

upload = API.media_upload(filename=r"/Users/tomweston/PycharmProjects/HEC/z_img_chosen/"+z_file)
print()
print("File stats : " + (str(upload)))
print(upload.media_id_string) #<<< mID
mID = [upload.media_id_string]
API.update_status(media_ids=mID, status=docName[:-6])

print()
print("Post complete")
