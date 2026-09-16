"""
초급 Python 빈칸 연습: 짝수의 합 구하기

목표: 리스트, 변수, for 반복문, if 조건문을 연습합니다.
아래의 ___ 네 곳을 알맞은 코드로 바꾸세요.
각 빈칸 바로 위 주석에 정답과 설명이 있습니다.

실행: python python_basics_fill_blanks.py
예상 출력: 짝수의 합: 6
참고: 빈칸을 채우기 전에는 오류가 발생하는 것이 정상입니다.
"""

# 리스트에 합계를 구할 숫자들을 저장합니다.
numbers = [1, 2, 3, 4, 5]
# 빈칸 1 정답: 0 — 아직 더한 숫자가 없으므로 합계를 0으로 시작합니다.
#total = ___
total = 0

# 빈칸 2 정답: numbers — 리스트의 숫자를 하나씩 꺼내 number에 넣습니다.
#for number in ___:
for number in numbers :
    # 빈칸 3 정답: 0 — %는 나머지 연산자이며, 2로 나눈 나머지가 0이면 짝수입니다.
    # if number % 2 == ___:
    if number % 2 == 0 :
        total = total + number
        # 빈칸 4 정답: number — 현재 짝수를 합계에 더하고 그 결과를 total에 저장합니다.
        # total = total + ___

# 빈칸을 올바르게 채우면 2와 4를 더한 결과인 6이 출력됩니다.
print("짝수의 합:", total)
