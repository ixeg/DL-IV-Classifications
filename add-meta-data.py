from PIL import Image
from PIL.PngImagePlugin import PngImageFile, PngInfo

filename = 'graph.png'
title = 'Title'
im = Image.open(filename)
im.load() #Needed only for .png EXIF data
print(im.info['Title'])


# targetImage = PngImageFile(filename)
# metadata = PngInfo()
# metadata.add_text("Key4", "Value")
# targetImage.save(filename,pnginfo=metadata)

# print(targetImage.text)
# print(im.info[title])
