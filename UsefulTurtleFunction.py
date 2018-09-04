import turtle

# draw a line from (x1,y1) to (x2,y2)
def drawLine(x1,y1,x2,y2):
    turtle.penup()     # 将笔尖朝上，移动时不绘制
    turtle.goto(x1,y1) #将turtle移动到指定的位置
    turtle.pendown()   #将笔尖朝下，移动时绘制
    turtle.goto(x2,y2)
    turtle.hideturtle() #隐藏turtle
    turtle.done()
    
# Write a string s at specified location(x,y) 
def writeText(s,x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write(s)
    turtle.done()
    
# Draw a point at the specified location (x,y)
def drawPoint(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()   # 在绘制的图形里填充颜色
    turtle.circle(3)      
    turtle.end_fill()     # 填充图形  
    
# Draw a circle centered at (x,y) with the specified radius
def drawCircle(x=0,y=0,radius=10):
    turtle.penup()
    turtle.goto(x,y-radius)  #此处不是中心，而是起笔点
    turtle.pendown()
    turtle.circle(radius)
    
# Draw a rectangle at (x,y) with the specified width and height
def drawRectangle(x=0,y=0,width=10,height=10):
    turtle.penup()
    turtle.goto(x+width/2,y+height/2)  # 此处不是中心，而是起笔点
    turtle.pendown()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    


