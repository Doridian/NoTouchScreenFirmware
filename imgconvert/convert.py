from PIL import Image
from sys import stdout

IMG = Image.open('background.png')
IMG = IMG.convert('RGB')
MULT = 0.6
WIDTH = 480
HEIGHT = 320

def convert_color(rgb, mult = 1.0):
    (r,g,b) = rgb
    r *= mult
    g *= mult
    b *= mult
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    r = int(r)
    g = int(g)
    b = int(b)
    return ((r >> 3) << 11) | ((g >> 2) << 5) | (b >> 3)

pixels = []
paletteTable = {}
palette = []
for y in range(0, HEIGHT):
    lpixels = []
    for x in range(0, WIDTH):
        col = convert_color(IMG.getpixel((x,y)), MULT)
        if col in paletteTable:
            lpixels.append("%d" % paletteTable[col])
        else:
            idx = len(palette)
            palette.append("0x%04X" % col)
            lpixels.append("%d" % idx)
            paletteTable[col] = idx
            if idx > 255:
                raise ValueError("More than 256 colors!")
    pixels.append('{%s}' % ','.join(lpixels))

out = open('../src/User/background.h', 'w')
out.write('''
#pragma once

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif
const uint8_t backgroundPixels[%d][%d] = {''' % (HEIGHT, WIDTH))
out.write(',\n'.join(pixels))
out.write('''};
const uint16_t backgroundPalette[] = {''')
out.write(','.join(palette))
out.write('''};
#ifdef __cplusplus
}
#endif
''')
out.close()
