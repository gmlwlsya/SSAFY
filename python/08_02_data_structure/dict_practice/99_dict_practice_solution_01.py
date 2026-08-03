# =============================================================
# [실습 1 해설] 혈액형 인원수 세기
# - 같은 문제를 3가지 방법으로 해결
# - 아래로 내려갈수록 '키가 있는지 확인하는 코드'가 줄어드는 것에 주목
#
# =============================================================

# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']
"""
실행 결과
{'A': 4, 'B': 3, 'O': 3, 'AB': 2}
"""


# =============================================================
# [해설 1] [] 표기법 - 존재 여부를 직접 확인
# - 핵심 고민: 처음 등장하는 혈액형은 딕셔너리에 키가 없는 상태
#             => 곧바로 += 1을 하면 KeyError
#             => 키가 이미 있는 경우와 없는 경우를 나눠서 처리해야 함
#
# - 처음 등장하는 혈액형은 키가 없으므로 곧바로 += 1을 할 수 없음
#   (KeyError 발생) => if로 두 경우를 나눠 처리
#     이미 있으면  : 기존 값에 +1
#     처음 나오면  : 1로 시작 (0이 아님에 주의)
# - 가장 길지만, 무슨 일이 일어나는지 가장 명확하게 보임
# =============================================================


# 1. [] 표기법을 사용한 방법
def count_blood_types_01(blood_types):
    blood_count_bracket = {}
    for blood in blood_types:
        if blood in blood_count_bracket:
            blood_count_bracket[blood] += 1
        else:
            blood_count_bracket[blood] = 1
    return blood_count_bracket


# =============================================================
# [해설 2] get() - if문을 없앤 방법
# - 핵심 고민: '없으면 0을 가져온다'고 생각하면 if문이 필요 없어짐
#             => 가져온 값에 1을 더해 다시 저장하면 끝
#
# - get(blood, 0)은 "있으면 그 값, 없으면 0"을 돌려줌
#   => 처음 등장하는 혈액형도 0을 받아오므로 +1을 해서 1이 됨
#   => 결국 두 경우를 하나의 식으로 통합할 수 있음
# - 반복문 안이 한 줄로 정리됨
# =============================================================


# 2. get() 메서드를 사용한 방법
def count_blood_types_02(blood_types):
    blood_count_bracket = {}

    for blood in blood_types:
        blood_count_bracket[blood] = blood_count_bracket.get(blood, 0) + 1

    return blood_count_bracket


# =============================================================
# [해설 3] defaultdict - 기본값 설정 자체를 딕셔너리에 맡김
# - 핵심 고민: 이제 존재 여부를 신경 쓸 필요가 전혀 없음
#             => 반복문 안이 += 1 한 줄로 끝남
#
# - get()은 '조회할 때마다' 기본값 0을 적어줘야 하지만,
#   defaultdict는 '만들 때 한 번만' 설정하면 됨
#   => 반복문 안이 += 1 한 줄로 끝남
# - dict()로 변환해 반환하는 이유
#   defaultdict 그대로 반환하면 출력이
#   defaultdict(<class 'int'>, {...}) 형태로 나오기 때문
#   (기능상 문제는 없으나 기대한 출력과 다르게 보임)
# =============================================================

# 3. defaultdict를 사용한 방법
# (키가 없을 때 자동으로 0으로 초기화해주므로 로직이 단순해짐)
from collections import defaultdict


def count_blood_types_03(blood_types):
    # int() 함수는 실행 시 0을 반환하므로, 기본값을 0으로 설정하는 효과
    blood_count = defaultdict(int)

    for blood in blood_types:
        blood_count[blood] += 1

    return dict(blood_count)  # 일반 딕셔너리로 변환하여 반환


print(count_blood_types_01(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
print(count_blood_types_02(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
print(count_blood_types_03(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
