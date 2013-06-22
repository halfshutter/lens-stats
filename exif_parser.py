import PIL.Image
from PIL.ExifTags import TAGS

def get_exif_data(fname):
    "Get embedded EXIF data from image file."
    ret = {}
    try:
        img = PIL.Image.open(fname)
        if hasattr( img, '_getexif' ):
            exifinfo = img._getexif()
            if exifinfo != None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
    except IOError:
        print 'IOERROR ' + fname
    return ret

def extract_focal_length(exif_data):
    focal_length_in_35_mm = exif_data.get('FocalLengthIn35Mm')
    if focal_length_in_35_mm:
        return focal_length_in_35_mm
    values = exif_data.get('FocalLength')
    if values:
        a, b = values
        return a / b
    else:
      return None

def focal_length(fname):
    exif = get_exif_data(fname)
    return extract_focal_length(exif)