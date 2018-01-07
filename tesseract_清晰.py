from PIL import Image
import subprocess

def clean_file(file_path, new_filepath):
    image = Image.open(file_path)

    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(new_filepath)

    subprocess.call(["tesseract", new_filepath, "output"])

    file = open("output.txt", "r")
    print(file.read())
    file.close()
clean_file("test2.png","test2clean.png")
