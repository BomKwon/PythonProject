# if 조건문 :
#   맞으면 처리(작업 추가)
# 공통처리
from operator import indexOf

# if 조건문 :  (흐름변경)
#   맞으면 처리
# else:
#   틀리면 처리
# 공통처리

# if 조건문 :   -> 중첩조건문(서로 다른 조건을 연속해서 물어볼 때 사용)
#   if 조건문1 :
#       맞으면 처리
#   else :
#       틀리면 처리
# else:
#   조건문이 틀리면 처리

# if 조건문 :  -> 동일한 내용으로 여러번 비교 처리할 때
#   조건문이 맞으면 처리
# elif 조건문2 :
#   (조건문은 틀리고) 조건문2가 맞으면 처리
# elif 조건문3 :
#   (조건문, 조건문2는 틀리고) 조건문3가 맞으면 처리
# else :
#   모든 조건이 틀리면 처리

a = input(input("성별을 입력하세요.(1-남자, 2-여자)"))
b = input(input("나이를 입력하세요."))
c = input(input("점수를 입력하세요."))

if a == 1:  # 남자인 경우에만 출력, 여자인 경우 아무 작업도 하지 않음
    print("입력한 성별은 남자입니다.")
else:
    print("입력한 성별은 여자입니다.")

if b>=19:  # 나이로 성인과 미성년자를 구분
    print("성인입니다.")
else:
    print("미성년자입니다.")

#       and 연산
# 남자이면서 19세 이상이면 "음주할 위험이 높음" , 그렇지 않으면 "음주할 위험이 낮음"
if a==1:  # 성별이 남자고
    if b>=19:  # 성인
        print("음주할 위험이 높습니다.")
    else:  # 미성년자
        print("음주할 위험이 낮습니다.")
else: # 여성이면
    print("대상이 아닙니다.")

if a==1 and b>=19:  # a조건에 else가 없으면 결합이 가능
    print("음주할 위험이 높습니다.")
else:
    print("음주할 위험이 낮습니다.")

if c>=90:  # 같은 값으로 여러번 비교 시 비교값이 큰 순 혹은 작은 순으로 정리해서 비교
    print("학점이 A등급입니다.")
elif c>=80:
    print("학점이 B등급입니다.")
elif c >= 70:
        print("학점이 C등급입니다.")
elif c >= 60:
    print("학점이 D등급입니다.")
else:
    print("학점이 F등급입니다.")

# if문을 연산식으로 구현 삼항식
# 변수 = 조건?참:거짓 => java, c++, c#
res = "합격" if c>=60 else "거짓"