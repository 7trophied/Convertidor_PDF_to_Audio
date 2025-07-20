# PDF a Audio (Texto a Voz)

Programa desarrollado en Python que integra un script que permite convertir el texto contenido en un archivo PDF a voz, mediante una interfaz gráfica construida con Tkinter y el uso del motor de síntesis de voz `pyttsx3`.

## Características

- Interfaz gráfica sencilla y con validacion basica.
- Selección de archivos PDF desde el explorador del sistema.
- Permite ingresar un rango personalizado de páginas a convertir.
- Conversión de texto a voz local (sin conexión a internet).
- Manejo básico de errores (archivos inválidos, rangos fuera de límite, etc.).

## Tecnologías utilizadas

- Python 3.x
- Tkinter (interfaz gráfica)
- PyPDF2 (lector de archivos PDF)
- pyttsx3 (síntesis de texto a voz)

## Uso

1. Correr la aplicación.  
2. Seleccionar un archivo PDF desde el botón correspondiente.  
3. Ingresar el número de página de inicio y de fin (según el contenido que quieras escuchar).  
4. Presionar el botón "Convertir a Audio".  
5. El contenido textual será leído en voz alta mediante el sistema TTS integrado.

## Consideraciones

- La aplicación valida que el usuario haya seleccionado un archivo PDF antes de permitir el ingreso del rango de páginas.
- Se implementa control de errores básicos mediante excepciones, por ejemplo:
  - rango de páginas inválido (inicio mayor que fin, valores fuera del límite válido),
  - error al abrir o leer el PDF.
- El motor de síntesis `pyttsx3` funciona localmente y no requiere conexión a internet.

**Gracias por leer**         
7t

   
