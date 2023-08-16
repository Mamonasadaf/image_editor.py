import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter, ImageEnhance, ImageGrab
from tkinter import ttk, PhotoImage
from tkinter.messagebox import showinfo, showerror, askyesno
# Image editor by Mamona Sadaf


root = tk.Tk()  # it is like a root containing all the other widgets
root.geometry("1000x670")
root.title("M-Image Editor")
root.config(bg="light blue")
icon = ImageTk.PhotoImage(file='icon.png')
root.iconphoto(False, icon)

pen_color = "black"
pen_size = 5
file_path = ""

left_frame = tk.Frame(root, width=200, height=670, bg="light blue")
left_frame.pack(side="left", fill="y")


# defining a function to import an image from the folder named below and then setting
# the canvas according to our image and hence we can perform various functions on it.
def Add_Image():
    global file_path
    file_path = filedialog.askopenfilename(
        initialdir="H:\pythonProject\image editor")
    # here add the name or location of folder where your images are saved.
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.BILINEAR)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor='nw')


def draw(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')


def Change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select the pen Colour")[1]


def change_size(size):
    global pen_size
    pen_size = size


def clear_canvas():
    canvas.delete("all")
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')


def apply_filter(filter):
    try:
        image = Image.open(file_path)
        width, height = int(image.width / 2), int(image.height / 2)
        image = image.resize((width, height), Image.BILINEAR)
        if filter == "Black and white":
            image = ImageOps.grayscale(image)
        elif filter == "Emboss":
            image = image.filter(ImageFilter.EMBOSS)
        elif filter == "Sharpen":
            image = image.filter(ImageFilter.SHARPEN)
        elif filter == "Smooth":
            image = image.filter(ImageFilter.SMOOTH)
        elif filter == "Smooth more":
            image = image.filter(ImageFilter.SMOOTH_MORE)
        elif filter == "Blur":
            image = image.filter(ImageFilter.BLUR)
        elif filter == "Contour":
            image = image.filter(ImageFilter.CONTOUR)
        elif filter == "Detail":
            image = image.filter(ImageFilter.DETAIL)
        elif filter == "Edge enhance":
            image = image.filter(ImageFilter.EDGE_ENHANCE)
        elif filter == "Edge enhance more":
            image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        elif filter == "Find edges":
            image = image.filter(ImageFilter.FIND_EDGES)

        image = ImageTk.PhotoImage(image)
        canvas.image = image
        canvas.create_image(0, 0, image=image, anchor='nw')
    except:
        showerror(title='Image Error', message='Please select an image first.!')


def apply_color(color):
    try:
        image = Image.open(file_path)
        width, height = int(image.width / 2), int(image.height / 2)
        image = image.resize((width, height), Image.BILINEAR)
        if color == "1":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(1)
        elif color == "3":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(3)
        elif color == "4":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(4)
        elif color == "5":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(5)
        elif color == "6":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(6)
        elif color == "7":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(7)
        elif color == "8":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(8)
        elif color == "9":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(9)
        elif color == "10":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(10)
        elif color == "11":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(11)
        elif color == "12":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(12)
        elif color == "13":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(13)
        elif color == "14":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(14)
        elif color == "15":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(15)
        elif color == "16":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(16)
        elif color == "17":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(17)
        elif color == "18":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(18)
        elif color == "19":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(19)
        elif color == "20":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(20)

        image = ImageTk.PhotoImage(image)
        canvas.image = image
        canvas.create_image(0, 0, image=image, anchor='nw')
    except:
        showerror(title='Image Error', message='Please select an image first!')


def apply_contrast(contrast):
    try:
        image = Image.open(file_path)
        width, height = int(image.width / 2), int(image.height / 2)
        image = image.resize((width, height), Image.BILINEAR)
        if contrast == "1":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(1)
        elif contrast == "2":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(2)
        elif contrast == "3":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(3)
        elif contrast == "4":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(4)
        elif contrast == "5":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(5)
        elif contrast == "6":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(6)
        elif contrast == "7":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(7)
        elif contrast == "8":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(8)
        elif contrast == "9":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(9)
        elif contrast == "10":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(10)
        elif contrast == "11":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(11)
        elif contrast == "12":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(12)
        elif contrast == "13":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(13)
        elif contrast == "14":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(14)
        elif contrast == "15":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(15)
        elif contrast == "16":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(16)
        elif contrast == "17":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(17)
        elif contrast == "18":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(18)
        elif contrast == "19":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(19)
        elif contrast == "20":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(20)

        image = ImageTk.PhotoImage(image)
        canvas.image = image
        canvas.create_image(0, 0, image=image, anchor='nw')
    except:
        showerror(title='Image Error', message='Please select an image first!')


def apply_brightness(bright):
    try:
        image = Image.open(file_path)
        width, height = int(image.width / 2), int(image.height / 2)
        image = image.resize((width, height), Image.BILINEAR)

        if bright == "0":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(0)
        elif bright == "1":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(1)
        elif bright == "2":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(1.2)
        elif bright == "2":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(1.3)
        elif bright == "3":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(1.5)
        elif bright == "4":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(1.7)
        elif bright == "5":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(2.0)
        elif bright == "6":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(2.3)
        elif bright == "7":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(2.5)
        elif bright == "8":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(2.7)
        elif bright == "9":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(3.0)
        elif bright == "10":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(3.3)
        elif bright == "11":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(3.5)
        elif bright == "12":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(3.7)
        elif bright == "13":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(4.0)
        elif bright == "14":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(4.5)
        elif bright == "15":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(4.7)

        image = ImageTk.PhotoImage(image)
        canvas.image = image
        canvas.create_image(0, 0, image=image, anchor='nw')
    except:
        showerror(title='Image Error', message='Please select an image first!')


def apply_sharpness(sharp):
    try:
        image = Image.open(file_path)
        width, height = int(image.width / 2), int(image.height / 2)
        image = image.resize((width, height), Image.BILINEAR)

        if sharp == "0":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(0)
        elif sharp == "1":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(10)
        elif sharp == "2":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(20)
        elif sharp == "3":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(30)
        elif sharp == "4":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(40)
        elif sharp == "5":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(50)
        elif sharp == "6":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(60)
        elif sharp == "7":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(70)
        elif sharp == "8":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(80)
        elif sharp == "9":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(90)
        elif sharp == "10":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(100)
        elif sharp == "11":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(110)
        elif sharp == "12":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(120)
        elif sharp == "13":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(130)
        elif sharp == "14":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(140)
        elif sharp == "15":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(150)
        elif sharp == "16":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(160)
        elif sharp == "17":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(170)
        elif sharp == "18":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(180)
        elif sharp == "19":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(190)
        elif sharp == "20":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(200)

        image = ImageTk.PhotoImage(image)
        canvas.image = image
        canvas.create_image(0, 0, image=image, anchor='nw')
    except:
        showerror(title=' Image Error', message='Please select an image first.!')


def flip_image():
    try:
        image = Image.open(file_path)
        width, height = int(image.width / 2), int(image.height / 2)
        image = image.resize((width, height), Image.BILINEAR)
        image = ImageOps.flip(image)
        image = ImageTk.PhotoImage(image)
        canvas.image = image
        canvas.create_image(0, 0, image=image, anchor='nw')
    except:
        showerror(title='Flip Image Error', message='Please select an image to flip!')


def mirror_image():
    try:
        image = Image.open(file_path)
        width, height = int(image.width / 2), int(image.height / 2)
        image = image.resize((width, height), Image.BILINEAR)
        image = ImageOps.mirror(image)
        image = ImageTk.PhotoImage(image)
        canvas.image = image
        canvas.create_image(0, 0, image=image, anchor='nw')
    except:
        showerror(title='Mirror Image Error', message='Please select an image to Mirror!')


def Inverting_Colors():
    try:
        image = Image.open(file_path)
        width, height = int(image.width / 2), int(image.height / 2)
        image = image.resize((width, height), Image.BILINEAR)
        image = ImageOps.invert(image)
        image = ImageTk.PhotoImage(image)
        canvas.image = image
        canvas.create_image(0, 0, image=image, anchor='nw')
    except:
        showerror(title='Inverting Pixels error', message='Please select an image first!')


def hello():
   showinfo("About me", "I am a very basic implementation of PIL and Tkinter module in python")


def save_image():
    global file_path
    if file_path:
        image = ImageGrab.grab(bbox=(
            canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + canvas.winfo_width(),
            canvas.winfo_rooty() + canvas.winfo_height()))
        filter = filter_combobox.get()
        if filter == "Black and white":
            image = ImageOps.grayscale(image)
        elif filter == "Emboss":
            image = image.filter(ImageFilter.EMBOSS)
        elif filter == "Sharpen":
            image = image.filter(ImageFilter.SHARPEN)
        elif filter == "Smooth":
            image = image.filter(ImageFilter.SMOOTH)
        elif filter == "Smooth more":
            image = image.filter(ImageFilter.SMOOTH_MORE)
        elif filter == "Blur":
            image = image.filter(ImageFilter.BLUR)
        elif filter == "Contour":
            image = image.filter(ImageFilter.CONTOUR)
        elif filter == "Detail":
            image = image.filter(ImageFilter.DETAIL)
        elif filter == "Edge enhance":
            image = image.filter(ImageFilter.EDGE_ENHANCE)
        elif filter == "Edge enhance more":
            image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        elif filter == "Find edges":
            image = image.filter(ImageFilter.FIND_EDGES)
        # Saving for color enhancer
        color = color_enhancer_combobox.get()
        if color == "1":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(1)
        elif color == "3":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(3)
        elif color == "4":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(4)
        elif color == "5":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(5)
        elif color == "6":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(6)
        elif color == "7":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(7)
        elif color == "8":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(8)
        elif color == "9":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(9)
        elif color == "10":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(10)
        elif color == "11":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(11)
        elif color == "12":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(12)
        elif color == "13":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(13)
        elif color == "14":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(14)
        elif color == "15":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(15)
        elif color == "16":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(16)
        elif color == "17":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(17)
        elif color == "18":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(18)
        elif color == "19":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(19)
        elif color == "20":
            colors_enhancer = ImageEnhance.Color(image)
            image = colors_enhancer.enhance(20)
        # Saving for contrast enhancers
        contrast = contrast_enhancer_combobox.get()
        if contrast == "1":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(1)
        elif contrast == "2":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(2)
        elif contrast == "3":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(3)
        elif contrast == "4":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(4)
        elif contrast == "5":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(5)
        elif contrast == "6":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(6)
        elif contrast == "7":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(7)
        elif contrast == "8":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(8)
        elif contrast == "9":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(9)
        elif contrast == "10":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(10)
        elif contrast == "11":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(11)
        elif contrast == "12":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(12)
        elif contrast == "13":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(13)
        elif contrast == "14":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(14)
        elif contrast == "15":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(15)
        elif contrast == "16":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(16)
        elif contrast == "17":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(17)
        elif contrast == "18":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(18)
        elif contrast == "19":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(19)
        elif contrast == "20":
            contrast_enhancers = ImageEnhance.Contrast(image)
            image = contrast_enhancers.enhance(20)
        bright = brightness_enhancer_combobox.get()
        if bright == "0":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(0)
        elif bright == "1":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(1)
        elif bright == "2":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(1.2)
        elif bright == "2":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(1.3)
        elif bright == "3":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(1.5)
        elif bright == "4":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(1.7)
        elif bright == "5":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(2.0)
        elif bright == "6":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(2.3)
        elif bright == "7":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(2.5)
        elif bright == "8":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(2.7)
        elif bright == "9":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(3.0)
        elif bright == "10":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(3.3)
        elif bright == "11":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(3.5)
        elif bright == "12":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(3.7)
        elif bright == "13":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(4.0)
        elif bright == "14":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(4.5)
        elif bright == "15":
            brightness_enhancers = ImageEnhance.Brightness(image)
            image = brightness_enhancers.enhance(4.7)
        sharp = sharpness_enhancer_combobox.get()
        if sharp == "0":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(0)
        elif sharp == "1":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(10)
        elif sharp == "2":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(20)
        elif sharp == "3":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(30)
        elif sharp == "4":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(40)
        elif sharp == "5":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(50)
        elif sharp == "6":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(60)
        elif sharp == "7":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(70)
        elif sharp == "8":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(80)
        elif sharp == "9":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(90)
        elif sharp == "10":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(100)
        elif sharp == "11":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(110)
        elif sharp == "12":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(120)
        elif sharp == "13":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(130)
        elif sharp == "14":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(140)
        elif sharp == "15":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(150)
        elif sharp == "16":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(160)
        elif sharp == "17":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(170)
        elif sharp == "18":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(180)
        elif sharp == "19":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(190)
        elif sharp == "20":
            sharpness_enhancers = ImageEnhance.Sharpness(image)
            image = sharpness_enhancers.enhance(200)
        file_path = file_path.split(".")[0] + "_" + filter.lower().replace(" ", "_") + ".jpg"
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file_path:
            if askyesno(title='Save Image', message='Do you want to save this image?'):
                # save the image to a file
                scale_factor = 2
                new_image_size = (image.size[0] * scale_factor, image.size[1] * scale_factor)
                image_resize_better = image.resize(new_image_size)
                image_resize_better.save(file_path)

    # pass


canvas = tk.Canvas(root, width=750, height=670)
canvas.pack()

image_button = tk.Button(left_frame, text="Add Image", font='chiller', command=Add_Image, bg="pink")
image_button.pack(pady=15)
color_button = tk.Button(left_frame, text="Change Color of pen", font='chiller', command=Change_color, bg="pink")
color_button.pack(pady=5)

pen_size_frame = tk.Frame(left_frame, bg='pink')
pen_size_frame.pack(pady=5)
pen_size_1 = tk.Radiobutton(pen_size_frame, text="small", value=3, command=lambda: change_size(3), bg="light blue")
pen_size_1.pack(side='left')

pen_size_2 = tk.Radiobutton(pen_size_frame, text="medium", value=5, command=lambda: change_size(5), bg="light blue")
pen_size_2.pack(side='left')
pen_size_2.select()

pen_size_3 = tk.Radiobutton(pen_size_frame, text="large", value=7, command=lambda: change_size(7), bg="light blue")
pen_size_3.pack(side='left')

pen_size_4 = tk.Radiobutton(pen_size_frame, text="extra large", value=10, command=lambda: change_size(10),
                            bg="light blue")
pen_size_4.pack(side='left')

#############################
# Clearing the canvas   #####
#############################
clear_button = tk.Button(left_frame, text="Clear", command=clear_canvas, bg="white")
clear_button.pack(pady=10)

#############################
# adding basic filters    ##
#############################

filter_label = (tk.Label(left_frame, text='Select filters', bg="light blue"))
filter_label.pack(pady=5)

filter_combobox = ttk.Combobox(left_frame, values=["Black and white", "Emboss", "Sharpen",
                                                   "Smooth", "Smooth More", "Blur", "Contour",
                                                   "Detail", "Edge enhance",
                                                   "Edge enhance more", "Find edges"])
filter_combobox.pack()
filter_combobox.bind("<<ComboboxSelected>>",
                     lambda event: apply_filter(filter_combobox.get()))

#############################
# Creating Color Enhancer ##
#############################
color_enhancer = tk.Label(left_frame, text="Apply Color Enhancer", bg="light blue")
color_enhancer.pack(pady=5)

color_enhancer_combobox = ttk.Combobox(left_frame,
                                       values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
                                               "13", "14", "15", "16", "17", "18", "19", "20"])
color_enhancer_combobox.pack()

color_enhancer_combobox.bind("<<ComboboxSelected>>",
                             lambda event: apply_color(color_enhancer_combobox.get()))

#############################
# Adding contrast Enhancer
#############################
contrast_enhancer = tk.Label(left_frame, text="Apply Contrast Enhancer", bg="light blue")
contrast_enhancer.pack(pady=5)

contrast_enhancer_combobox = ttk.Combobox(left_frame,
                                          values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
                                                  "13", "14", "15", "16", "17", "18", "19", "20"])
contrast_enhancer_combobox.pack()

contrast_enhancer_combobox.bind("<<ComboboxSelected>>",
                                lambda event: apply_contrast(contrast_enhancer_combobox.get()))

#############################
# Adding brightness Enhancer
#############################
brightness_enhancer = tk.Label(left_frame, text="Apply Luminance Enhancer", bg="light blue")
brightness_enhancer.pack(pady=5)

brightness_enhancer_combobox = ttk.Combobox(left_frame, values=["0", "1", "2", "3", "4", "5", "6", "7", "8",
                                                                "9", "10", "11", "12", "13", "14", "15"])
brightness_enhancer_combobox.pack()

brightness_enhancer_combobox.bind("<<ComboboxSelected>>",
                                  lambda event: apply_brightness(brightness_enhancer_combobox.get()))

#############################
# Adding Sharpness Enhancer
#############################
sharpness_enhancer = tk.Label(left_frame, text="Apply sharpness Enhancer", bg="light blue")
sharpness_enhancer.pack(pady=5)

sharpness_enhancer_combobox = ttk.Combobox(left_frame,
                                           values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
                                                   "13", "14", "15", "16", "17", "18", "19", "20"])
sharpness_enhancer_combobox.pack()

sharpness_enhancer_combobox.bind("<<ComboboxSelected>>",
                                 lambda event: apply_sharpness(sharpness_enhancer_combobox.get()))

#############################
# #### adding flip button  ##
#############################
flip_button = tk.Button(left_frame, text="Flip Image", command=flip_image, bg="pink")
flip_button.pack(pady=4)

#############################
# Mirroring the image  ######
#############################
mirror_button = tk.Button(left_frame, text="Mirror Image", command=mirror_image, bg="pink")
mirror_button.pack(pady=4)

### Inverting image pixels
pixel_button = tk.Button(left_frame, text="Inverting Pixels", command=Inverting_Colors, bg="pink")
pixel_button.pack(pady=4)

#### Saving image

save_button = tk.Button(left_frame, text="Save", command=save_image, bg="pink")
save_button.pack(pady=4)



B1 = tk.Button(left_frame, text = "About Me", command = hello, bg = "pink", font = "chiller")
B1.pack(pady = 30)


# Now allowing to draw on canvas after importing image i.e when we drag and can draw via this.
canvas.bind("<B1-Motion>", draw)

root.mainloop()
