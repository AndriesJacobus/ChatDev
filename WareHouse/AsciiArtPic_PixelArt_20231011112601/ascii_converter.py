'''
Image to ASCII art converter.
'''
import math
class ASCIIConverter:
    def __init__(self):
        self.ascii_chars = '@%#*+=-:. '
    def convert(self, image, width, scale):
        # Resize the image
        new_width = int(image.width * scale)
        new_height = int(image.height * scale)
        resized_image = image.resize((new_width, new_height))
        # Convert the image to grayscale
        grayscale_image = resized_image.convert('L')
        # Map grayscale values to ASCII characters
        ascii_art = ''
        for y in range(new_height):
            for x in range(new_width):
                pixel = grayscale_image.getpixel((x, y))
                ascii_char = self.ascii_chars[min(math.floor(pixel / 32), len(self.ascii_chars) - 1)]
                ascii_art += ascii_char
            ascii_art += '\n'
        # Adjust the width of the ASCII art
        lines = ascii_art.split('\n')
        ascii_art = '\n'.join(line[:width] for line in lines)
        return ascii_art