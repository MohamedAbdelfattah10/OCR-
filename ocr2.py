from PIL import Image
import pytesseract
from pdf2image import convert_from_path
# Path of the pdf
PDF_file = "E:/Abdelfattah/Graduation Porject/Mohamed 2019-HR.pdf"
def ocr(PDF_file):
#Converting PDF to images
    pages = convert_from_path(PDF_file, 500)
    # Counter to store images of each page of PDF to image
    image_counter = 1
    for page in pages:
    	filename = "page_"+str(image_counter)+".jpg"
    	page.save(filename, 'JPEG')
    	image_counter = image_counter + 1
    # Recognizing text from the images
    filelimit = image_counter-1
    # Creating a text file to write the output
    outfile = "out_text.txt"
    # Open the file in append mode so that
    f = open(outfile, "a")
    # Iterate from 1 to total number of pages
    for i in range(1, filelimit + 1):
    	filename = "page_"+str(i)+".jpg"
    	# Recognize the text as string in image using pytesserct
    	text = str(((pytesseract.image_to_string(Image.open(filename)))))
    	text = text.replace('-\n', '')	
    	# Finally, write the processed text to the file.
    	f.write(text)
    # Close the file after writing all the text.
    f.close()
    return 0 

    
      

