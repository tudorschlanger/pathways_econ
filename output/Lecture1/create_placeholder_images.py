#!/usr/bin/env python3
"""
Create placeholder images for money and happy person
"""
from PIL import Image, ImageDraw, ImageFont
import os

# Create directories if needed
os.makedirs('fig', exist_ok=True)

# Create money.jpg - green with dollar signs
img_money = Image.new('RGB', (400, 300), color='#E8F5E9')
draw_money = ImageDraw.Draw(img_money)

# Draw dollar sign symbols
text = "💵"
# Draw simple green rectangle with $ text
draw_money.rectangle([(50, 50), (350, 250)], fill='#2E7D32', outline='#1B5E20', width=3)
draw_money.text((160, 110), "$$$", fill='white', font=None)

img_money.save('fig/money.jpg')
print("✓ Created fig/money.jpg")

# Create happy_person.jpg - smiley face
img_happy = Image.new('RGB', (400, 300), color='#FFF9C4')
draw_happy = ImageDraw.Draw(img_happy)

# Draw smiley face
# Head
draw_happy.ellipse([(50, 50), (350, 250)], fill='#FFD54F', outline='#F57F17', width=4)
# Left eye
draw_happy.ellipse([(120, 120), (160, 160)], fill='#333333')
# Right eye
draw_happy.ellipse([(240, 120), (280, 160)], fill='#333333')
# Smile
draw_happy.arc([(100, 80), (300, 240)], 0, 180, fill='#F57F17', width=4)

img_happy.save('fig/happy_person.jpg')
print("✓ Created fig/happy_person.jpg")
