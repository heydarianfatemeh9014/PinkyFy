# from tkinter import *

# root = Tk()

# # توابع دکمه‌ها
# def btn1():
#     print("دکمه اول")

# def btn2():
#     print("دکمه دوم")

# def btn3():
#     print("دکمه سوم")

# # لیست متن دکمه‌ها و تابعشان
# buttons = [
#     ("دکمه 1", btn1),
#     ("دکمه 2", btn2),
#     ("دکمه 3", btn3)
# ]

# # ساخت همه دکمه‌ها
# for text, func in buttons:
#     Button(root, text=text, command=func).pack()

# root.mainloop()
import ast
with open('info.txt','r') as file:
    content = file.read()
    content = list(content.split('\n'))
    content = [ast.literal_eval(item) for item in content]

   

playlistnum =[]
for m in range(len(content)):
    playlistnum.append(tuple(content[m]))
    
    
print(type(content[1]),'\n\n\n',len(content))