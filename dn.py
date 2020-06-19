import os
import sys

def getfiles():
    pdf_list = []
    path = "./data"
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(".pdf"):
                pdf_list.append(filepath)
    return pdf_list

print(getfiles())

