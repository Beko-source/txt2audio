# Import the python text to speech libarary and the PDF REader library
import PyPDF3
import pyttsx3
import pdfplumber

# Read the PDF file binary mode
file = 'on_murder.pdf'
book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)

# Find the number of pages in the PDF document
pages = pdfReader.numPages

finalText = ""

with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        # Read the PDF page
        page = pdf.pages[i]
        # Extract the text of the PDF page
        text = page.extract_text()
        # Collect all text in one place
        finalText += text

# save text as mp3
engine = pyttsx3.init()

# set the audio speed and volume
newrate = 200
engine.setProperty('rate', newrate)
newvolume = 200
engine.setProperty('volume', newvolume)
finalText += text

engine.save_to_file(finalText, 'on_murder.mp3')
engine.runAndWait()

# hear text
engine = pyttsx3.init()

# set the audio speed and volume
newrate = 200
engine.setProperty('rate', newrate)
newvolume = 200
engine.setProperty('volume', newvolume)
finalText += text

engine.say(finalText)
engine.runAndWait()
