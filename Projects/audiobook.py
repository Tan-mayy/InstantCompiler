import pyttsx3 
import PyPDF2

pdf_file = open('4thsem.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)

number_of_pages = read_pdf.getNumPages()

engine = pyttsx3.init()

for i in range(1, number_of_pages ):
    # Read the PDF page 
    page = read_pdf.getPage(i)
    
    # Extract the text of the PDF page 
    page_content = page.extractText()
        
    # say method on the engine that passing input text to be spoken 
    engine.say(page_content) 
    
    # run and wait method to processes the voice commands.  
    engine.runAndWait()