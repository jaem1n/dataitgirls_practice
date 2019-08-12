class_scores = [
    {
        '국어': 80,
        '영어': 100,
        '수학': 50
    },
    {
        '국어': 90,
        '영어': 70,
        '수학': 40
    }
]


# 1) 두 개의 dictionary에서 국어 점수의 총 합은?
# => assert class_total(class_scores, '국어') == 170
# 이렇게 확인할 수 있는 함수를 만들어보세요

def class_total(scores, subject):
    score = 0
    for i in range(0,len(scores)):
        score += scores[i][subject]
    return score

def test_class_total():
    assert class_total(class_scores, '국어') == 170


# 2) class_scores set에 있는 모든 점수의 합은 얼마인가요? 역시 함수를 만들어보세요
# => assert class_total_all(class_scores) == 430

def class_total_all(scores):
    score = 0
    for i in range(0, len(scores)):
        score += sum(scores[i].values())
    return score

def test_class_total_all():
    assert class_total_all(class_scores) == 430
