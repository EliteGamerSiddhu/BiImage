import tempfile

from Library.headers import BITMAPCOREHEADER, BITMAPFILEHEADER, BITMAPINFOHEADER
from Library.structures import PIXEL_ARRAY
from Library.basicfunc import calcFileSize, calcPixelArraySize, pixel_offset

class Img:

    def __init__(self, file_header : BITMAPFILEHEADER, dib_header, pixel_array : PIXEL_ARRAY, temp_file):
        self.file_header = file_header
        self.dib_header = dib_header
        self.pixel_array = pixel_array
        self.temp_file = temp_file

    def open(path):
        pass

    def new(width, height, bpp, dib_type = 'CORE', planes = 1, colour = None): #Later add other header support
        total_size = calcFileSize(width, height, bpp, dib_type)
        pixel_array_size = calcPixelArraySize(width, height, bpp)
        pixel_arr_offset = pixel_offset(dib_type)
        fheader = BITMAPFILEHEADER.new(total_size, pixel_arr_offset)
        dibheader = None
        if dib_type == 'CORE':
            dibheader = BITMAPCOREHEADER.new(width, height, bpp, planes)
        elif dib_type == 'INFO':
            dibheader = BITMAPINFOHEADER.new(width, height, bpp, pixel_array_size)
        elif dib_type == 'INFOV2':
            pass
        elif dib_type == 'INFOV3':
            pass
        elif dib_type == 'V4':
            pass
        elif dib_type == 'V5':
            pass
        pixelarr = PIXEL_ARRAY.new(width, height, bpp, colour)
        f = tempfile.TemporaryFile()
        fheader.write(f)
        dibheader.write(f)
        pixelarr.write(f)
        f.seek(0)
        print('File created')
        return Img(fheader, dibheader, pixelarr, f)
        
    def make_temp_copy(path):
        pass

    def save(self,dst):
        with open(dst, 'wb') as fout:
            data = self.temp_file.read()
            fout.write(data)
        print(f"File saved at {dst}")

    def make_temp(self):
        pass

    def __del__(self):
        del self.temp_file