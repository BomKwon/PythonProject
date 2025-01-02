#거북이 통해서 원을 그리는 프로그램
#0-purple,1-red,2-orange,3-yellow,4-green,5-blue,6-navyblue
#각 그리는 순서에 따라서 선의 색을 변경하면서 그린다.
#0~6=>가지수 7가지(배수)
import turtle

swidth, sheight = 500, 500 #창크기

#거북이 준비
turtle.title("원그리기") #제목
turtle.shape("turtle") #커서모양
turtle.setup(width=swidth+50, height=sheight+50) #창크기
turtle.screensize(swidth, sheight) #캔버스(윈도우 창내에 그래픽처리 공간)

#거북이 위치
turtle.penup()
turtle.goto(0, -sheight/2) #0,-250 (중앙 하단에 위치)
turtle.pendown()
turtle.speed(10) #거북이의 이동 속도

#원그리기
colorPoint = 0 #색상값 위치
for radius in range(7, 106): #1~99회 반복해서 그린다.
    if radius%7 ==0: #or colorPoint == 0:
        turtle.color("purple")
    elif radius%7 ==1: #or colorPoint == 1:
        turtle.color("red")
    elif radius%7 ==2: #or colorPoint == 2:
        turtle.color("orange")
    elif radius%7 ==3: #or colorPoint == 3:
        turtle.color("yellow")
    elif radius%7 ==4: #or colorPoint == 4:
        turtle.color("green")
    elif radius%7 ==5: #or colorPoint == 5:
        turtle.color("blue")
    elif radius%7 ==6: #or colorPoint == 6:
        turtle.color("pink")
    #다음 색상값 준비
    colorPoint = colorPoint + 1
    #색상 범위 값에 대한 유효성 검사(0~6번까지 생상이 존재)
    if colorPoint > 6: #색상값 범위를 벗어나면
        colorPoint = 0 #색상값은 다시 0부터 시작

    turtle.circle(radius) #반지름 1부터 100까지

turtle.done() #거북이 실행