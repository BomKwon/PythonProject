# 레이블 객체
# 윈도우 창 내에 문자열을 출력
# 객체는 위에서 아래로 순서대로 출력
# 객체 생성후 윈도우 창에 배치

from tkinter import *

window = Tk()
# 윈도우 환경을 구성
#label(부모창, text="출력할 문자열", bg="배경색", width="폭", height="높이")
#text = "문자열"
# bg =
label1 = Label(window, text="Hello World")

window.mainloop()