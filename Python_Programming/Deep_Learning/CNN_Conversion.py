from PIL import Image

img = Image.open("digit.png")

print(img.size) 

img = img.convert("L")          #Convert img into grayscale

img = img.resize((28,28))       # Resize img into 28 * 28 

img.save("digit_28x28.png")

print(img.size)