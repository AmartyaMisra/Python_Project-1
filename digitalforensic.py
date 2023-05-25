from PIL import Image

# specify the path of the image file
image_path = "C:\\Users\\AMARTYA\\Downloads\\cyb.png"

# open the image file using Pillow
with Image.open(image_path) as img:
    # get the metadata of the image file
    metadata = img.info
    
# print the metadata
print(metadata)
