# 将彩色图片转换为灰度图片

from graphics import *


def main():
    # 创建彩色图片窗口
    win = GraphWin("Color Image", 1500, 800)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    
    # 设置提示语
    Text(Point(1, 9.5), "Enter name of image : ").draw(win)
    inputText = Entry(Point(2, 9.5), 10)   # 实体，可以接受键盘的输入
    inputText.draw(win)
    
    # 设置虚拟按键
    button = Text(Point(1.5, 8), "Show color image")
    button.draw(win)
    Rectangle(Point(1, 7.5), Point(2, 8.5)).draw(win) # 画一个矩形代表案件框

    win.getMouse()    # 单击鼠标才能继续运行（实际上返回的是鼠标单击点的坐标）

    # 获取图片名字
    imageName = inputText.getText()
    
    # 显示图片
    image1 = Image(Point(5, 5), imageName)
    image1.draw(win)
    
    # 获取图片像素矩阵的大小
    maxx = image1.getWidth()
    maxy = image1.getHeight()
    
    # 更新按键
    button.setText("Convert to greyscale")
    win.getMouse()
    win.close()

    # 设置转换按键
    for i in range(maxx):
        for j in range(maxy):
            rgb = image1.getPixel(i, j)
            r, g, b = rgb[0], rgb[1], rgb[2]

            gray = int(round(0.299*r + 0.587*g + 0.114*b)) # 将rgb图像转换为灰度图像，所谓灰度指的是亮度
            
            image1.setPixel(i, j, color_rgb(gray, gray, gray)) # 将转换好的值赋予彩色图像，使之转为灰度图像

    
    # 之所直接开一个新的的窗口，是因为我的电脑配置太差，不能一帧一帧的观察彩色图像转换为灰度图像的过程
    win1 = GraphWin("Gray image", 1500, 800)
    win1.setCoords(0.0, 0.0, 10.0, 10.0)
    image1.draw(win1)

    Text(Point(1, 9.5), "Enter name of image : ").draw(win1)
    inputText = Entry(Point(2, 9.5), 10)
    # inputText.setText("")
    inputText.draw(win1)

    button = Text(Point(1.5, 8), "Save image")
    button.draw(win1)
    Rectangle(Point(1, 7.5), Point(2, 8.5)).draw(win1)
    
    win1.getMouse()
    imageName = inputText.getText()
    image1.save(imageName)

    win1.close()

main()
