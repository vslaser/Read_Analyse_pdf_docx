import pandas as pd
import numpy as np 
import os

def read_file(filepath):
    ext = os.path.splitext(filepath)[1]
    data = None
    

    if ext == ".xlsx":
        print("excel file reading into dataframe...")
        data = pd.read_excel(filepath)
        print("file read. File type: ", type(data))
    elif ext == ".csv":
        print("csv file reading into dataframe...")
        data = pd.read_csv(filepath)
        print("file read. File type: ", type(data))
    elif ext == ".pdf":
        print("pdf file reading. This will take a few minutes...")
        import PyPDF2 
        pdfFileObj = open(filepath,'rb')     #'rb' for read binary mode
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pdfReader.numPages
        pdffile = '' # This creates an empty string object to which the text from the pdf file will be added
        for i in range(0,pdfReader.numPages): # iterating page by page to read text
            pageObj = pdfReader.getPage(i)          
            pdffile = pdffile + pageObj.extractText()
        data = pdffile
        print("file read. File type: ", type(data))
    elif ext == ".docx":
        import dox

        doc = docx.Document(filepath)
        fullText = []
        for para in doc.paragraphs:
            txt = para.text.encode("ascii", "ignore")
            fullText.append(txt)
        data = fullText
        print("file read. File type: ", type(data))
    elif ext == ".xls":
        print("reading an old excel file into dataframe.")
        import xlrd
        wb = xlrd.open_workbook(filepath)
        sheet_names = wb.sheet_names()
        sheet = wb.sheet_by_name(sheet_names[0])
        d = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
        data = pd.DataFrame(d)
        print("file read. File type: ", type(data))
    else:
        print("Dont Recognise the file format. I only read xls, xlsx, csv, pdf and docx files", ext)
    return data


