from PIL import Image
import exifread

# Caminho para a imagem
#image_path = "20241108_075634.jpg"
image_path = r"C:\Users\DELL\Downloads\TC_00041.jpg"
# Abrindo a imagem com Pillow
with Image.open(image_path) as img:
    # Exibindo informações básicas de metadados
    print("Formato:", img.format)
    print("Tamanho:", img.size)
    print("Modo:", img.mode)

    # Exibindo metadados EXIF com Pillow (nem todas as imagens têm EXIF)
    exif_data = img._getexif()
    if exif_data:
        for tag, value in exif_data.items():
            print(f"{tag}: {value}")
    else:
        print("Nenhum dado EXIF encontrado com Pillow.")

# Usando ExifRead para metadados EXIF detalhados
with open(image_path, 'rb') as img_file:
    tags = exifread.process_file(img_file)
    for tag in tags.keys():
        print(f"{tag}: {tags[tag]}")