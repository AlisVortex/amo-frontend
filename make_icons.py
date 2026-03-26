from PIL import Image, ImageDraw, ImageFont
import os

def make_icon(size, filename):
    img = Image.new("RGB", (size, size), "#0a0f1e")
    draw = ImageDraw.Draw(img)
    # Круг
    margin = size // 8
    draw.ellipse([margin, margin, size-margin, size-margin], fill="#60a5fa")
    # Буква Э
    font_size = size // 2
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    text = "Э"
    bbox = draw.textbbox((0,0), text, font=font)
    tw = bbox[2]-bbox[0]
    th = bbox[3]-bbox[1]
    x = (size - tw) // 2
    y = (size - th) // 2
    draw.text((x, y), text, fill="white", font=font)
    img.save(filename)
    print("Создан: " + filename)

try:
    make_icon(192, "icon-192.png")
    make_icon(512, "icon-512.png")
    make_icon(96,  "icon-96.png")
    print("Иконки созданы!")
except ImportError:
    print("Установите Pillow: pip install Pillow")
    print("Или используйте любые PNG иконки 192x192 и 512x512")

input("Enter для выхода...")
