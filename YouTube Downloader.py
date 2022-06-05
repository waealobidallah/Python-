import tkinter as tk
from tkinter import * # GUI مكتبية تعطيناالواجهات
#https://docs.python.org/3/library/tkinter.html
# جرب python -m tkinter
#تفاصيل  https://www.pythontutorial.net/tkinter/
#pip install Tkinter

from pytube import YouTube
# مكتبيةتحميل اليوتيوب https://pytube.io/en/latest/
#pip install pytube

#################### نتعامل مع تكينتر############
root = Tk()
message=Label(root, text="اهلا بك في تنزيل مقاطع اليوتيوب")
message.pack()

root.title("تنزيل مقاطع اليوتيوب")  # عنوان البرنامج


#root.geometry("300x300")

################# الافضل جعلها في المنتصف######
window_width = 600
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


root.resizable(1,1)# التحكم في الحجم

root.attributes('-alpha', 1) #الشفافيه 0.5 0.0 1.0 

# اضافة ايقونه اعلى اليسار من النافذه
root.iconbitmap('imam.ico')

#################################################

Label(root, text="تنزيل مقاطع اليوتيوب",
      font=("Helvetica", 15, "bold")).pack(ipadx=20, ipady=20) 

##########################################
link = StringVar()  # Variable for save link of video
filename = StringVar()  # Variable for save link of video
#######################################

Label(root, text=':ضع الرابط هنا', font=("arial",13, "bold")).place(
    x=450, y=90) 
link_enter = Entry(root, width=65, textvariable=link).place(
    x=50, y=90)  # Input for add the link

def Download():  # Function for download video

    url = YouTube(str(link.get()))

    video = url.streams.first()

    video.download()
    
    Label(root, text=' تم التنزيل', font=("arial", "20","bold"),bg="blue").place(x=100, y=150)

#زرالتنزيل
Button(root, text='تنزيل', font='arial 15 bold',command=Download).place(x=400, y=150)
# زر الخروج
Button(root,text='اخرج',command=lambda: root.quit()
,font='arial 15 bold'
).place(x=250,y=150)

root.mainloop()
