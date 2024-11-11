from PIL import Image, ImageDraw, ImageFont
import exifread
from datetime import datetime

# Caminho para a imagem
image_path = r"C:\Users\DELL\Downloads\TC_00041.jpg"
image_path = r"C:\Users\DELL\OneDrive\Área de Trabalho\SIMCAR_DIGITAL_CAMPO\CAMPO_20241108\CAMPO_20241108\20241108_075643.jpg"
output_path = "imagem_anotada.jpg"

# Função para extrair latitude, longitude e direção de visada dos metadados EXIF
def obter_exif_data(image_path):
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file)
        
        # Extraindo as informações de latitude, longitude e direção
        datahora = tags.get("EXIF DateTimeOriginal")
        latitude = tags.get("GPS GPSLatitude")
        latitude_letter = tags.get('GPS GPSLatitudeRef')
        longitude = tags.get("GPS GPSLongitude")
        longitude_letter = tags.get('GPS GPSLongitudeRef')
        visada = tags.get("GPS GPSImgDirection")
        altitude = tags.get('GPS GPSAltitude')
        
        # Convertendo as coordenadas para string legível
        def coordenada_para_str(coord):
            if coord:
                graus, minutos, segundos = [float(x.num) / float(x.den) for x in coord.values]
                return "{}°{}'{}\"".format(int(graus), int(minutos), segundos)
            return "Desconhecido"
        
        # Converter para o objeto datetime se a data estiver presente
        if datahora:
            dt = datetime.strptime(str(datahora), "%Y:%m:%d %H:%M:%S")
            data = dt.strftime("%d/%m/%Y")
            hora = dt.strftime("%H:%M:%S")
        else:
            data = "Desconhecido"
            hora = "Desconhecido"

        latitude = coordenada_para_str(latitude)
        latitude_letter = latitude_letter.values[0]
        longitude = coordenada_para_str(longitude)
        longitude_letter = longitude_letter.values[0]
        visada = "{}°".format(round(float(visada.values[0].num) / float(visada.values[0].den), 2)) if visada else "Desconhecido"
        altitude = "{}m".format(round(float(altitude.values[0].num) / float(altitude.values[0].den), 2)) if altitude else "Desconhecido"
        
        return latitude, latitude_letter, longitude, longitude_letter, visada, altitude, data, hora

# Carregar a imagem e extrair dados EXIF
latitude, latitude_letter, longitude, longitude_letter, visada, altitude, data, hora = obter_exif_data(image_path)

# Abrir imagem original
img = Image.open(image_path)
largura, altura = img.size

# Configurações do retângulo e texto
altura_quadrado = int(0.1 * altura)  # 10% da altura da imagem
quadrado_preto = Image.new("RGB", (largura, altura_quadrado), "black")
draw = ImageDraw.Draw(quadrado_preto)

# Texto a ser inserido
texto = "Data: {}, Hora: {} \nLatitude: {} {} | Longitude: {} {} | Direção: {} | Altitude: {}".format(
    data, hora, latitude, latitude_letter, longitude, longitude_letter, visada, altitude)

# Determinar o tamanho da fonte para encaixar no quadrado
for tamanho_fonte in range(300, 10, -1):  # Testa do tamanho 100 até o mínimo necessário
    fonte = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", tamanho_fonte)
    largura_texto, altura_texto = draw.textsize(texto, font=fonte)
    if altura_texto <= altura_quadrado - 10 and largura_texto <= largura - 10:
        break  # Encontra o maior tamanho de fonte que cabe dentro do quadrado
posicao_texto = ((largura - largura_texto) // 2, (altura_quadrado - altura_texto) // 2)

# Desenhar o texto no quadrado
draw.text(posicao_texto, texto, fill="white", font=fonte)

# Combinar a imagem original com o quadrado preto
nova_imagem = Image.new("RGB", (largura, altura + altura_quadrado))
nova_imagem.paste(img, (0, 0))
nova_imagem.paste(quadrado_preto, (0, altura))

# Salvar a imagem final mantendo metadados EXIF
nova_imagem.save(output_path, "JPEG", exif=img.info.get("exif"))

print("Imagem anotada salva em: {}".format(output_path))
