from Library.Exceptions import CustomError

class PIXEL_ARRAY:
    def __init__(self, arr):
        self.arr = arr
    
    def new(width, height, bpp, colour = None):
        if colour is None:
            if bpp <= 8:
                colour = '1' * bpp

            #Later add alpha channel support
            
            pixel_arr = PIXEL_ARRAY.make_pixel_array(width, height, colour)
            
            return PIXEL_ARRAY(pixel_arr)

        elif isinstance(colour, str):
            if len(colour) != bpp:
                raise CustomError('Length of colour binary should be equal to bits per pixel')

            elif '1' not in colour and '0' not in colour:
                raise CustomError('The colour binary does not contains neither a 1 or 0 or it is empty')

            else:
                pixel_arr = PIXEL_ARRAY.make_pixel_array(width, height, colour)
                
                return PIXEL_ARRAY(pixel_arr)


    def make_pixel_array(width : int, height : int, colour : str):
        row_arr = colour * width
        if len(row_arr) % 32 != 0:                      #Making sure that each row starts with a multiple of 4 bytes
            row_arr += '0' * (32 - len(row_arr) % 32)   #by making the string a multiple of 32 bits

        byte_list = []
        for i in range(0, len(row_arr) - 7, 8): #Works if i remove stepping which adds large amounts of useless information
                                                #in the end of the file
            data = row_arr[i:i+8]
            byte_list.append(data)

        pixel_row_arr = b''
        for i in byte_list:
            pixel_row_arr += int(i, 2).to_bytes(1, 'little')  #converting each 8 bits to 1 byte

        pixel_arr = pixel_row_arr * height

        #pixel_arr += b'00000000' This is needed by 1 bpp to work for some unknown reasons

        return pixel_arr

    def write(self, f):
        f.write(self.arr)