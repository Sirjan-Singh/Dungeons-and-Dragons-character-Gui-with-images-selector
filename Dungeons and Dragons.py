from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Dungeons and Dragon")
root.iconbitmap('d%d.ico')

root.geometry("417x800")

def clicked(value):
    global my_label
    my_label=Label(root,image=image_list[value]).grid(row=1, column=0, columnspan=3,rowspan=6)






image1 = ImageTk.PhotoImage(Image.open("elf.png"))
image2 = ImageTk.PhotoImage(Image.open("brute.png"))
image3 = ImageTk.PhotoImage(Image.open("Wizard.png"))
image4 = ImageTk.PhotoImage(Image.open("Knight.png"))
image5 = ImageTk.PhotoImage(Image.open("orc.png"))




image_list=[image1, image2, image3, image4, image5 ]



status=Label(root, text="Brute",bd=1,relief=RAISED).grid(row=7 ,column=0,columnspan=5,rowspan=3)


frame=LabelFrame(root, text="Character",padx=5,pady=5).grid(row=0,column=0)

my_label = Label(image=image2)
my_label.grid(row=1, column=0, columnspan=3,rowspan=6)
label1=Label(root,text="Characters",bg="black",fg="white").grid(row=0, column=4, columnspan=2,rowspan=2)






Radiobutton(root,text="Elf",value=1,command=lambda : clicked(0)).grid(column=4, row=2)
Radiobutton(root,text="Brute",value=2,command=lambda : clicked(1)).grid(column=4, row=3)
Radiobutton(root,text="Knight",value=3,command=lambda : clicked(3)).grid(column=4, row=4)
Radiobutton(root,text="Wizard",value=4,command=lambda : clicked(2)).grid(column=4, row=5)
Radiobutton(root,text="Orc",value=5,command=lambda : clicked(4)).grid(column=4, row=6)








root.mainloop()