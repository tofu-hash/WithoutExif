from PIL import Image
import PIL.ExifTags


def remove_exif(file_format: str):
    image_file = open('source/service/WithoutExifImage.%s' % file_format, mode="rb")
    image = Image.open(image_file)

    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in image.getexif().items()
        if k in PIL.ExifTags.TAGS
    }

    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save('source/service/WithoutExifImage.%s' % file_format)
    return exif
