import random
import string

def acronym(y=3):
    return ''.join(random.choice(string.ascii_uppercase) for x in range(y))
print()
randAcronym = (acronym(3))
print("Looking for " + randAcronym + " manual ...")
print()

exec(open("seekerActual.py").read())

pdfName = pdfGrab()
print("Searching ... ")
print()
print("Search complete @ "+tStamp)
print()
print("index check, list contents :")
print(pdfName)

if not pdfName:
    print("empty, re-run ...")
    pdfGrab()

import requests
PDFurl = pdfGrab()[0]
r = requests.get(PDFurl, allow_redirects=True)
print(r)

print("- - - ")
# requests.get(PDFurl, headers = {'User-agent': 'your bot 0.1'}) # use above when config'd 442 err
print(">>"+PDFurl)
print("\n")

import io
for i in range(1):
    with io.open("/Users/tomweston/PycharmProjects/HEC/z_img_thePDF/thePDF_" + str(i) + ".pdf", 'w', encoding='utf-8') as f:
        f = open("/Users/tomweston/PycharmProjects/HEC/z_img_thePDF/thePDF_"+str(i)+".pdf","w")

open("/Users/tomweston/PycharmProjects/HEC/z_img_thePDF/thePDF_"+str(i)+".pdf", "wb").write(r.content)
"/Users/tomweston/PycharmProjects/HEC/z_img_thePDF/thePDF_%s.pdf" % i
"/Users/tomweston/PycharmProjects/HEC/z_img_thePDF/thePDF_{}.pdf".format(i)