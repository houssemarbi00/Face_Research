from tkinter import *
import chlougaFace
from tkinter import filedialog as fd
import accelerate_video as av

def function():
    main=av.accelarate(function())

def function1():    
    path_video=fd.askopenfilename()
    global video
    video=str(path_video)

def function2():
    path_image=fd.askdirectory()
    global image
    image=str(path_image)

def function3():
    main=chlougaFace.main(video,image)



fenetre = Tk()
fenetre.title('face recognition')
fenetre.resizable(height=False,width=False)
photo = PhotoImage(file="D:/9raya/PROJET/Python projects/face research/face.png")
label=Label(fenetre,image=photo)
label.pack()

label_0=Label(fenetre,text="Accelerer la video de surveillance:",font=("Verdana",12,"italic bold"))
label_0.place(x="170",y="120")

label_1=Label(fenetre,text="Premierement Choisir la video de la camera de serveillance :",font=("Verdana",12,"italic bold"))
label_1.place(x="170",y="210")

label_2=Label(fenetre,text="Deuxiement Choisir le dossier qui contient la photo que vous voulez chercher:",font=("Verdana",12,"italic bold"))
label_2.place(x="170",y="300")

label_3=Label(fenetre,text="Commencer à chercher:",font=("Verdana",12,"italic bold"))
label_3.place(x="170",y="390")

boutton=Button(fenetre,text="Accelerer",command=function,bg='yellow',fg='blue')
boutton.place(x="170",y="160")

boutton1=Button(fenetre,text="Choisir une video",command=function1,bg='yellow',fg='blue')
boutton1.place(x="170",y="250")

boutton2=Button(fenetre,text="Choisir le dossier d'image",command=function2,bg='yellow',fg='blue')
boutton2.place(x="170",y="340")

boutton3=Button(fenetre,text="Commencer",command=function3,bg='yellow',fg='blue')
boutton3.place(x="170",y="430")

fenetre.mainloop()