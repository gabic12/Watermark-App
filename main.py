from PIL import Image, ImageOps, ImageDraw, ImageFont

IMAGE_PATH = "images/cat.jpg" #Change the path here
FONT_PERCENT = 7 #Change the font size here
MARGIN_PERCENT = 1 #Change the margin here

#User input
watermark_text = input("Enter the watermark's text: ")
watermark_text_position = input("Chose watermark position LU(left side up), LD(left side down), RU(right side up), RD(right side down), C(center): ")

#Open the image
img = Image.open(IMAGE_PATH).convert("RGBA")
img = ImageOps.exif_transpose(img) # Rotate the image in case the EXIF Orientation tag is other than 1
image_width = img.size[0]
image_height = img.size[1]

#New draw to add the text
text_img = Image.new('RGBA', img.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(text_img)

#Setting up the font size and position
font_size = (FONT_PERCENT / 100) * image_height
font = ImageFont.truetype("arial.ttf", font_size)
text_color = (255, 255, 255, 125) #white
text_width = draw.textlength(watermark_text, font)
text_height = font_size
margin_width = (MARGIN_PERCENT / 100) * image_width
margin_height = (MARGIN_PERCENT / 100) * image_height

if watermark_text_position.lower() == "lu":
    text_position = (margin_width, margin_height)
elif watermark_text_position.lower() == "ld":
    text_position = (margin_width, image_height - text_height - margin_height)
elif watermark_text_position.lower() == "ru":
    text_position = (image_width - text_width - margin_width, margin_height)
elif watermark_text_position.lower() == "rd":
    text_position = (image_width - text_width - margin_width, image_height - text_height - margin_height)
elif watermark_text_position.lower() == "c":
    text_position = ((image_width / 2) - (text_width / 2), (image_height / 2) - (text_height / 2))
else:
    text_position = (0, 0) #Default position

#Draw the watermark
draw.text(text_position, watermark_text, font=font, fill=text_color)

#Add the watermark to the image
watermarked = Image.alpha_composite(img, text_img)
watermarked.save("images/watermarked_image.png")

print("Watermark added, check the images folder.")