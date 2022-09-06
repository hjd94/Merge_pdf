from PyPDF2 import PdfFileMerger, PdfFileReader
from os.path import isfile, join
from PIL import Image

mypath = r'C:\Users\JakeIreland\OneDrive - PublicVoice\Desktop\Projects\bio-mms'
mysupportingdocs = join(mypath, r'exports\boimms all submissions 14 6 2021\interface_exported\supporting documentation')
# Call the PdfFileMerger
mergedObject = PdfFileMerger()
Â 
# read directory
supporting_docs = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for doc in supporting_docs:
    f = ''
    if fileisimage:
        im = Image.open(doc)
        im = im.convert('RGB')
        newf = join('tmp', filename_without_extension)
        im.save(newf)
        f = newf

    mergedObject.append(PdfFileReader(f, 'rb'))


# Write all the files into a file which is named as shown below
mergedObject.write("mergedfilesoutput.pdf")
