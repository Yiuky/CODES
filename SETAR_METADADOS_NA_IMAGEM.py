# -*- coding: utf-8 -*-
from PIL import Image
import piexif
import os

def convert_to_dms(degree):
    """Converte coordenadas decimais para o formato DMS (graus, minutos, segundos) exigido pelo EXIF."""
    d = int(degree)
    m = int((degree - d) * 60)
    s = round((degree - d - m/60) * 3600, 2)
    return ((d, 1), (m, 1), (int(s * 100), 100))

def set_gps_location_if_absent(image_path, latitude, longitude):
    img = Image.open(image_path)
    # Carrega os metadados EXIF, se presentes
    exif_dict = piexif.load(img.info.get("exif", b''))
    
    # Verifica se já existe informação de GPS
    if piexif.GPSIFD.GPSLatitude in exif_dict["GPS"] and piexif.GPSIFD.GPSLongitude in exif_dict["GPS"]:
        print("Imagem já possui dados de GPS. Nenhuma alteração foi feita.")
    else:
        # Converte coordenadas para o formato EXIF GPS (DMS)
        lat_dms = convert_to_dms(abs(latitude))
        lon_dms = convert_to_dms(abs(longitude))
        
        # Define a direção N/S e E/W com base no valor das coordenadas
        lat_ref = 'N' if latitude >= 0 else 'S'
        lon_ref = 'E' if longitude >= 0 else 'W'
        
        # Insere dados de GPS nos metadados EXIF
        exif_dict['GPS'][piexif.GPSIFD.GPSLatitude] = lat_dms
        exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef] = lat_ref
        exif_dict['GPS'][piexif.GPSIFD.GPSLongitude] = lon_dms
        exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef] = lon_ref

        # Insere os metadados na imagem e salva com o novo nome
        exif_bytes = piexif.dump(exif_dict)
        
        # Define o novo caminho de saída
        base, ext = os.path.splitext(image_path)
        output_path = f"{base}_geo{ext}"
        
        img.save(output_path, "jpeg", exif=exif_bytes)
        print(f"Localização inserida: Latitude {latitude}, Longitude {longitude}")
        print(f"Imagem salva como: {output_path}")

# Caminho da imagem e coordenadas
image_path = "C:\Users\DELL\OneDrive\Área de Trabalho\SIMCAR_DIGITAL_CAMPO\CAMPO_20241108\CAMPO_20241108\20241108_075634.jpg"
latitude = -23.5505  # Exemplo: São Paulo
longitude = -46.6333  # Exemplo: São Paulo

# Inserindo localização somente se não houver dados GPS
set_gps_location_if_absent(image_path, latitude, longitude)