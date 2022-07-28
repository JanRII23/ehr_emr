from tkinter import *
from PIL import ImageTK, Image

root = Tk()
root.title('Using some icon')
 
# root.iconbitmap('location of the png or some image for the top left icon')

button_quit = Button(root, text="exit program", command = root.quit)
button_quit.pack()

# my_igm = ImageTk.PhotoImage(Image.open("pathway directory"))
# my_label = Label(image= my_img) #keep in mind that importing pics is a 3 step process, finding it, putting it on an object, then displaying the object
# my_label.pack()

image_list = [] #array syntax for python, keep in mind that images keep actually be stored in the array

root.mainloop()

#status bar/info can be added with labels