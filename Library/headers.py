from Library.structures import PIXEL_ARRAY
from Library.basicfunc import padding

#All the information stored in headers are in bytes for direct file writing

class BITMAPCOREHEADER:
    def __init__(self, width : bytes, height : bytes, bpp : bytes,  planes : bytes, size : bytes):
        self.size = size
        self.width = width
        self.height = height
        self.planes = planes
        self.bpp = bpp

    def new(width : int, height : int, bpp : int, planes : int = 1, size : int = 12):
        return BITMAPCOREHEADER(width.to_bytes(2, 'little'), height.to_bytes(2, 'little'), bpp.to_bytes(2, 'little'), planes.to_bytes(2, 'little'), size.to_bytes(4, 'little'))

    def write(self, f):
        f.write(self.size)
        f.write(self.width)
        f.write(self.height)
        f.write(self.planes)
        f.write(self.bpp)

class BITMAPFILEHEADER:
    def __init__(self , file_size : bytes, offset : bytes, reserved1 : bytes, reserved2 : bytes, file_type : bytes):
        self.file_type = file_type
        self.file_size = file_size
        self.reserved1 = reserved1
        self.reserved2 = reserved2
        self.offset = offset

    def new(file_size : int, offset : int, reserved1 : int = 0, reserved2 : int = 0, file_type : str = 'BM'):
        return BITMAPFILEHEADER(file_size.to_bytes(4, 'little'), offset.to_bytes(4, 'little'), reserved1.to_bytes(2, 'little'), reserved2.to_bytes(2, 'little'), bytes(file_type, 'utf-8'))

    def write(self, f):
        f.write(self.file_type)
        f.write(self.file_size)
        f.write(self.reserved1)
        f.write(self.reserved2)
        f.write(self.offset)

class BITMAPINFOHEADER:
    def __init__(self, width : bytes, height : bytes, bpp : bytes, pixel_array_size : bytes, X_pixels_per_metre : bytes, Y_pixels_per_metre : bytes, compression : bytes ,colours_used : bytes, colours_important : bytes, planes : bytes, size : bytes):
        self.size = size
        self.width = width
        self.height = height
        self.planes = planes
        self.bpp = bpp
        self.compression = compression
        self.pixel_array_size = pixel_array_size
        self.X_pixels_per_metre = X_pixels_per_metre
        self.Y_pixels_per_metre = Y_pixels_per_metre
        self.colours_used = colours_used
        self.colours_important = colours_important

    def new(width : int, height : int, bpp : int, pixel_array_size : int, X_pixels_per_metre : int = 1835, Y_pixels_per_metre : int = 1835, compression : int = 0, colours_used : int = 0, colours_important : int = 0, planes : int = 1, size : int = 40):
        return BITMAPINFOHEADER(width.to_bytes(4, 'little'), height.to_bytes(4, 'little'), bpp.to_bytes(2, 'little'), pixel_array_size.to_bytes(4, 'little'), X_pixels_per_metre.to_bytes(4, 'little'), Y_pixels_per_metre.to_bytes(4, 'little'), compression.to_bytes(4, 'little'), colours_used.to_bytes(4, 'little'), colours_important.to_bytes(4,'little'), planes.to_bytes(2, 'little'), size.to_bytes(4, 'little'))

    def write(self, f):
        f.write(self.size)
        f.write(self.width)
        f.write(self.height)
        f.write(self.planes)
        f.write(self.bpp)
        f.write(self.compression)
        f.write(self.pixel_array_size)
        f.write(self.X_pixels_per_metre)
        f.write(self.Y_pixels_per_metre)
        f.write(self.colours_used)
        f.write(self.colours_important)

"""class BITMAPV2INFOHEADER(BITMAPINFOHEADER):
    def __init__(self, width : bytes, height : bytes, bpp : bytes, pixel_array_size : bytes, red_mask : bytes, green_mask : bytes, blue_mask : bytes, X_pixels_per_metre : bytes, Y_pixels_per_metre : bytes, compression : bytes, colours_used : bytes, colours_important : bytes, planes : bytes, size : bytes):
        super().__init__(self, width , height , bpp , pixel_array_size , X_pixels_per_metre , Y_pixels_per_metre , compression ,colours_used , colours_important , planes , size)
        self.red_mask = red_mask
        self.green_mask = green_mask
        self.blue_mask = blue_mask

    def new(width : int, height : int, bpp : int, pixel_array_size : int, red_mask )

class BITMAPV3INFOHEADER(BITMAPV2INFOHEADER):
    def __init__(self, size, width, planes, bitcount, compression, image_size, X_pixels_per_metre, Y_pixels_per_metre, colours_used, colours_important, red_mask, green_mask, blue_mask, alpha_mask):
        super().__init__(self, width, height, planes, bpp, pixel_array_size, red_mask, green_mask, blue_mask, X_pixels_per_metre, Y_pixels_per_metre, compression, colours_used, colours_important, size)
        self.alpha_mask = alpha_mask

class BITMAPV4HEADER(BITMAPV3INFOHEADER):
    def __init__(self, size, width, planes, bitcount, compression, image_size, X_pixels_per_metre, Y_pixels_per_metre, colours_used, colours_important, red_mask, green_mask, blue_mask, alpha_mask, colour_space, ciexyz : CIEXYZTRIPLE, gamma_red, gamma_green, gamma_blue):
        super().__init__(self, size, width, planes, bitcount, compression, image_size, X_pixels_per_metre, Y_pixels_per_metre, colours_used, colours_important, red_mask, green_mask, blue_mask, alpha_mask)
        self.colour_space = colour_space
        self.ciexyz = ciexyz
        self.gamma_red = gamma_red
        self.gamma_green = gamma_green
        self.gamma_blue = gamma_blue

class BITMAPV5HEADER(BITMAPV4HEADER):
    def __init__(self, size, width, planes, bitcount, compression, image_size, X_pixels_per_metre, Y_pixels_per_metre, colours_used, colours_important, red_mask, green_mask, blue_mask, alpha_mask, colour_space, ciexyz : CIEXYZTRIPLE, gamma_red, gamma_green, gamma_blue, intent, profile_data, profile_size, reserved):
        super().__init__(self, size, width, planes, bitcount, compression, image_size, X_pixels_per_metre, Y_pixels_per_metre, colours_used, colours_important, red_mask, green_mask, blue_mask, alpha_mask, colour_space, ciexyz, gamma_red, gamma_green, gamma_blue)
        self.intent = intent
        self.profile_data = profile_data
        self.profile_size = profile_size
        self.reserved = reserved
        """