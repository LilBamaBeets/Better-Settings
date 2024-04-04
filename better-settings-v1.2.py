import os
import subprocess
from time import sleep
import tkinter as tk
import ctypes

def exp():
    os.startfile("C:\\Windows\\explorer.exe")

def james():
    
    penius = tk.Tk()
    penius.title('silly moment')
    penius.resizable(False, False)
    penius.geometry("720x72+600+180")
    penius.config(bg="#121212")
    woahitsmemario = tk.Label(
        text="you idiot",
        font=("Montserrat Black", 12),
        fg="#ffffff",
        bg="#1e1e1e",
        width=720,
        height=72,
        master=penius
    )
    woahitsmemario.pack()
    sleep(2)
    os.system("taskkill /im explorer.exe /F")
    penius.mainloop()
    
    

def weee():
    #os.system("start \"\" https://amphe.co.uk")
    command = ['reg.exe', 'add', 'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize', 
           '/v', 'AppsUseLightTheme', '/t', 'REG_DWORD', '/d', '0', '/f']
    subprocess.run(command)
    
    


def exi():
    exit()

window = tk.Tk()
window.title('Better Settings v1.1')
window.resizable(False, False)
window.geometry("720x720+600+180")
window.config(bg="#121212")
label = tk.Label(

    bg="#1e1e1e",
    width=85,
    height=45
)
button = tk.Button(
    text="Dark Mode",
    font=("Montserrat Black", 12),
    width=25,
    height=5,
    bg="#BB86FC",
    fg="#FFFFFF",
    border=0,
    command=weee
)
exite=tk.Button(
        text="Exit",
         font=("Montserrat Black", 12),
        width=9,
        height=3,
        bg="#BB86FC",
        fg="#FFFFFF",
        border=0,
        command=exi
    )
exite.place(x=65,y=600)

superexit=tk.Button(
        text="Admin Unlock",
         font=("Montserrat Black", 12),
        width=25,
        height=3,
        bg="#BB86FC",
        fg="#FFFFFF",
        border=0,
        command=james
    )
superexit.place(x=65,y=235)

inv=tk.Button(
        width=25,
        height=5,
        bg="#1e1e1e",
        fg="#FFFFFF",
        border=0,
        command=exp
    )
inv.place(x=200,y=600)

button.place(x=65,y=90)
label.place(x=50,y=25)
window.mainloop()
