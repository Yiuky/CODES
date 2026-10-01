# CODES · Ferramentas para fotos de campo

Scripts em Python para trabalhar com os **metadados EXIF** de fotos tiradas em vistorias e trabalhos de
campo: carimbar data, hora e coordenadas na própria imagem, inspecionar os metadados e gravar a posição GPS
em fotos que não têm.

| Script | O que faz |
|---|---|
| `INSERIR_DADOS_NA_IMAGEM.py` | Lê data/hora, latitude, longitude e direção de visada do EXIF e escreve essas informações sobre a foto (gera `imagem_anotada.jpg`) |
| `PRINTAR_DADOS_DA_IMAGEM.py` | Mostra formato, tamanho e todos os metadados EXIF da imagem (Pillow + ExifRead) |
| `SETAR_METADADOS_NA_IMAGEM.py` | Grava latitude e longitude no EXIF (formato graus/minutos/segundos) quando a foto ainda não tem GPS |

## Requisitos

```bash
pip install pillow exifread piexif
```

Ajuste o caminho da imagem (`image_path`) no início de cada script antes de executar.

## ☕ Doe um café para o dev

Se estes scripts economizaram o seu tempo, considere pagar um café para o desenvolvedor.

<table>
  <tr>
    <td align="center"><img src="pix_qrcode.png" alt="QR Code Pix" width="170" /></td>
    <td>
      <strong>Pix</strong> (qualquer valor)<br><br>
      Chave aleatória:<br>
      <code>fcf8071f-416d-49f1-b4b9-3188d3d03c4b</code><br><br>
      <em>Favorecido: Joberth Firmino Gambati</em>
    </td>
  </tr>
</table>

---
Autor: [Joberth Firmino Gambati](https://github.com/Yiuky) · CGMA/SEMA-MT
