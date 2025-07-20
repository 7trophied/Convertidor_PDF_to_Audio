import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Convertidor de PDF a Audio 
# Este script convierte el texto de un archivo PDF en audio utilizando la biblioteca pyttsx3


book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

# Inicializa el motor de texto a voz
speaker = pyttsx3.init()

# Configura las propiedades del motor de voz
speaker.setProperty('voice', 'spanish')  # Cambia a voz en español
speaker.setProperty('rate', 150)  # Velocidad 
for num in range(pages):
    pdfpage = pdfreader.pages[num]
    text = pdfpage.extract_text()
    if text:  
        speaker.say(text)
        speaker.runAndWait()
