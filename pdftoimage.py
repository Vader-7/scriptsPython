from pdf2image import convert_from_path
from PIL import Image
import os

poppler_path = r"/opt/homebrew/Cellar/poppler/23.03.0/bin"
pdf_folder = r"/Users/ty/Downloads/Fotos"
savingFolder = r"/Users/ty/Downloads/FotosIMG"
savingFolderRescale = r"/Users/ty/Downloads/FotosIMGRescale"

for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, pdf_file)
        pages = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)

        saving_folder = savingFolder
        c = 1

        for page in pages:
            img_name = f"{pdf_file[:-4]}-img-{c}.jpg"
            image_path = os.path.join(saving_folder, img_name)
            page.save(image_path, "JPEG", quality=50, optimize=True)
            # Load the image with PIL
            image = Image.open(image_path)
            # Check if the image is too big
            max_width = 5000  # set your maximum width here
            max_height = 5000  # set your maximum height here
            if image.width > max_width or image.height > max_height:
                # Scale down the image while maintaining the aspect ratio
                image.thumbnail((max_width, max_height), Image.ANTIALIAS)
                # Save the downscaled image
                image.save(os.path.join(savingFolderRescale, img_name), "JPEG", optimize=True)
            c += 1

print("Done")
