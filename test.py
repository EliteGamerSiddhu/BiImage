from Library.bpp import Img
from Library.colours import four_bpp

samp = Img.new(600, 600, 4, 'INFO', colour= four_bpp.mindaro)
samp.save('lol.bmp')
