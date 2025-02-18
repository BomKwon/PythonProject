#윤년은 1년을 계산시 남는 시간을 모아서 하루로 처리
#2월을 +1
#100으로 나눠 떨어지고 400으로 나누어서 떨어지지 않으면 평년
#4의 배수 : 4, 8, 12, 16
#계산법
#4로 나누어 떨어지고, 100으로 나누어서 떨어지지 않으면 평년
#400으로 나누어 떨어지는 해도 윤년

#입력
year = int(input("원하는 년도를 입력하세여"))

#처리
sw = True #스위치 기법(가상의 결과를 미리 지정-윤년)

#유효성검사(결정한 결과가 맞는지 확인)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    sw = True #윤년
else:
    sw = False #평년

# 출력
if sw == True:
    print("해당 년도는 윤년입니다.")
else:
    print("해당 년도는 평년입니다.")
