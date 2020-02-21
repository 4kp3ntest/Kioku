import requests
import shutil
import os
import re
from fpdf import FPDF


print('[*] What chapter to crawl?')
chapter = input()
path = 'https://rawkuma.com/one-piece-chapter-{}/'.format(chapter)
pdf = FPDF()

raw = requests.get(path).text

all_image_urls = re.findall('<img src="(.*?\.jpg)"', raw)[:-1] #last image asks for donations

for image_url in all_image_urls:
    print(image_url)
    pdf.add_page()
    resp = requests.get(image_url, stream=True)
    # Open a local file with wb ( write binary ) permission.
    local_file = open('local_image.jpg', 'wb')
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True
    # Copy the response stream raw data to local image file.
    shutil.copyfileobj(resp.raw, local_file)
    del resp
    # Remove the image url response object.
    pdf.image(local_file,0,0)

pdf.output("yourfile.pdf", "F")
