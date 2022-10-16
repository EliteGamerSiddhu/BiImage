import math

LCS_CALIBRATED_RGB = '0x00000000'
LCS_sRGB = '0x73524742'
LCS_WINDOWS_COLOR_SPACE = '0x57696E20'

def dib_check(dib_size):
    if dib_size == 40:
        return 'INFO'
    elif dib_size == 52:
        return 'INFOV2'
    elif dib_size == 56:
        return 'INFOV3'
    elif dib_size == 108:
        return 'V4'
    else:
        return 'V5'

def padding(b : bytes, req : int):
    if len(b) < req:
        x = b + (b'0' * (req - len(b)))
        return x

def calcFileSize(width : int, height : int, bpp : int, dib_type : str):
    file_header_size = 14
    dib_size = 0
    if dib_type == 'CORE':
        dib_size = 12
    elif dib_type == 'INFO':
        dib_size = 40
    elif dib_type == 'INFOV2':
        dib_size = 52
    elif dib_type == 'INFOV3':
        dib_size = 56
    elif dib_type == 'V4':
        dib_size = 108
    elif dib_type == 'V5':
        dib_size = 124
    size = file_header_size + dib_size + calcPixelArraySize(width, height, bpp)
    return int(size)

def pixel_offset(dib_type : str):
    file_header_size = 14
    dib_size = 0
    if dib_type == 'CORE':
        dib_size = 12
    elif dib_type == 'INFO':
        dib_size = 40
    elif dib_type == 'INFOV2':
        dib_size = 52
    elif dib_type == 'INFOV3':
        dib_size = 56
    elif dib_type == 'V4':
        dib_size = 108
    elif dib_type == 'V5':
        dib_size = 124
    offset = file_header_size + dib_size
    return int(offset)

def calcPixelArraySize(width : int, height : int, bpp : int):
    row_size = math.ceil((bpp * width)/32) * 4
    pixel_array_size = row_size * height
    return int(pixel_array_size)