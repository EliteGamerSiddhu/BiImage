from Library.Exceptions import CustomError

class PIXEL_ARRAY:
    def __init__(self, arr):
        self.arr = arr
    
    def new(width, height, bpp, colour = None):
        if colour is None:
            if bpp <= 8:
                colour = '1' * bpp

            #Later add alpha channel support
            
            row_arr = colour * width
            if len(row_arr) % 32 != 0:
                row_arr += '0' * (32 - len(row_arr) % 32)

            byte_list = []
            for i in range(len(row_arr) - 7):
                data = row_arr[i:i+8]
                byte_list.append(data)

            pixel_row_arr = b''
            for i in byte_list:
                pixel_row_arr += int(i, 2).to_bytes(1, 'little')

            pixel_arr = pixel_row_arr * height
            
            return PIXEL_ARRAY(pixel_arr)

    def write(self, f):
        f.write(self.arr)