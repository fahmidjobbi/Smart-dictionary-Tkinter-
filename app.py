import tkinter as tk
from PIL import Image,ImageTk
from dictTranslate import translate


root=tk.Tk()
canvas = tk.Canvas(root,width=600, height=300)
canvas.grid(columnspan=3 ,rowspan=3)

#LOGO

logo=Image.open('logo.png')
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Djobbi Dictionary DD")
instructions.grid(columnspan=3,column=0,row=1)






#input word

tk.Label(root, text="").grid(row=2)
word= tk.Entry(root)
word.grid(row=3, column=1)


def show():
   translated = translate(word.get())
   label.config(text= translated)


    
    
   

#browse button
browse_text=tk.StringVar()

browse_btn=tk.Button(root,textvariable=browse_text,command=show,font="Raleway",bg="#20bebe",fg="white",height=2,width=15)
browse_text.set("Translate")
browse_btn.grid(column=1,row=2)

label= tk.Label(root)
label.grid(column=1,row=4)

canvas = tk.Canvas(root,width=600, height=250)
canvas.grid(columnspan=3 )









root.mainloop()



