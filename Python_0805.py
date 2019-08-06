# score가 다음과 같은 형태로 주어졌을 때
scores = [80, 100, 70, 90, 40]

# 1. total 함수 만들기
def total(x):
    t = 0
    for i in x:
        t += i
    return t

# 2. average 함수 만들기
def average(x):
    return total(x)/len(x)

# 3. 제대로 했는지 확인하기
print(total(scores))
print(average(scores))

# 4. 코드를 Github에 올리기