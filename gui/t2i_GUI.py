import tkinter as tk
from tkinter.filedialog import askopenfilename
from core.T2I_core import img2Txt, txt2Img

window = tk.Tk()

window.title('T2I')
window.geometry('400x500')
window.resizable(0, 0)

tk.Label(
    window,
    text='T2I',
    font=('rockwell', 30)
).pack()

tk.Label(
    window,
    text='Kernel: T2I_core\n'
         'Author: Wyatt Huang',
    font=('rockwell', 10)
).place(x=115, y=400)

mode = tk.IntVar()
imgAddr = tk.StringVar()
txtAddr = tk.StringVar()

imgAddr.set('select the image file')
txtAddr.set('select the txt file')

txtBt = tk.Label(
    window,
    textvariable=txtAddr,
).place(x=70, y=205)

imgBt = tk.Label(
    window,
    textvariable=imgAddr,
).place(x=70, y=155)


def selectFileAddrForImg():
    addr = askopenfilename()
    if mode.get() and addr.split('.')[-1].lower() != 'png':
        imgAddr.set('under img2Txt mode, file must be .png')
    elif addr.split('.')[-1].lower() != 'jpg' and addr.split('.')[-1].lower() != 'png':
        imgAddr.set('file type must be .jpg or .png')
    else:
        imgAddr.set(addr)


def selectFileAddrForTxt():
    addr = askopenfilename()
    if addr.split('.')[-1].lower() != 'txt':
        txtAddr.set('File type must be .txt')
    else:
        txtAddr.set(addr)


tk.Button(
    window,
    text='IMG',
    command=selectFileAddrForImg
).place(x=10, y=150)
tk.Button(
    window,
    text='TXT',
    command=selectFileAddrForTxt
).place(x=10, y=200)


def mode1Program():
    StartBtStatus.set('Start')
    tk.Button(
        window,
        textvariable=StartBtStatus,
        command=processing_img2txt,
        width=44,
        height=10,
        bg='grey'
    ).place(x=0, y=300)


def mode2Program():
    StartBtStatus.set('Start')
    tk.Button(
        window,
        textvariable=StartBtStatus,
        command=processing_txt2img,
        width=44,
        height=10,
        bg='grey'
    ).place(x=0, y=300)


tk.Radiobutton(
    window,
    text='Text2Img',
    value=0,
    variable=mode,
    command=mode2Program
).place(x=10, y=70)

modeTranB = tk.Radiobutton(
    window,
    text='Img2Text',
    value=1,
    variable=mode,
    command=mode1Program
).place(x=10, y=100)

StartBtStatus = tk.StringVar()
StartBtStatus.set('Start')


def processing_img2txt():
    message = img2Txt(imgAddr.get())
    open(txtAddr.get(), 'w').write(message)
    StartBtStatus.set('OK')


def processing_txt2img():
    StartBtStatus.set('Start')
    originImgName = imgAddr.get().split('/')[-1].split('.')[0]
    txt2Img(imgAddr.get(), open(txtAddr.get(), 'r').read(), originImgName + '_hideTxt.png')
    StartBtStatus.set('OK')


tk.mainloop()
