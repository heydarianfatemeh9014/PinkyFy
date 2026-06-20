from tkinter import *
import tkinter as tk
from PIL import Image , ImageTk
from tkinter import filedialog
import shutil
import os

root = Tk()
root.title('PinkyFy')

root.geometry('2050x890')
root.config(bg ='black')


image_s = Image.open('img\\search.png')
image_s = image_s.resize((350,60))
searchimg = ImageTk.PhotoImage(image_s)
searchlbl = Label(root,bg = 'black',image = searchimg)
searchlbl.place(x = 630, y = 5)





            
    



sent = Entry(root, bg= 'white', border= False, fg = 'red',font = ('Segoe Print',14,'bold'))
sent.place(x = 637, y = 18)


main_frame_1 = tk.Frame(root,bg = '#1e1e1e',width= 400 , height = 700)
main_frame_1.place(x= 40 , y= 100)
main_frame_1.pack_propagate(False)

# def a_def():
#     files = filedialog.askopenfilenames(title = 'Select your songs', filetypes = (('mp3 files','*.mp3'),('wav files','*.wav')))
#     df = 'songs'
#     for i in files:
#         shutil.copy(i,df)
#         inf = tk.Frame(main_frame_1,bg = '#7c7c7c',width= 380 , height = 85)
#         inf.place(x= 10 , y= 70)
#         inf.pack_propagate(False)
#         inf = tk.Frame(main_frame_1,bg = '#7c7c7c',width= 380 , height = 85)
#         inf.place(x= 10 , y= 70)
#         inf.pack_propagate(False)
     
     
def c_def():
    global root2,files2,df2,filename2,covimg,namelib,files3,df3,filename3,sbtn,impbtn,nameent
    
    root2 = Toplevel()
    root2.config(bg = 'pink')
    root2.geometry('800x800')
    
    def i_def():
        global files2,df2,filename2,covimg
        files2 = filedialog.askopenfilename(title= ' Select Your Cover Photo', filetypes = (('jpg files','*.jpg'),('png files','*.png')))
        df2 = 'img'
        shutil.copy(files2,df2)
        filename2 = os.path.basename(files2)
            
        image_c = Image.open(f'img\\{filename2}')
        image_c = image_c.resize((200,200))
        covimg = ImageTk.PhotoImage(image_c)
        covimg = Label(root2)
        covimg.photo = ImageTk.PhotoImage(image_c)
        covimg.config(image=covimg.photo)
        covimg.place(x = 400, y = 150)
        
        
        # inf_list = [nameent.get(),f'img\\{filename2}']
        
        
        impbtn.place_forget()
        
    
    
    def s_def():
        global namelib,files3,df3,filename3,sbtn
        
        namelib = nameent.get()
        files3 = filedialog.askopenfilenames(title= ' Select Your Cover Photo', filetypes = (('mp3 files','*.mp3'),('wav files','*.wav')))
        df3 = f'songs\\{namelib}'
        os.makedirs(df3, exist_ok=True)
        for j in files3:
            shutil.copy(j,df3)
            filename3 = os.path.basename(j)
            
        
        
        # inf_list = [nameent.get(),f'img\\{filename2}']
        
        
        sbtn.place_forget()
        Label(root2, text = 'Songs Imported', bg = 'pink', fg = '#ff5a8f', font = ('Segoe Print', 18, 'bold')).place(x = 300 , y = 370)






    def playlist():
        with open('info.txt','r') as file:
            content = file.read()
            infolen = 0
            for i in content:
                if i =='[':
                    infolen += 1
        w1 = 380
        h1 = 100
        x1 = 10
        y1 = 80
        x2 = 10
        y2 = 10
        x3 = 95
        y3 = 10
        x4 = 95
        y4 = 40
        www = 0
        
        w = content.split('\n')
        bgg = tk.Frame(main_frame_1,bg = '#aaaaaa',width= w1 , height = h1)
        bgg.place(x= x1 , y= y1)
        bgg.pack_propagate(False)
        w0 = w[infolen].split(',')
        
        image_c3 = Image.open(f'{str(w0[2])}')
        image_c3 = image_c3.resize((80,80))
        covimg3 = ImageTk.PhotoImage(image_c3)
        covimg3 = Label(bgg)
        covimg3.photo = ImageTk.PhotoImage(image_c3)
        covimg3.config(image=covimg3.photo)
        covimg3.place(x = x2, y = y2)
        
        def show_songs_def():
            image_c4 = Image.open(f'{str(w0[www])}')
            image_c4 = image_c4.resize((200,200))
            covimg4 = ImageTk.PhotoImage(image_c4)
            covimg4 = Label(main_frame_2)
            covimg4.photo = ImageTk.PhotoImage(image_c4)
            covimg4.config(image=covimg4.photo)
            covimg4.place(x = 20, y = 20)
            Label(main_frame_2, text = w0[1], bg = '#1e1e1e', fg = 'white', font = ('Arial', 25, 'bold')).place(x = 250 , y = 50)

            
        
        Button(bgg,border = False, text = w0[1], bg = '#aaaaaa', fg = 'white', font = ('Arial', 18, 'bold'),command = show_songs_def).place(x = x3 , y = y3)
        Label(bgg, text = f'{w0[4]} Songs in this Playlist', bg = '#aaaaaa', fg = 'black', font = ('Arial', 10, 'bold')).place(x = x4 , y = y4+20)
        www+=1
        
        
        y1 += 120
            
            
            


        
        
            
            
    def sub_def():
        inf_list = [namelib,f'img\\{filename2}',f'songs\\{namelib}']
        with open('info.txt','a') as f:
            f.write(f"[,{inf_list[0]},{inf_list[1]},{inf_list[2]},{len(files3)},] \n")
        playlist()
        root2.destroy()
        

                
                
        
        
    
    
    root2.resizable(False,False)
    Label(root2, text = 'Your Library Name :', bg = 'pink', fg = '#ff5a8f', font = ('Segoe Print', 18, 'bold')).place(x = 30 , y = 30)
    nameent = Entry(root2, bg= 'white', border= False, fg = 'red',font = ('Segoe Print',18,'bold'))
    nameent.place(x = 300, y = 30)
    
    Label(root2, text = 'Your Library Cover :', bg = 'pink', fg = '#ff5a8f', font = ('Segoe Print', 18, 'bold')).place(x = 30 , y = 200)
    impbtn =Button(root2, text = 'Import',activebackground = 'pink',activeforeground='red', bg = 'pink', fg = 'red', font = ('Segoe Print', 18, 'bold'),command = i_def)
    impbtn.place(x = 300,y = 200)
    
    Label(root2, text = 'Your Library Songs :', bg = 'pink', fg = '#ff5a8f', font = ('Segoe Print', 18, 'bold')).place(x = 30 , y = 370)
    sbtn =Button(root2, text = 'Import',activebackground = 'pink',activeforeground='red', bg = 'pink', fg = 'red', font = ('Segoe Print', 18, 'bold'),command = s_def)
    sbtn.place(x = 300,y = 370)
    
    subbtn =Button(root2, text = 'Submit',activebackground = '#9cff9c',activeforeground='dark green', bg = '#9cff9c', fg = 'dark green', font = ('Segoe Print', 18, 'bold'),command = sub_def)
    subbtn.place(x = 30,y = 540)


    
    
    
    
    root2.mainloop()


Label(main_frame_1, text = 'Your Library', bg = '#1e1e1e', fg = 'white', font = ('Segoe Print', 12, 'bold')).place(x = 14 , y = 10)

main_frame_2 = tk.Frame(root,bg = '#1e1e1e',width= 700 , height = 700)
main_frame_2.place(x= 450 , y= 100)
main_frame_2.pack_propagate(False)


main_frame_3 = tk.Frame(root,bg = '#1e1e1e',width= 400 , height = 700)
main_frame_3.place(x= 1160 , y= 100)
main_frame_3.pack_propagate(False)


play_frame = tk.Frame(root,bg = '#171717',width= 1520 , height = 100)
play_frame.place(x= 40 , y= 750)
play_frame.pack_propagate(False)



c_frame = tk.Frame(main_frame_1,bg = '#ff9cbc',width= 110 , height = 35)
c_frame.place(x= 260 , y= 15)
c_frame.pack_propagate(False)

# image_c4 = Image.open('img\\pp.png')
# image_c4 = image_c4.resize((300,80))
# covimg4 = ImageTk.PhotoImage(image_c4)
# covimg4 = Label(play_frame)
# covimg4.photo = ImageTk.PhotoImage(image_c4)
# covimg4.config(bg = '#171717',image=covimg4.photo)
# covimg4.place(x =600, y = 13)

play_txt = '▶'

def playy_def():
    global play_txt
    
    if play_txt == '▶':
        play_txt = '⏸'
    else:
        play_txt = '▶'
    play_btn()


def play_btn():


    Button(play_frame, text = play_txt,border = False,activebackground = '#ff588d',activeforeground='white', bg = '#ff588d', fg = 'white', font = ('Segoe Print', 30, 'bold'),command = playy_def).place(x = 730 , y = 20,width = 60, height = 60)

Button(play_frame, text = '⏭',border = False,activebackground = '#ff81a9',activeforeground='white', bg = '#ff81a9', fg = 'white', font = ('Segoe Print', 30, 'bold'),command = playy_def).place(x = 835 , y = 25,width = 50, height = 50)
Button(play_frame, text = '⏮',border = False,activebackground = '#ff81a9',activeforeground='white', bg = '#ff81a9', fg = 'white', font = ('Segoe Print', 30, 'bold'),command = playy_def).place(x = 625 , y = 25,width = 50, height = 50)


play_btn()


Button(c_frame, text = 'Create ╋',border = False,activebackground = '#ff9cbc',activeforeground='white', bg = '#ff9cbc', fg = 'white', font = ('Segoe Print', 12, 'bold'),command = c_def).pack()




        
with open('info.txt','r') as file:
    content = file.read()
    infolen = 0
    for i in content:
        if i =='[':
            infolen += 1
w1 = 380
h1 = 100
x1 = 10
y1 = 80
x2 = 10
y2 = 10
x3 = 95
y3 = 10
x4 = 95
y4 = 40
www = 0
for j in range(infolen):
    
    w = content.split('\n')
    bgg = tk.Frame(main_frame_1,bg = '#aaaaaa',width= w1 , height = h1)
    bgg.place(x= x1 , y= y1)
    bgg.pack_propagate(False)
    w0 = w[www].split(',')
    
    image_c3 = Image.open(f'{str(w0[2])}')
    image_c3 = image_c3.resize((80,80))
    covimg3 = ImageTk.PhotoImage(image_c3)
    covimg3 = Label(bgg)
    covimg3.photo = ImageTk.PhotoImage(image_c3)
    covimg3.config(image=covimg3.photo)
    covimg3.place(x = x2, y = y2)
    
    def show_songs_def():
        image_c4 = Image.open(f'{str(w0[2])}')
        image_c4 = image_c4.resize((200,200))
        covimg4 = ImageTk.PhotoImage(image_c4)
        covimg4 = Label(main_frame_2)
        covimg4.photo = ImageTk.PhotoImage(image_c4)
        covimg4.config(image=covimg4.photo)
        covimg4.place(x = 20, y = 20)
        Label(main_frame_2, text = w0[1], bg = '#1e1e1e', fg = 'white', font = ('Arial', 25, 'bold')).place(x = 250 , y = 50)

        
    
    Button(bgg,border = 0, text = w0[1], bg = '#aaaaaa', fg = 'white', font = ('Arial', 18, 'bold'),command = show_songs_def).place(x = x3 , y = y3)
    Label(bgg, text = f'{w0[4]} Songs in this Playlist', bg = '#aaaaaa', fg = 'black', font = ('Arial', 10, 'bold')).place(x = x4 , y = y4+20)
    www+=1
    
    
    y1 += 120
    
image_c4 = Image.open('icc2.png')
image_c4 = image_c4.resize((60,60))
covimg4 = ImageTk.PhotoImage(image_c4)
covimg4 = Label(root)
covimg4.photo = ImageTk.PhotoImage(image_c4)
covimg4.config(bg = 'black',image=covimg4.photo)
covimg4.place(x =10, y = 10)
root.mainloop()