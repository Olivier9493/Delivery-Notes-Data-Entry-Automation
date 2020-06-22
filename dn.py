import os
import sys


# Global data
pdf_list = []
path = "./data"

def getfiles(pdf_list, path):
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(".pdf"):
                pdf_list.append(filepath)
    return pdf_list

if __name__ == '__main__':
    print(getfiles(pdf_list, path))

