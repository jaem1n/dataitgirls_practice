# TDD 테스트 함수 만들기


# 합계와 평균

scores = [80, 100, 70, 90, 40]
scores2 = [20, 40, 50, 80, 90]

def total(score_list):
    total_score = 0
    for i in score_list:
        total_score += i
    return total_score

def average(score_list):
    return total(score_list)/len(score_list)

def test_total():
    assert total(scores) == 380
    assert total(scores2) == 340  # fail: 오답
    assert total(scores2) == 280  # pytest가 알려 준 답

def test_average():
    assert average(scores) == 76
    assert average(scores2) == 56  # 아무 숫자나 썼는데 정답이었어요


# 구구단

def gugudan(x):
    result = []
    for i in range(1,10):
        result.append(x*i)
    return result

def test_gugudan():
    assert gugudan(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45]
    assert gugudan(5)[2] == 10
    assert gugudan(5)[1] == 10


# 팩토리얼

def factorial(n):
    accumulator = 1
    for i in range(1, n+1):
        accumulator *= i
    return accumulator

def test_factorial():
    assert factorial(2) == 2
    assert factorial(10) == 1024
    assert factorial(10) == 3628800

