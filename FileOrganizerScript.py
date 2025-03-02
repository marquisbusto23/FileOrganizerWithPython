import os
import shutil

# Directorio que contiene los archivos desorganizados
source_dir = 'C:/Users/marco/Downloads/AllFiles'  # Puedes usar '/' o '\\' 

# Extensiones de archivos y sus carpetas de destino correspondientes
file_types = {
    'IMAGENES': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'DOCUMENTOS': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'VIDEOS': ['.mp4', '.avi', '.mov', '.mkv'],
    'AUDIOS': ['.mp3', '.wav', '.aac'],
    'OTROS': []
}

# Crear las carpetas de destino si no existen
for folder in file_types.keys():
    os.makedirs(os.path.join(source_dir, folder.upper()), exist_ok=True)

# Mover archivos a las carpetas correspondientes
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    if os.path.isfile(file_path):
        try:
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(source_dir, folder.upper(), filename))
                    moved = True
                    break
            # Si la extensión del archivo no está en las listas, mover a 'OTROS'
            if not moved:
                shutil.move(file_path, os.path.join(source_dir, 'OTROS', filename))
        except Exception as e:
            print(f"Error al mover el archivo {filename}: {e}")

print("Archivos organizados correctamente.")
