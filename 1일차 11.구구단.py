# 2단부터 9단까지 가로로 출력하는 프로그램
# 예) 2x1=2 3x1=3 4x1=4 ... 9x1=9

for i in range(1, 10, 1): #차순
    gugudan = "" #한 행을 처리할 변수, 1행 출력 후 초기작업
    for j in range(2, 10 ,1) : #단수
        # 1행을 작성하는 부분
        # 문자열로 누적
        gugudan += str("%2d X %2d = %2d" %(j, i, i*j))+", "
    print(gugudan)

# while문 : 불규칙한 반복처리
# 초기값
# while 조건:
#   증가값

# break: 남은 반복수와 상관없이 반복문을 종료
# continue: 현재위치에서 반복문(조건식)으로 이동