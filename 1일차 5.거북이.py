#라이브러리 추가
import turtle #거북이를 이용한 그래픽 라이브러리
import random #난수를 만드는 라이브러리

#전역변수
#폭 300x높이 300 윈도우, 펜 굵기 3, 종료할 수
swidth, sheight, pSize, extiCount = 300, 300, 3, 0

#라이브러리는 해당 라이브러리에 함수 사용법을 익힌다.
#함수를 이용해서 프로그램
turtle.title("창제목") #창 제목
turtle.shape("turtle") #커서 모양
turtle.screensize(swidth, sheight) #작업지 크기
turtle.setup(width=swidth+30, height=sheight+30) #창 크기
turtle.pencolor("red") #펜 색상
turtle.pensize(pSize)  #펜 굵기

#이동 forward(거리) : 앞으로 전진, left/right(각도) : 회전
#backward(거리) : 뒤로 후진, circle(반지름) : dnjsrmflrl
#penup() : 펜 올리기, pendown() : 펜 내리기(이동시 그리기)
#xcor/ycor : 거북이의 x와 y의 좌표

while True: #반복문 조건(True)-무한반복
    #펜 색상을 난수로 구하기
    r = random.random() #빛의 3원색(0 검은색 -> 255 흰색)
    g = random.random()
    b = random.random()
    turtle.pencolor((r,g,b)) #3원색으로 펜 색을 지정

    #거북이가 이동할 방향(0~360도)
    angle = random.randrange(0, 360) #0~360도 사이의 난수를 구한다.
    #거북이의 이동거리(0~100)
    dist = random.randrange(1, 100)

    turtle.left(angle)
    turtle.forward(dist)

    #현재 거북이의 위치값
    curX = turtle.xcor()
    curY = turtle.ycor()

    #제약조건(거북이 창 밖으로 벗어났을 때)
    #300x300=>-150~150범위
    #거북이가 가로폭 안에 들어가 있으면
    if(-swidth/2<=curX and curX<=swidth/2)\
        and (-sheight/2<=curY and curY<=sheight/2):
        pass #거북이가 윈도우 창내에 존재하면 변경내용 없음
    else: #거북이가 창을 벗어나면 가운데로 이동
        turtle.penup() #펜을 올리기(거북이 이동시 그림을 그리지 않는다._
        turtle.goto(0,0) #거북이를 중앙에 이동시킨다.
        turtle.pendown() #펜을 내린다(그림 그릴 준비)

    extiCount += 1 #카우터를 증가
    if extiCount >= 100: #그리기를 100회 진행 후 종료
        break #while 종료

turtle.done() #설정 종료 후 실행
