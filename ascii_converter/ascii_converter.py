# steps
# 1. ASCII Characters Map
# 2. Calculating a Pixel’s Brightness
# 3. Converting a Pixel to a Character
# 4. Parsing an Image
import PIL
from PIL import Image
import time

# this only seems to work for very small images


ascii_characters_by_surface = (
    '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
)
#add an empty space ?

print(len(ascii_characters_by_surface))
im = Image.open("turbine.jpg")
width, height = im.size

#@profile
def pixel_to_ascii(pixel):
    brightness_weight = len(ascii_characters_by_surface) / 765
    pixel_brightness = sum(pixel)
    index =  int((pixel_brightness * brightness_weight))
    px_ascii = ascii_characters_by_surface[index]
    return px_ascii

#@profile
def image_to_ascii(image):
    ascii_art = []
    count = 0
    for y in range(0, height - 1):
        line = ""
        for x in range(0, width - 1):
            count += 1
            px = im.getpixel((x, y))
            line += pixel_to_ascii(px)

            #attempt at a loading bar
            if count / (height * width) % 0.1 < 0.00001:
                print("█", end="")
                print(f"{count/(height*width):.2}", "%")
        ascii_art.append(line)
    return ascii_art

#@profile
def image_to_ascii_method2(image):
    pixels = list(im.getdata())
    ascii_art = []
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    print(pixels)
    return pixels

#@profile
def save_as_text(ascii_art):
    with open("image.txt", "w") as file:
        for line in ascii_art:
            file.write(line)
            file.write("\n")
        file.close()

#def view_txt(filename)


# method 1
# pixels = [pixels[i * width:(i+1) * width] for i in range(height)]


# method 2.5
# brightness_weight = len(ascii_characters_by_surface) / max_brightness
# index = int(pixel_brightness * brightness_weight) - 1
# return ascii_characters_by_surface[index]


# method 2
#@profile
def main():
    image = Image.open("water.PNG")
    width, height = image.size
    ascii_art = image_to_ascii(image)
    save_as_text(ascii_art)
    image_to_ascii_method2(image)
    index=0
    for char in ascii_art:
        print(char)
        time.sleep(0.1)
        index+=1

main()