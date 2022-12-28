from tkinter.filedialog import *
from pdf2docx import Converter

getFile = askopenfilename()

cv = Converter(getFile)
cv.convert("sample.docx")

cv.close()