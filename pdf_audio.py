import pyttsx3                     
import PyPDF2                       
import tkinter as tk                
from tkinter import filedialog, messagebox, ttk  

# Función para seleccionar un archivo PDF desde el explorador de archivos
def seleccionar_pdf():
    ruta_pdf = filedialog.askopenfilename(
        title="Selecciona el archivo PDF",
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    if not ruta_pdf:
        return  

    try:
        # Guarda la ruta y el lector del PDF en un diccionario global
        lector_pdf["file"] = ruta_pdf
        lector = PyPDF2.PdfReader(ruta_pdf)
        total_paginas = len(lector.pages)
        lector_pdf["reader"] = lector

        # Muestra cuántas pags tiene el PDF
        label_paginas.config(text=f"El PDF tiene {total_paginas} páginas.")

        # Habilita los campos de entrada y el boton de conversión para evitar errores
        entry_inicio.config(state="normal")
        entry_fin.config(state="normal")
        btn_convertir.config(state="normal")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el PDF:\n{e}")

# Func que convierte un rango de paginas del PDF a audio
def convertir_pdf_a_audio():
    lector = lector_pdf.get("reader")
    ruta = lector_pdf.get("file")

    if not lector or not ruta:
        messagebox.showerror("Error", "Primero selecciona un archivo PDF.")
        return

    total_paginas = len(lector.pages)

    
    try: # Obtiene el rango de pags del usuario
        inicio = int(entry_inicio.get())
        fin = int(entry_fin.get())
        if inicio < 1 or fin > total_paginas or inicio > fin:
            raise ValueError("Rango de páginas inválido.")
    except ValueError:
        messagebox.showerror("Error", "Debes ingresar un rango de páginas válido.")
        return

    # Inicializa el motor de texto 
    motor = pyttsx3.init()
    motor.setProperty('rate', 150)  # Velocidad de lectura
    motor.setProperty('voice', motor.getProperty('voices')[0].id)  #TODO: Cambiar a voz en español si es necesario t agregar mas voces

    # Itera por las páginas seleccionadas y convierte el texto a voz
    for i in range(inicio - 1, fin):
        pagina = lector.pages[i]
        texto = pagina.extract_text()
        if texto and texto.strip():
            motor.say(texto)
            motor.runAndWait()  # Comienza a hablar el compa robot

    motor.stop()
    messagebox.showinfo("Listo", "Conversión completada.")  # Notifica al usuario

# Configuración de la ventana 
ventana = tk.Tk()
ventana.title("PDF a Audio")             
ventana.geometry("350x300")              
ventana.resizable(False, False)  # No permite cambiar el tamaño de la ventana

frame = ttk.Frame(ventana, padding=20)
frame.pack(fill="both", expand=True)

lector_pdf = {}  # Diccionario global (linea 16)

# Elementos graficos
ttk.Label(frame, text="Conversor de PDF a Voz", font=("Segoe UI", 14)).pack(pady=(0, 10))

btn_seleccionar = ttk.Button(frame, text="Seleccionar PDF", command=seleccionar_pdf)
btn_seleccionar.pack()

label_paginas = ttk.Label(frame, text="")
label_paginas.pack(pady=(10, 5))

ttk.Label(frame, text="Página de inicio:").pack()
entry_inicio = ttk.Entry(frame, width=10, state="disabled")
entry_inicio.pack()

ttk.Label(frame, text="Página final:").pack()
entry_fin = ttk.Entry(frame, width=10, state="disabled")
entry_fin.pack()

btn_convertir = ttk.Button(frame, text="Convertir a Audio", command=convertir_pdf_a_audio, state="disabled")
btn_convertir.pack(pady=15, ipadx=20, ipady=8)

ventana.mainloop()
