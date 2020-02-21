#!/usr/bin/env python

"""
    Script fills a base PDF with 20 pictures at the right locations
    Reusability small

    features:
        read, change and save a PDF with PyPDF2
        The Image module of the PIL library to work with pictures

"""

from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from PIL import Image
from random import choice
import subprocess
import numpy as np
import io

MAX_PICTURE_HEIGHT_LEFT  = 64
MAX_PICTURE_WIDTH_LEFT   = 142
MOST_LEFT = 35 #if picture has maximum dim in x
RATIO_LEFT = MAX_PICTURE_WIDTH_LEFT / MAX_PICTURE_HEIGHT_LEFT
MAX_PICTURE_HEIGHT_RIGHT = 74
MAX_PICTURE_WIDTH_RIGHT  = 162 
MOST_RIGHT = 235 #a bit confusing - means most left coordinate of RIGHT picture
RATIO_RIGHT = MAX_PICTURE_WIDTH_RIGHT / MAX_PICTURE_HEIGHT_RIGHT
DISTINCT_CHAR = '_' 
FOLDER = '10-3/'
debug = True

def remove_digits_from_list(l):
    ret = []
    for i in l:
        ret.append(remove_digits_from_string(i))
    return ret

def remove_digits_from_string(s):
    ret = ''
    for i in s:
        if i.isdigit():
            ret+='' 
        else:
            ret+=i
    return ret

def merge_multi_picture(folder, pic_l):
    """
    Takes in list of images and merges them into one 
    Numbering is important and dictates order
    return: Name of merged picture that was created 
    """
    imgs    = [ Image.open(folder+i) for i in pic_l]
    name = remove_digits_from_string(pic_l[0]).split('.')[0]
    fname = '{}_MERGED.jpg'.format(name)
    # Pick smallest image, and resize others to match it 
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    imgs_comb = Image.fromarray(imgs_comb)
    imgs_comb.save(folder+fname)    
    return fname

def write_pdf_to_file(pdf, fname):
    with open(fname, 'wb') as fp:
        pdf.write(fp)

def add_image_to_canvas(can, image, x, y, x_dim, y_dim):
    """
    Add Image image to existing_pdf at postion x, y
    with dimensions x_dim and y_dim
    return: Canvas object
    """
    can.drawImage(image, x, y, height=x_dim, width=y_dim)
    return can

def create_pdf_page_from_iostream(iostream):
    new_pdf = PdfFileReader(iostream)
    return new_pdf.getPage(0)

def create_pdf_file_writer(page):
    output = PdfFileWriter()
    output.addPage(page)

def load_pictures(folder):
    """ 
    Load all pictures in folder, prepare and group them
    Image names for Gesten and Bilder should differ by a distinct character like '_'
    return: 2-dim list with IMAGE NAMES [[gesten(10)][bilder(10)]]
    """
    # Linux system call to list all files in folder
    # TODO crossplatform
    raw = subprocess.check_output('ls {}'.format(FOLDER), shell=True)
    raw_l = raw.decode('utf-8').split('\n')[:-1]
    bilder, gesten  = [],[]
    # Split into Gesten & Bilder
    for i in raw_l:
        bilder.append(i) if DISTINCT_CHAR in i else gesten.append(i)
    # Find unique Gesten (remove digits; create set, remove file extension)
    gesten_uniq = [x.split('.')[0] for x in list(set(remove_digits_from_list(gesten)))]
    # Group numbered pictures together in 2-dim list
    # TODO beautify
    gesten_grouped = [] #contains complete filenames again
    for i in gesten_uniq:
        tmp = []
        for j in gesten:
            if i in j:
                tmp.append(j)
        gesten_grouped.append(tmp)
    # Assemble pictures together with 
    for i, val in enumerate(gesten_grouped):
        if len(val) > 1: #multiple pictures 
            # Exchange list of filenames with filename of merged picture
            gesten_grouped[i] = [merge_multi_picture(folder, val)]
    return gesten_grouped, bilder

def main():
    """
    1. Load the file names from FOLDER
    2. Create a blank Canvas and add every picture to it
    3. Load the template PDF and merge Canvas with it

    """
    gesten, bilder = load_pictures(FOLDER)
    if debug == True:
        print(gesten, bilder)
        print(len(gesten))
        print(len(bilder))
        print(gesten[1])
        print(bilder[1])

    packet = io.BytesIO()
    #Create Canvas object; add pictures to it
    c = canvas.Canvas(packet)

    # Add gesten to blank canvas
    for i in range(10): 
        y_left = 34 + i*79
        ppath = '{}{}'.format(FOLDER,gesten[i][0])
        im = Image.open(ppath)
        width, height = im.size
        ratio = width/height
        # Check if picture needs to be scaled and find center position
        if ratio < RATIO_LEFT:
            y_dim = MAX_PICTURE_HEIGHT_LEFT *ratio
            x_left = MOST_LEFT + (MAX_PICTURE_WIDTH_LEFT-y_dim)/2
        else:
            y_dim = MAX_PICTURE_WIDTH_LEFT
            x_left = MOST_LEFT
        c = add_image_to_canvas(c, ppath, x_left, y_left,
                MAX_PICTURE_HEIGHT_LEFT, y_dim) 
    # Add bilder to canvas
    for i in range(10):
        y_right = 29 + i*79
        r = choice(bilder)
        bilder.remove(r)
        ppath = '{}{}'.format(FOLDER, r)
        im = Image.open(ppath)
        width, height = im.size
        ratio = width/height
        if ratio < RATIO_RIGHT:
            y_dim = MAX_PICTURE_HEIGHT_RIGHT *ratio
            x_right = MOST_RIGHT + (MAX_PICTURE_WIDTH_RIGHT-y_dim)/2
        else:
            y_dim = MAX_PICTURE_WIDTH_RIGHT
            x_right = MOST_RIGHT
        c = add_image_to_canvas(c, ppath, x_right, y_right,
                MAX_PICTURE_HEIGHT_RIGHT, y_dim) 

    c.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    existing_pdf = PdfFileReader(open('template.pdf', 'rb'))
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output = PdfFileWriter()
    output.addPage(page)
    outputStream = open("test3.pdf", "wb")
    output.write(outputStream)
    outputStream.close()


if __name__ == '__main__':
    main()
