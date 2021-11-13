from PIL import Image
from PIL.ExifTags import TAGS

#file
filename = 'graph.png'
#open img
im = Image.open(filename)
im.load() #Needed only for .png EXIF data


#extrat the exif metadata
exifdata = im.getexif()
print('here')

#loop through all the tags present in exifdata
for id in exifdata:
    # tagname = TAGS.get(tagid,tagid)
    # value = exifdata.get(tagid)
    print('here2')