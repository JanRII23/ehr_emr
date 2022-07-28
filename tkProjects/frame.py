from tkinter import *


root = Tk()

root.title('MAIN')

frame = LabelFrame(root, padx = 50, pady = 50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="test")
b2.grid(row=0, column = 0)
b.grid(row=1, column = 1)

#Despite the frame being packed it can be manipulated with the grid, I belive this does not apply things other than LabelFrame

root.mainloop()