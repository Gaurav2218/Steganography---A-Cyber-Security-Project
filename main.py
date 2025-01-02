import os
from tkinter import *
from tkinter import font as tkFont
from subprocess import Popen

# Function to open Image Steganography
def open_image_steganography():
    Popen(['python', 'test.py'])  # Assuming your image steganography script is named image_steganography.py
    main.destroy()

# Function to open Audio Steganography
def open_audio_steganography():
    Popen(['python', 'audio.py'])  # Assuming your audio steganography script is named audio_steganography.py
    main.destroy()

# Main program
main = Tk()
main.title('Steganography - Image & Audio')
main.geometry("1000x750")

# Making the grid layout responsive
main.columnconfigure(0, weight=1)  # Center column configuration
main.rowconfigure([0, 1, 2, 3], weight=1)  # Configure rows for dynamic resizing

# Font settings for the buttons
fontl = tkFont.Font(family='Algerian', size=20)

# Button for Image Steganography
img_button = Button(main, text='Image Steganography', fg="white", bg="blue", width=20, command=open_image_steganography)
img_button['font'] = fontl
img_button.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

# Button for Audio Steganography
audio_button = Button(main, text='Audio Steganography', fg="white", bg="green", width=20, command=open_audio_steganography)
audio_button['font'] = fontl
audio_button.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

# Exit button
def exit():
    main.destroy()

exit_button = Button(main, text='EXIT', fg="white", bg="red", width=20, command=exit)
exit_button['font'] = fontl
exit_button.grid(row=2, column=0, padx=20, pady=20, sticky='nsew')

main.mainloop()
