import glob
import sys
import os
import re
from PIL import Image, ImageOps, ImageEnhance, ImageDraw, ImageFont


class ImageProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.img = Image.open(filepath).convert("RGBA")

    def contrast(self, amount=1.5):
        enhancer = ImageEnhance.Contrast(self.img)
        self.img = enhancer.enhance(amount)

    def grayscale(self):
        self.img = ImageOps.grayscale(self.img)
        self.img = self.img.convert("RGB")

    def ascii(self):
        letters = [" ", "C", "S", "5", "0", ".", "-", "!"]
        font_size = 10
        (w, h) = self.img.size

        new_w = int(w / font_size)
        new_h = int(h / font_size)

        sample_size = (new_w, new_h)
        final_size = (new_w * font_size, new_h * font_size)

        self.grayscale()
        self.contrast(5.0)
        self.img = self.img.resize(sample_size)

        ascii_output = Image.new("RGBA", final_size, color="#ffff")
        font = ImageFont.truetype("font/Mattone-Regular.otf")
        drawer = ImageDraw.Draw(ascii_output)
        for i in range(new_w):
            for j in range(new_h):
                (r, g, b) = self.img.getpixel((i, j))

                brightness = r / 256
                letter = letters[int(len(letters) * brightness)]

                position = (i * font_size, j * font_size)
                drawer.text(position, letter, font=font, fill=(0, 0, 0, 255))

        self.img = ascii_output

    def rotate_180(self):
        self.img = self.img.rotate(180)

    def resize(self, size=(128, 128)):
        self.img.thumbnail(size)

    def square(self, size=200):
        (w, h) = self.img.size
        if w > h:
            x = (w - h) * 0.5
            y = 0
            box = (x, y, h + x, h + y)
        else:
            x = 0
            y = (h - w) * 0.5
            box = (x, y, x + w, y + w)

        self.img = self.img(resize(size, size), box=box)

    def watermark(self):
        font = ImageFont.truetype("font/Mattone-Regular.otf")

        drawer.text((32, 32), "CS50 watermark", font=font, fill=(255, 0, 0))

    def save(self, output):
        self.img.save(output)

        # list with all .jpg files inside input folder


def generate_art(inp, output):
    try:
        image = ImageProcessor(inp)
    except:
        sys.exit("Input not found")
    else:
        image.ascii()
        image.save(output)


def get_file_name():
    file = input("Insert file name: ").strip()

    file = "input/" + file
    return file


def get_output_folder():
    os.makedirs("outputs", exist_ok=True)
    paths = inputs.split(".")
    output = inputs.replace(f"{paths[0]}", "output")
    return output


def main():
    file = get_file_name()
    output = get_output_folder()

    # inputs = glob.glob("input/*.jpg")
    generate_art(file, output)


if __name__ == "__main__":
    main()
