from pdf2image import convert_from_path
import os

poppler_path = r"/opt/homebrew/Cellar/poppler/23.03.0/bin"
pdf_folder = r"/Users/ty/Downloads/test"

for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, pdf_file)
        pages = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)

        saving_folder = pdf_folder
        c = 1

        for page in pages:
            img_name = f"{pdf_file[:-4]}-img-{c}.jpg"
            page.save(os.path.join(saving_folder, img_name), "JPEG")
            c += 1
