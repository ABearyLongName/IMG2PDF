from PIL import Image
import os, fnmatch
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


file_path = tk.filedialog.askdirectory(title="Select folder to convert to PDF")

files = fnmatch.filter(os.listdir(file_path), "*.jpg") + fnmatch.filter(os.listdir(file_path), "*.jpeg") + fnmatch.filter(os.listdir(file_path), "*.png")


images = [
    Image.open(file_path + "/" + f)
    for f in files
]

pdf_path = file_path + "/imagestopdf.pdf"

images[0].save(
    pdf_path, "PDF", resolution = 100.0, save_all = True, append_images = images[1:]
)