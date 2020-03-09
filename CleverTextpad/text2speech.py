from gtts import gTTS
import tkinter as tk

t2s = tk.Tk()
t2s.title("Text to Speech")

canvas1 = tk.Canvas(t2s, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(t2s, text='Text To Speech')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(t2s, text='Enter Your Text:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

label3 = tk.Label(t2s, text='Enter Your File Name:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 140, window=label3)

global entry1
entry1 = tk.Entry(t2s)
canvas1.create_window(200, 120, window=entry1)

global entry2
entry2 = tk.Entry(t2s)
canvas1.create_window(200, 160, window=entry2)


def getFile():
    from gtts import gTTS
    import tkinter as tk
    text1 = entry1.get()
    text2speech1 = gTTS(text1, lang='en')
    filename = entry2.get()
    text2speech1.save(filename + ".mp3")


button1 = tk.Button(t2s, text='Produce MP3 File', command=getFile, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 200, window=button1)

t2s.mainloop()