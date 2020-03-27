from PIL import Image

img = Image.open('../day10/pic.jpg')
print(img.size)
print(img.format)
print(img.format_description)
img.save('./guido.jpg')

img2 = Image.open('../day10/pic.jpg')
img3 = img2.crop((335, 435, 430, 615))
for x in range(4):
    for y in range(5):
        img2.paste(img3, (95 * y, 180 * x))
img2.resize((img.size[0] // 2, img.size[1] // 2))
img2.rotate(90)
img2.save('./guido2.jpg')
