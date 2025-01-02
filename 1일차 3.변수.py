# 변수는 데이터형이 존재하지 않는다.

bVar = True  # 논리형 변수(True, False)
IntVar = 123  # 정수형 변수
floatVar = 3.14  # 실수형 변수
strVar = "hello world" # 문자열 변수

# 각 순서대로 변수에 값을 적용
bVar, IntVar, floatVar, strVar = True, 123, 3.14, "hello world"

IntVar1 = IntVar2 = IntVar3 = 100  # 100을 IntVar3, IntVar2, IntVar1에 적용
IntVar4, IntVar5, IntVar6 = [100]*3  # 100을 3번 반복해서 적용

print(bVar, IntVar, floatVar, strVar)