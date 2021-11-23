
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

from googlesearch import search
pdfGrab = search("filetype:pdf manual"+randAcronym, num_results=0)
print (pdfGrab)

import requests
PDFurl = pdfGrab[0]
r = requests.get(PDFurl, allow_redirects=True)
print()

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

chosen=random.choice(os.listdir("/Users/tomweston/PycharmProjects/HEC/z_img_output"))
print("\n")
print("Publish - ", chosen)

import shutil

src_path = r"/Users/tomweston/PycharmProjects/HEC/z_img_output/"+chosen
dst_path = r"/Users/tomweston/PycharmProjects/HEC/z_img_chosen"
shutil.move(src_path, dst_path)

