from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Ronoks Image Viewer')
root.iconbitmap('C:/Users/Ronok Arya/Downloads/cal2.ico')

def open():
    global my_image
    root.filename = filedialog.askopenfilename(intitialdir="/gui/images", title="Select A File", filetype=((
    "png files", "*.png"),("all files", "*.*")))
    mylabel = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image+my_image).pack()

my_btn = Button(root, text="Open File", command = open).pack()

root.mainloop()