from urllib.request import urlopen
from urllib.error import *
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox

window = Tk()
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width,height))
window.title("Fake URL Detector")
window.configure(background ='red')


def getentyryvalue():
    return text_input.get()

def but_compute():
    input_path = getentyryvalue()
    try:
        html = urlopen(input_path)
     
    # except block to catch
    # exception
    # and identify error
    except HTTPError as e:
        messagebox.showinfo("HTTP error", e)
     
    except URLError as e:
        messagebox.showinfo("its fake!", e)
    except:
        messagebox.showinfo("its fake!")
    else:
        messagebox.showinfo('its real')
        

text_input = StringVar()


label = Label(window, text = "Phishing Link Detector", relief=RIDGE,width=20,font=('bold',30,'bold'),fg='black')
label.place(x=450,y=50)



entry_URL = Entry(window, text = text_input, relief=RIDGE,width=115,font=('arial',8,'normal'),bd=5,insertwidth=4,bg='white',justify='right')
entry_URL.place(x=360,y=292)

button = Button(window,text="Check_URL",font=('arial',9,'bold'),relief=RAISED,width=22,fg="Black",command=but_compute)

button.place(x=610,y=350)

window.mainloop()
