1、TKinter：Tk interface

一个简单的例子
from tkinter import  * # Import all definitions from tkinter

window = Tk()
label = Label(window ,text="Welcome to Python")
button=Button(window ,text="Click me")
label.pack()
button.pack()
window.mainloop()


import：导入类，对象，函数
from：表示来自某个模块

设置按键文字的颜色
from tkinter import  * # Import all definitions from tkinter

def processOK():
    print("Ok button is clicked!")

def processCancel():
    print(("Cancel button is clicked"))

window = Tk()
btOK=Button(window, text="OK",fg="red",command=processOK())   
btCancle=Button(window, text="Cancel",fg="yellow",command=processCancel())

btOK.pack()
btCancle.pack()

window.mainloop()
"""
command：关联一个回调函数
fg:按键文字颜色
bg:按键框颜色
"""

也可以定义一个类来实现上述功能，执行时，直接调用那个类，一般来说，推荐定义类来实现该功能，这样可以提高代码的可重用性

2、小构件类

Button  一个用来执行一条命令的简单按钮（按下可以调用一个函数）

Canvas  结构化的图形
用于绘制图形、创建图形编辑器以及实现自定制的小构件类

Checkbutton   单击复选按钮，在值之间切换

Entry 一个文本输入域，也被称为文本域或者文本框

Frame  包含其他小构件的一个容器小构件

Label  显示文本或者图形

Menu  用来实现下拉或者弹出菜单的菜单栏

Menubutton  用来实现下拉菜单的菜单按钮

Message  显示文本，与Label相似，但是它能自动地将文本放在给定的宽度或者宽高比内

Radiobutton  单击单选按钮，设置变量为指定值，同时清除所有和同一个变量相关联的其他单选按钮

Text  格式化的文本显示，允许使用不同风格和属性显示，也支持文本编辑和内嵌图片与窗口

以上小构件有许多对象选项（但是第一个参数总是：父容器）：
（1）、前景色（fg）
（2）、背景色（bg）
（3）、字体（包括字体名、大小、风格）
例如：
Times 10 bold
Helvetica 10 bold italic
CourierNew 20 bold italic
Courier 20 bold italic overstrike underline
（4）、光标风格
（5）默认下，标签或者文本都是居中的，可以使用命名常量LEFT、CENTER或者RIGHT的justify选项改变基准线
（6）可以通过cursor选项指定arrow（默认）、circle、cross、plus或者其他图形的字符串值来指定鼠标光标的特定风格

小构件类属性：fg、bg、font、cursor、text、command

例1：
        window = Tk()
        btOK = Button(window, text="OK", fg="red", bg="white",
                      command=self.processOK)
        btOK["text"] = "I OK"
        btOK["bg"] = "#AB84F6"            # 这种写法是RRGGBB的格式，（R,G,B）
        btOK["cursor"] = "circle"
        btOK["justify"] = "left"
        btCancel = Button(window, text="Cancel", fg="red", bg="white",
                      command=self.processCancel)
        btOK.pack()
        btCancel.pack()

        window.mainloop()
例2：
from tkinter import *


class WidegetsDemo:
    def __init__(self):
        window = Tk()
        window.title("Widget Demo")

        # Add a check button, and a radio button to frame1
        frame1 = Frame(window)
        frame1.pack()
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text="Bold",
                              variable=self.v1, command=self.processCheckbutton)
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text="Red", bg="red", font="Helvetica 10 bold italic",
                            variable=self.v2, value=1, cursor="plus",
                            command=self.processRadiobutton)
        rbYellow = Radiobutton(frame1, text="Yellow", bg="yellow", cursor="circle",
                            variable=self.v2, value=2,  font="Courier 10 bold italic overstrike underline",
                            command=self.processRadiobutton)
        cbtBold.grid(row=1, column=1)
        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)

        # Add a label, an entry, a button, and a message to frame2
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text="Enter your name: ", justify="left")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable=self.name)
        btGetName = Button(frame2, text="Get Name",
                           command=self.processButton)
        message = Message(frame2, text="It is a Widget Demo")
        label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btGetName.grid(row=1, column=3)
        message.grid(row=5, column=2)

        # Add text
        text = Text(window)
        text.pack()
        text.insert(END,
                    "Tip\nThe best way to learn Tkinter is t read ")
        text.insert(END,
                    "these carefully designed examples and use them ")
        text.insert(END,
                    "to creat your applications.")
        window.mainloop()

    def processCheckbutton(self):
        print("Check button is " + ("checked " if self.v1.get() == 1 else "unchecked"))

    def processRadiobutton(self):
        print(("Red " if self.v2.get() == 1 else "Yellow ") + "is selected")

    def processButton(self):
        print("Your name is" + self.name.get())


WidegetsDemo()

