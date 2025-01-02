from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter import font as tkFont
from pydub import AudioSegment
import numpy as np
import wave
import os
from subprocess import Popen

def encode_audio():
    main.destroy()
    enc = Tk()
    enc.title("Audio Steganography - Encode")
    enc.geometry("800x600")  # Set a larger window size
    
    fontl = tkFont.Font(family='Algerian', size=32)
    
    LabelTitle = Label(enc, text="ENCODE AUDIO", bg="Blue", fg="white")
    LabelTitle['font'] = fontl
    LabelTitle.pack(pady=20)  # Use pack with padding for better layout

    frame = Frame(enc)  # Create a frame to hold content
    frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

    def openfile():
        global fileopen
        fileopen = askopenfilename(title="Select Audio File", filetypes=(("Wav files", "*.wav"), ("All files", "*.*")))
        Labelpath.config(text=fileopen)

    Button2 = Button(frame, text="Open Audio File", command=openfile)
    Button2.grid(row=0, column=0, padx=10, pady=10)

    Labelpath = Label(frame, text="No file selected")
    Labelpath.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    Label1 = Label(frame, text="Enter Message")
    Label1.grid(row=1, column=0, padx=10, pady=10)

    entrysecmes = Entry(frame, width=40)
    entrysecmes.grid(row=1, column=1, padx=10, pady=10)

    Label2 = Label(frame, text="File Name to Save")
    Label2.grid(row=2, column=0, padx=10, pady=10)

    entrysave = Entry(frame, width=40)
    entrysave.grid(row=2, column=1, padx=10, pady=10)

    def encode():
        audio = wave.open(fileopen, mode='rb')
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
        message = entrysecmes.get() + int((len(frame_bytes) - len(entrysecmes.get()) * 8 * 8) / 8) * '#'
        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in message])))
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit
        frame_modified = bytes(frame_bytes)
        
        with wave.open(entrysave.get() + '.wav', 'wb') as fd:
            fd.setparams(audio.getparams())
            fd.writeframes(frame_modified)
        audio.close()
        messagebox.showinfo("Popup", "Successfully Encoded to " + entrysave.get() + ".wav")

    Button3 = Button(frame, text="ENCODE", command=encode)
    Button3.grid(row=3, column=1, padx=10, pady=20, sticky=E)

    def back():
        enc.destroy()
        Popen('python audio_steganography.py')

    Buttonback = Button(frame, text="Back", command=back)
    Buttonback.grid(row=3, column=0, padx=10, pady=20)

    enc.mainloop()


def decode_audio():
    main.destroy()
    dec = Tk()
    dec.title("Audio Steganography - Decode")
    dec.geometry("800x600")  # Set a larger window size
    
    fontl = tkFont.Font(family='Algerian', size=32)
    
    LabelTitle = Label(dec, text="DECODE AUDIO", bg="Blue", fg="white")
    LabelTitle['font'] = fontl
    LabelTitle.pack(pady=20)

    frame = Frame(dec)
    frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

    def openfile():
        global fileopen
        fileopen = askopenfilename(title="Select Audio File", filetypes=(("Wav files", "*.wav"), ("All files", "*.*")))
        Labelpath.config(text=fileopen)

    Button2 = Button(frame, text="Open Audio File", command=openfile)
    Button2.grid(row=0, column=0, padx=10, pady=10)

    Labelpath = Label(frame, text="No file selected")
    Labelpath.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    def decode():
        audio = wave.open(fileopen, mode='rb')
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        message = "".join(chr(int("".join(map(str, extracted[i:i + 8])), 2)) for i in range(0, len(extracted), 8))
        decoded_message = message.split("###")[0]
        audio.close()

        Label2.config(text="Decoded Message: " + decoded_message)

    Button3 = Button(frame, text="DECODE", command=decode)
    Button3.grid(row=1, column=0, padx=10, pady=20)

    Label2 = Label(frame, text="")
    Label2.grid(row=1, column=1, padx=10, pady=10, sticky=W)

    def back():
        dec.destroy()
        Popen('python audio_steganography.py')

    Buttonback = Button(frame, text="Back", command=back)
    Buttonback.grid(row=2, column=0, padx=10, pady=20)

    dec.mainloop()


# Main program
main = Tk()
main.title('Audio Steganography - ENCODE & DECODE')
main.geometry("1000x750")

fontl = tkFont.Font(family='Algerian', size=20)

encbutton = Button(main, text='Encode Audio', fg="white", bg="black", width=20, command=encode_audio)
encbutton['font'] = fontl
encbutton.pack(pady=40)

decbutton = Button(main, text='Decode Audio', fg="white", bg="black", width=20, command=decode_audio)
decbutton['font'] = fontl
decbutton.pack(pady=40)

def exit():
    main.destroy()

closebutton = Button(main, text='EXIT', fg="white", bg="red", width=20, command=exit)
closebutton['font'] = fontl
closebutton.pack(pady=40)

main.mainloop()
