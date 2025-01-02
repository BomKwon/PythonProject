import turtle
import random
from tkinter.simpledialog import * # 윈도우 라이브러리(대화상자 일부분)

# set~ : 받은 인수값을 저장하는 목적
# get~ : return으로 결과값을 전달
# is : 함수 내에서 if문으로 true, false의 비교 결과값 전달
# 일반적으로 동작 함수는 명사로 구성
def getAskStr(): #문자열을 입력받는 함수
    # 문자열을 변수에 저장 후 변경 없이 결과 처리할 때는 변수가 불필요
    return askstring("문자열 입력", "문자열을 입력하세요.")

def getColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r,g,b)

def getXYS(swidth, sheight):
    tX = random.randrange(int(-swidth/2),int(swidth/2))
    tY = random.randrange(int(-sheight/2), int(sheight/2))
    txtSize = random.randrange(10,50)
    return (tX,tY,txtSize)

instr = "" #입력받은 문자열을 저장할 변수
swidth, sheight = 300, 300 #윈도우 크기

tX, tY, tSize = [0]*3 #난수로 생성할 위치, 글자 크기를 저장할 변수

turtle.title("거북이 문자열 출력")
turtle.shape("turtle")
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup() #선그리기 해제

# askstring("창제목","문자열")
instr = getAskStr()

for ch in instr: #문자열을 한 글자씩 분리해서 반복
    # 작업에 필요한 값들을 난수로 구성
    tX, tY, txtSize = getXYS(swidth, sheight)
    r,g,b = getColor()

    turtle.goto(tX, tY) #출력할 위치로 거북이 이동
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=("Arial", txtSize, 'bold')) # 해당문자를 출력

turtle.done()