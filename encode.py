from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import tkinter.font as tkFont
import os
from subprocess import Popen

def encode():
    main.destroy()
    enc = Tk()
    enc.geometry("800x500")
    enc.title("Encode")
    
    # Load background image
    img = ImageTk.PhotoImage(Image.open("1.jpg"))
    label1 = Label(enc, image=img)
    label1.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Create title label
    fontl = tkFont.Font(family='Algerian', size=32)
    LabelTitle = Label(text="ENCODE", bg="Blue", fg="white", width=20)
    LabelTitle['font'] = fontl
    LabelTitle.place(relx=0.5, rely=0.1, anchor=CENTER)

    # Function to open file dialog and select an image file
    def openfile():
        global fileopen
        global imagee
        fileopen = filedialog.askopenfilename(initialdir="/Desktop", title="Select file",
                                              filetypes=(("jpeg,png files", "*jpg *png"), ("all files", "*.*")))
        imagee = ImageTk.PhotoImage(Image.open(fileopen))

        Labelpath = Label(text=fileopen)
        Labelpath.place(relx=0.5, rely=0.3, anchor=CENTER)

        Labelimg = Label(image=imagee)
        Labelimg.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Create button to open file dialog
    Button2 = Button(text="Open file", command=openfile)
    Button2.place(relx=0.5, rely=0.25, anchor=CENTER)

    # Create radio buttons to select image format
    secimg = StringVar()
    radio1 = Radiobutton(text='jpeg', value='jpeg', variable=secimg)
    radio1.place(relx=0.4, rely=0.6, anchor=CENTER)

    radio2 = Radiobutton(text='png', value='png', variable=secimg)
    radio2.place(relx=0.6, rely=0.6, anchor=CENTER)

    # Create labels and entry boxes for message and file name
    Label1 = Label(text="Enter message")
    Label1.place(relx=0.4, rely=0.7, anchor=CENTER)
    entrysecmes = Entry()
    entrysecmes.place(relx=0.6, rely=0.7, anchor=CENTER)

    Label2 = Label(text="File Name")
    Label2.place(relx=0.4, rely=0.8, anchor=CENTER)
    entrysave = Entry()
    entrysave.place(relx=0.6, rely=0.8, anchor=CENTER)

    # Function to encode message in selected image file
    def encode():
                 if secimg.get() == "jpeg":
                               inimage = fileopen
                               response = messagebox.askyesno("Encode", "Do you want to encode?")
                              if response == 1:
                                  aaa.hide(inimage, entrysave.get() + '.jpg', entrysecmes.get())
                                  messagebox.showinfo("Success", "Successfully encoded " + entrysave.get() + ".jpeg")
 
                            else:
                                         messagebox.showwarning("Unsuccessful", "Encoding canceled.")

             if secimg.get() == "jpeg":
                          inimage = fileopen
                          response = messagebox.askyesno("Encode", "Do you want to encode?")
                         if response == 1:
                                     aaa.hide(inimage,entrysave.get()+'.jpg',entrysecmes.get())
                                     messagebox.showinfo("popup","successfully encode"+entrysave.get()+".jpeg")


                     else:
                                       messagebox.showwarning("popup","Unsuccessful")

	if secimg.get()=="png":
			inimage=fileopen
			response=messagebox.askyesno("popup","Do you want to encode ?")
			if response==1: 
				lsb.hide(inimage,message=entrysecmes.get()).save(entrysave.get()+'.png')
				messagebox.showinfo("popup","successfully encode to "+entrysave.get()+".png")


			else:
                            messagebox.showwarning("popup","Unsuccessful")
		


	def back():
		enc.destroy()
		#execfile('image steganography using lsb.py')
		#os.system('python imagesteganographyusinglsb.py')
		Popen('python steganography.py')

	Button2 = Button(text="ENCODE",command=encode)
	Button2.place(relx=0.7, rely=0.8, height=31, width=94)

	Buttonback = Button(text="Back",command=back)
	Buttonback.place(relx=0.7, rely=0.85, height=31, width=94)

	enc.mainloop()

