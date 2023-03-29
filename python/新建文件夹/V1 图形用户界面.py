#〇、模块导入
import tkinter,cv2,numpy
from PIL import Image, ImageTk

#一、定义函数（用于识别半径）
def radius():
    name=str(inp1.get()+'.bmp')
    Rmin=int(inp2.get())
    Rmax=int(inp3.get())
    p1=int(inp4.get())
    p2=int(inp5.get())
    txt.delete(0.0,'end')  #获取五个参数并清空输出框

    img=Image.open(inp1.get()+'.bmp')
    img=img.resize((320,256))
    photo=ImageTk.PhotoImage(img)  #读取图片并进行初步处理
    lb6.config(image=photo)
    lb6.image=photo                #在lb6中显示图片（预览）
    
    img=cv2.imread(name)
    result=cv2.blur(img,(5,5))   #将图片模糊处理
    gray=cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)   #灰度化处理
    circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,50,param1=p1,param2=p2,minRadius=Rmin,maxRadius=Rmax)   #读取半径

    try:    
        for circle in circles[0]:
            #圆的基本信息
            txt.insert('end',str(circle[2])+'\n')
            #坐标行列(就是圆心)
            x=int(circle[0])
            y=int(circle[1])
            #半径
            r=int(circle[2])
            #在原图用指定颜色圈出圆，参数设定为int所以圈画存在误差
            img=cv2.circle(img,(x,y),r,(0,0,255),1,8,0)
            font=cv2.FONT_HERSHEY_SIMPLEX
            img=cv2.putText(img,str(circle[2]),(x,y),font,1.2,(255,255,255),2)

        #显示新图像
        img=cv2.resize(img,(640,512))
        cv2.imshow('5',img)

    except:
        font=cv2.FONT_HERSHEY_SIMPLEX
        img=cv2.putText(img,'Failed to detect circles',(200,200),font,1.2,(255,255,255),2)
        img=cv2.resize(img,(640,512))
        cv2.imshow('5',img)

#二、窗口建立
root=tkinter.Tk()
root.title('圆半径读取')
root.geometry('720x360')


#三、控件的建立和摆放
font1=('华文仿宋',14)

txt=tkinter.Text(root,font=font1)
txt.place(relx=0.05,rely=0.5,relwidth=0.4,relheight=0.3)

lb1=tkinter.Label(root,text='文件名')
inp1=tkinter.Entry(root,font=font1)
inp1.insert('end','1')
lb1.place(relx=0.05,rely=0.095,relwidth=0.1,relheight=0.08)
inp1.place(relx=0.05,rely=0.15,relwidth=0.1,relheight=0.06)

lb2=tkinter.Label(root,text='Rmin')
inp2=tkinter.Entry(root,font=font1)
inp2.insert('end','30')
lb2.place(relx=0.2,rely=0.095,relwidth=0.1,relheight=0.08)
inp2.place(relx=0.2,rely=0.15,relwidth=0.1,relheight=0.06)

lb3=tkinter.Label(root,text='Rmax')
inp3=tkinter.Entry(root,font=font1)
inp3.insert('end','300')
lb3.place(relx=0.35,rely=0.095,relwidth=0.1,relheight=0.08)
inp3.place(relx=0.35,rely=0.15,relwidth=0.1,relheight=0.06)

lb4=tkinter.Label(root,text='param1')
inp4=tkinter.Entry(root,font=font1)
inp4.insert('end','80')
lb4.place(relx=0.05,rely=0.25,relwidth=0.1,relheight=0.08)
inp4.place(relx=0.05,rely=0.305,relwidth=0.1,relheight=0.06)

lb5=tkinter.Label(root,text='param2')
inp5=tkinter.Entry(root,font=font1)
inp5.insert('end','30')
lb5.place(relx=0.2,rely=0.25,relwidth=0.1,relheight=0.08)
inp5.place(relx=0.2,rely=0.305,relwidth=0.1,relheight=0.06)

btn=tkinter.Button(root,text='求半径',font=font1,command=radius)
btn.place(relx=0.35,rely=0.25,relwidth=0.1,relheight=0.08)

img=Image.open(str(inp1.get())+'.bmp')
img=img.resize((320,256))
photo=ImageTk.PhotoImage(img)
lb6=tkinter.Label(root,image=photo)
lb6.place(relx=0.5,rely=0.1)  

root.mainloop()
