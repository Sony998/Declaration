import webbrowser
import time
import wget
from tkinter import * 
from PIL import Image, ImageTk
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


window = Tk()


window.geometry("1000x500")

window.title("Programa bonito :3 ")

imagen = "https://i.pinimg.com/474x/4c/9c/b8/4c9cb8eca9fa923e5ea14df8b409c890.jpg" 

wget.download(imagen, 'imagen1.jpg')

imagen = ImageTk.PhotoImage(Image.open('imagen1.jpg').resize((150, 150)))

imagen2 = "https://i.pinimg.com/originals/da/b5/5d/dab55da941de88a48115f47f99afd181.png"
wget.download(imagen2, 'apenado.png')

imagen2 = ImageTk.PhotoImage(Image.open('apenado.png').resize((150, 150)))

imagen3 = "https://i.pinimg.com/474x/d8/58/46/d8584639afbe059e1eb0d1988c7696e0.jpg"
wget.download(imagen3, 'tirste.jpg')

imagen3 = ImageTk.PhotoImage(Image.open('tirste.jpg').resize((150, 150)))

imagen4 = "https://pbs.twimg.com/media/Eio1KjeWsAItnuM.png"
wget.download(imagen4, 'triste2.png')

imagen4 = ImageTk.PhotoImage(Image.open('triste2.png').resize((150, 150)))

imagen5 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBQ8iZuBjgVTR1M11uz--LO8qrazfSRKk_pw&usqp=CAU"
wget.download(imagen5, 'casar.png')

imagen5 = ImageTk.PhotoImage(Image.open('casar.png').resize((150, 150)))

imagen6 = "https://freepngimg.com/thumb/emoji/104165-angry-emoji-free-photo.png"
wget.download(imagen6, 'obligar.png')

imagen6 = ImageTk.PhotoImage(Image.open('obligar.png').resize((150, 150)))

imagen7 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdg1zBtkRtUqXuWjmDmqLPqZLy0_XAh5MsTg&usqp=CAU"
wget.download(imagen7, 'losabia.png')

imagen7 = ImageTk.PhotoImage(Image.open('losabia.png').resize((150, 150)))

imagen8 = "https://i.pinimg.com/474x/4b/5b/b5/4b5bb5a1deea63b514f6bcbd282ed217.jpg"
wget.download(imagen8, 'byebye.jpg')

imagen8 = ImageTk.PhotoImage(Image.open('byebye.jpg').resize((150, 150)))

imagen9 = "https://i.pinimg.com/originals/64/d5/eb/64d5eb2d3b5ae1fc097bee614883c3f9.jpg"

wget.download(imagen9, 'beso.jpg')
imagen9 =  ImageTk.PhotoImage(Image.open('beso.jpg').resize((300, 138)))

lb1 = Label(image=imagen)
lb1.place(x=390, y=150)

#lb1 = Label(window, text="Hello")
lb2 = Label(window, text= "Hola Peciosota, te saluda tu bonito novio :3", font=("Times New Roman", 28, "bold"))
lb2.place(x=170, y=40)


#Cambio de mensaje al dar click
def clicked():
    lb2.configure (text= "Ya se que toy bonito :3, gracias por recordarmelo ")  
    lb1.configure (image=imagen2)
    lb2.place(x=75, y=40)  
    btn1.configure(text="teamo", command=clickod)

#Boton1
btn1 = Button(window, text="hola bonito novio ",  font=("Calibri", 19, "bold", ), bg="red", command=clicked , bd=10 )
btn1.place(x=250, y=390, width=500, height=50)

def clickod():
    btn1.configure(text="ta bien no dire mas mentiras", command=clickud)
    lb1.configure(image=imagen3)
    lb2.configure(text= "No me digas tales mentirotas :(")


def clickud():
    lb1.configure(image=imagen4)
    lb2.configure(text= "Eso, mucho mejor o bueno ni tan mejor :(")
    btn1.configure(text= "no seas mensote cadadebola", command=clickid)

def clickid():
    lb1.configure(image=imagen5)
    lb2.configure(text= "Ves como eres de gosera? en fin... te quieres casar con yo?")
    btn1.configure(text= "noquiero", command=clickin)

def clickin():
    lb1.configure(image=imagen6)
    lb2.configure(text= "Pues te obligo ")
    btn1.configure(text= "bueno asi si quiero D:", command=clickon)

def clickon():
    lb1.configure(image=imagen7)
    lb2.configure(text= "Sabia que ibas a querer, no ves lo bonito que nos vemos juntos? ", font=("Times New Roman", 20 , "bold") )
    btn1.configure(text= "nones no lo veo pero quiero ver ", command=openbrow)

def openbrow():
    webbrowser.open('https://drive.google.com/drive/folders/1B2xU7My-aR7zKy1tBvRIdVf01hWJSFXI?usp=sharing')
    time.sleep(6)
    lb1.configure(image=imagen8)
    lb2.configure(text= "viste que bonitos?")
    btn1.configure(text= "chines, que lindos", command=ultimotevamos)

def ultimotevamos():
    lb1.configure(image=imagen9)
    lb2.configure(text= "gracias por tu atencion :3 ")
    btn1.configure(text="nomecaesbien tontote", command=cerrar)

def cerrar():
    window.destroy()


window.mainloop()