from PyPDF2 import PdfFileMerger, PdfFileReader
from os.path import isfile, join
from PIL import Image

mypath = r''

# Call the PdfFileMerger
merging_object = PyPDF2.PdfFileMerger()

# read contents of folds
supporting_docs = [file for file in listdir(mypath) if file.endswith(".pdf")]
for doc in supporting_docs:
    merging_object.append(PdfFileReader(doc, 'rb'))
# Write all the files into a file which is named as shown below
merging_object.write("mergedfilesoutput.pdf")
