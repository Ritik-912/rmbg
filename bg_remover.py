from rembg import remove
from PIL import Image

## Path for input and output image
input_img = input('Enter input image path:\t')
output_img = "".join(input_img.split('.')[:-1]) + '_rmbg' + '.png'

## loading and removing background
inp = Image.open(input_img)
output = remove(inp)

## Saving background removed image to same location as input image
output.save(output_img)
