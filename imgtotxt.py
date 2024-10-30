import cv2
import pytesseract
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
# pip install tensorflow tensorflow-hub opencv-python pytesseract Pillow

def load_image(image_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img_rgb

def preprocess_image(img_rgb):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    _, img_binary = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY)
    return img_binary

def image_to_text(image):
    text = pytesseract.image_to_string(image)
    return text

def open_file_and_process():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
    )

    if file_path:
        try:
            image = load_image(file_path)
            preprocessed_image = preprocess_image(image)

            extracted_text = image_to_text(preprocessed_image)

            messagebox.showinfo("Extracted Text", extracted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process the image. Error: {e}")

root = tk.Tk()
root.title("Image to Text Converter")

select_button = tk.Button(root, text="Select Image", command=open_file_and_process)
select_button.pack(pady=20)

root.mainloop()
