from PIL import Image
import numpy as np

name = input('enter image name: ')

try:
    im = Image.open(name)
except FileNotFoundError:
    print('image does not exist')
    exit()

im = Image.open(name)
new_size = im.size
new_size = (new_size[0] // 4, new_size[1] // 8)
im = im.resize(new_size)

symbols = {0: ' ', 32: '.', 64: ':', 96: '/', 128: 'O', 160: '8', 192: 'B', 224: '#'}

new_im = [[[np.mean(pix).astype(np.uint8), np.mean(pix).astype(np.uint8), np.mean(pix).astype(np.uint8), pix[3]] for pix in row] for row in np.asarray(im)]

ascii = ''
for row in new_im:
    for pix in row:
        ascii += symbols[(pix[0] // 32) * 32]
    ascii += '\n'
output = '.'.join(name.split('.')[:-1]) + '.txt'

with open(output, 'w+') as f:
    f.write(ascii)