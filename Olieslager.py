import os
import sys
import csv
import math
import unicodedata
from pathlib import Path
from datetime import datetime, date, timedelta
from ics import Calendar, Event
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER, A4, landscape, portrait
from reportlab.lib.units import inch
from reportlab.lib.colors import blue, green, black, red, pink, gray, brown, purple, orange, yellow, white, lightgrey
from reportlab.pdfbase import pdfmetrics  
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

kamerdata = []

class Kamer:
    def __init__(self, nummer, pad, zijde, bewoner):
        self.nummer = nummer
        self.pad = pad
        self.zijde = zijde
        self.bewoner = bewoner

def processcsv(csvfile):
    with open(file_to_open, 'r') as file:
        csvreader = csv.reader(file, delimiter = ';')
        count = 0
        for row in csvreader:
            if count > 0:
                kamerdata.append(row)
            count += 1

if sys.platform[0] == 'l':
    path = '/home/jan/git/Olieslager'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Olieslager"
os.chdir(path)
kamers = []
file_to_open = "Data/Kamers.csv"
processcsv(file_to_open)
print(len(kamerdata))
for i in range(len(kamerdata)):
    nummer = kamerdata[i][0]
    pad = kamerdata[i][1]
    zijde = kamerdata[i][2]
    bewoner = kamerdata[i][3]
    kamers.append(Kamer(nummer, pad, zijde, bewoner))
for i in range(len(kamers)):
    print(kamers[i].bewoner)
    
d = Drawing(595, 842)
d.add(Rect(5, 5, 200, 100, fillColor = colors.yellow))
d.add(String(10, 10, 'Hello World', fontSize = 18, fillColor = colors.red))
renderPDF.drawToFile(d, 'PDF/olieslager.pdf')

pdfmetrics.registerFont(TTFont('Ubuntu', 'Ubuntu-Regular.ttf'))
pdfmetrics.registerFont(TTFont('UbuntuBold', 'Ubuntu-Bold.ttf'))
pdfmetrics.registerFont(TTFont('UbuntuItalic', 'Ubuntu-Italic.ttf'))
pdfmetrics.registerFont(TTFont('UbuntuBoldItalic', 'Ubuntu-BoldItalic.ttf'))
pdfmetrics.registerFont(TTFont('LiberationSerif', 'LiberationSerif-Regular.ttf'))
pdfmetrics.registerFont(TTFont('LiberationSerifBold', 'LiberationSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('LiberationSerifItalic', 'LiberationSerif-Italic.ttf'))
pdfmetrics.registerFont(TTFont('LiberationSerifBoldItalic', 'LiberationSerif-BoldItalic.ttf'))
key = input("Wait")
