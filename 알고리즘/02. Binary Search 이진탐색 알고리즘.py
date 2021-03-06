#‘이진 탐색(Binary Search)’ 알고리즘을 사용해서 어떤 원소가 리스트 안에 포함되어 있는지 확인하려고 합니다.
# 이진 탐색 알고리즘은 선형 탐색 알고리즘과 달리, 정렬된 리스트를 전제로 합니다. 정렬된 리스트가 아니면 이 알고리즘은 적용이 불가능합니다.
#왜 이 알고리즘의 이름이 ‘이진 탐색’일까요? 1회 비교를 거칠 때마다 탐색 범위가 (대략) 절반으로 줄어들기 때문입니다.

#예시
#예를 들어 [1, 2, 3, 5, 8, 13, 21, 34, 55]에서 3을 찾는 경우, 알고리즘의 진행 방식은 다음과 같습니다:

#시도 1
#리스트의 첫 번째 인덱스와 마지막 인덱스의 값을 합하여 2로 나눈 후, 중간 인덱스로 지정합니다.
# 그리고 그 인덱스에 해당하는 값이 3인지 확인해봅니다.

#이 경우 리스트의 첫 번째 인덱스는 0이고 마지막 인덱스는 8이기 때문에, 중간 인덱스는 4이고 해당 원소는 8입니다.
#찾고자 하는 원소(3)는 중간 원소(8)에 비해 작습니다. 리스트는 정렬되어 있으니, 이제 인덱스 4~8은 탐색 범위에서 제외시킬 수 있습니다.
# 탐색 범위가 절반으로 줄어든 것이죠.

#시도 2
#탐색 범위는 이제 인덱스 0~3입니다.
# 탐색 범위의 첫 번째 인덱스는 0이고 마지막 인덱스는 3이기 때문에, 중간 인덱스는 (0 + 3) // 2인 1입니다. 인덱스 1에 해당하는 원소는 2이죠.

#찾고자 하는 원소(3)는 중간 원소(2)에 비해 큽니다. 리스트는 정렬되어 있으니, 이제 인덱스 0~1은 탐색 범위에서 제외시키면 됩니다.
# 탐색 범위가 다시 절반으로 줄어든 것이죠.

#시도 3
#탐색 범위는 이제 인덱스 2~3입니다. 탐색 범위의 리스트의 첫 번째 인덱스는 2이고 마지막 인덱스는 3이므로, 중간 인덱스는 (2 + 3) // 2인 2입니다.
# 인덱스 2에 해당하는 원소의 값은 3이죠.

#찾고자 하는 원소(3)는 중간에 해당하는 원소(3)와 일치합니다. 값을 찾았으니, 인덱스 2를 리턴해주며, 알고리즘을 종료합니다.


# 코드를 작성할 것.
# def binary_search(element, some_list):
#     # 코드를 작성하세요.
#
# print(binary_search(2, [2, 3, 5, 7, 11]))
# print(binary_search(0, [2, 3, 5, 7, 11]))
# print(binary_search(5, [2, 3, 5, 7, 11]))
# print(binary_search(3, [2, 3, 5, 7, 11]))
# print(binary_search(11, [2, 3, 5, 7, 11]))


# while 사용해서 풀기
# def binary_search(element, some_list):
#     # 코드를 작성하세요.
#     j = 0   # 중간값 => 최종적으로 리턴하기전엔 해당반복 리스트의 첫인덱스값을 기록함.
#     while len(some_list) != 0:      # 리스트 길이가 0이 아니면 반복해라
#         i = len(some_list) // 2     # i 는 리스트의 길이의 절반 값.
#
#         if element > some_list[i]:          # 찾는 값이 중간원소값보다 클 때 -> 리스트의 오른쪽 부분만 필요함
#             some_list = some_list[i + 1:]   # 리스트를 i+1 부터 끝까지 슬라이싱해서 새롭게 대입함
#             j += (i + 1)                    # 이제 i+1이 첫인덱스값이므로 이를 j에다 더함
#         elif element < some_list[i]:        # 찾는 원소값이 중간값보다 작을 때 -> 리스트의 왼쪽 부분만 필요함
#             some_list = some_list[:i]       # 리스트 0 부터 i까지 슬라이싱해서 새로운 리스트로 대입함
#         elif element == some_list[i]:       # 찾는 값이 리스트의 중간값과 동일할 경우
#             j += i                          # j 에다가 i를 더함
#             return j                        # j 를 리턴
#     return None                             # 리스트의 길이가 0이되서 while문이 끝날떄까지 동일값이 없으면 None리턴





# 공식적인 정답
def binary_search(element, some_list):
    start_index = 0                     # 시작 인덱스
    end_index = len(some_list) - 1      # 마지막 인덱스

    while start_index <= end_index:     # 시작인덱스가 끝인덱스보다 작아지면 종료 // 둘다 0이라면 한번 돌게되고 끝인덱스는 -1이 됨.
        midpoint = (start_index + end_index) // 2   # 중간 지점은 양끝 더해서 //2를 해준 값.
        if some_list[midpoint] == element:      # 중간값이 찾는 값과 동일하다면
            return midpoint                     # 해당 중간원소번호를 리턴
        elif some_list[midpoint] > element:     # 찾는 값보다 더 크다면
            end_index = midpoint - 1            # 끝 인덱스를 중간값-1로 바꿈 => 중간값보다 큰 값들을 전부 버린 것.
        else:                                   # 그 외 = 찾는 값보다 중간값이 더 작다면
            start_index = midpoint + 1          # 시작 인덱스를 중간값+1로 바꿈 => 중간값보다 작은 값들을 전부 버린 것.
    return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))