# 실습과제
# 스다벅스는 줄어든 매출 때문에 지점 하나를 닫아야 하는 위기에 처해 있습니다.
# 어떤 지점을 닫는 게 회사에 타격이 적을지 고민이 되는데요.
# 서로 가까이 붙어 있는 매장이 있으면, 그 중 하나는 없어져도 괜찮지 않을까 싶습니다.
#
# 사장님은 비서 태호에게, 직선 거리가 가장 가까운 두 매장을 찾아서 보고하라는 임무를 주셨습니다.
#
# 함수 설명
# 태호는 영업팀에서 매장들 좌표 위치를 튜플 리스트로 받아왔습니다.
#   # 예시 tuple 리스트
#   test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
# 튜플은 각 매장의 위치를 xx, yy 좌표로 나타낸 것입니다. 0번 매장은 (2, 3)에, 그리고 1번 매장은 (12, 30) 위치에 있는 거죠.
#
# 태호가 사용하려는 함수 closest_pair는 이 좌표 리스트를 파라미터로 받고,
# 리스트 안에서 가장 가까운 두 매장을 [(x1, y1), (x2, y2)] 형식으로 리턴합니다.
#
# 참고로 태호는 이미 두 좌표 사이의 거리를 계산해 주는 함수 distance를 써 놨는데요,
# 함수 distance는 인풋으로 두 튜플을 받아서 그 사이의 직선 거리를 리턴합니다.
#   print(distance((2, 5), (5, 9))) # => 두 지점 사이의 거리 5.0이 출력됨

# 예시
#   # 테스트
#   test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
#   print(closest_pair(test_coordinates))
#   [(2, 3), (3, 4)]

# 내 풀이 = 실패
# # 제곱근 사용을 위한 sqrt 함수
# from math import sqrt
#
# # 두 매장의 직선 거리를 계산해 주는 함수
# def distance(store1, store2):
#     return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)
#
# # 가장 가까운 두 매장을 찾아주는 함수
# def closest_pair(coordinates):
#     dis = distance(coordinates[0], coordinates[1])
#     first = 0
#     second = 0
#     # 여기 코드를 쓰세요
#     for i in coordinates:
#         for j in coordinates:
#             if i != j:
#                 if distance(i, j) < dis:
#                     dis = distance(i, j)
#                     first = i
#                     second = j
#
# # 테스트
# test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
# print(closest_pair(test_coordinates))


# 제곱근 사용을 위한 sqrt 함수 불러오기
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    # 현재까지 본 가장 가까운 두 매장
    pair = [coordinates[0], coordinates[1]]

    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            store1, store2 = coordinates[i], coordinates[j]

            # 더 가까운 두 매장을 찾으면 pair 업데이트
            if distance(pair[0], pair[1]) > distance(store1, store2):
                pair = [store1, store2]

    return pair


# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))