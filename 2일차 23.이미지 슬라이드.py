# 버튼을 이용해서 이전 이미지, 다음 이미지로 이동하면서 이미지를 출력하는 프로그램
# 윈도우에 이미지 미리보기와 유사
from tkinter import *
from time import * #시간관련 라이브러리

# 이미지
fnameList=["jeju1.gif","jeju2.gif","jeju3.gif","jeju4.gif",
           "jeju5.gif","jeju6.gif","jeju7.gif",
           "jeju8.gif","jeju9.gif"]
# 이미지 저장 리스트
photoList = [None]*9
#현재 이미지 번호
num=0

#========함수
# 이전 이미지로 이동하는 버튼
def clickPrev():
    # 함수밖에 있는 변수를 불러오는 명령 global : 전역변수 연계
    global num  # 전역변수 num을 연결

    num -= 1  # 이전 이미지로 이동
    if num < 0:  # 유효성 검사(마지막 이미지를 벗어나면)
        num = 0  # num=0이면 더 안넘어가고 8이면 계속 넘어감

    photo = PhotoImage(file="gif/"+fnameList[num])
    pLabel.configure(image=photo) #이미지 변경
    pLabel.image= photo #메모리 상에도 이미지 변경

# 다음 이미지로 이동하는 버튼
def clickNext():
    # 함수밖에 있는 변수를 불러오는 명령 global : 전역변수 연계
    global num # 전역변수 num을 연결

    num += 1 # 다음 이미지로 이동
    if num>8: # 유효성 검사(마지막 이미지를 벗어나면)
        num = 8 #num=0 회전

    photo = PhotoImage(file="gif/"+fnameList[num])
    pLabel.configure(image=photo) #이미지 변경
    pLabel.image= photo #메모리 상에도 이미지 변경

#=======윈도우 디자인
window = Tk()
window.geometry("700x500") #창 크기
window.title("제주관광")
# 이미지 이동 버튼
btnPrev = Button(window,text="<<이전",command=clickPrev)
btnNext = Button(window,text="다음>>",command=clickNext)
# 초기 이미지
photo = PhotoImage(file="gif/"+fnameList[0])
pLabel = Label(window, image=photo)

# 배치
btnPrev.place(x=250, y=0)
btnNext.place(x=400, y=0)
pLabel.place(x=15, y=50)

window.mainloop()