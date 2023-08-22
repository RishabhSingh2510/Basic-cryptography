import tkinter
import cip

window = tkinter.Tk()
window.title(' Cipher')
window.geometry('400x250')

l1 = tkinter.Label(window, text="Your Text")
l1.pack()

edit_text = tkinter.Text(window, height=10, width=100)
edit_text.pack(pady=10)

frame = tkinter.Frame(window)
frame.pack()

def encypt_command():
    text = edit_text.get("1.0", tkinter.END)

    with open(cip.file_path, 'w') as f:
        f.write(text.strip())

    cipher = cip.encryption()

    edit_text.delete("1.0", tkinter.END)
    edit_text.insert(tkinter.INSERT, cipher)

def decrypt_command():
    text = edit_text.get("1.0", tkinter.END)

    with open(cip.file_path, 'w') as f:
        f.write(text.strip())

    text = cip.decryption()

    edit_text.delete("1.0", tkinter.END)
    edit_text.insert(tkinter.INSERT, text)

enc_btn = tkinter.Button(frame, text="Encrypt", command=encypt_command)
enc_btn.pack(side=tkinter.LEFT, padx=10)

dec_btn = tkinter.Button(frame, text="Decrypt", command=decrypt_command)
dec_btn.pack(side=tkinter.RIGHT, padx=10)

window.mainloop()