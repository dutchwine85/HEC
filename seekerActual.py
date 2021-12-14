from googlesearch import search
def pdfGrab():
    return search("filetype:pdf manual"+randAcronym, num_results=0)

pdfGrab()