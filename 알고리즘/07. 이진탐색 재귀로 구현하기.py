# 내가 푼 풀이
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # 코드를 작성하세요.
    midpoint = (start_index + end_index) // 2
    if start_index > end_index:
        return None
    if some_list[midpoint] == element:
        return midpoint
    elif some_list[midpoint] > element:
        return binary_search(element, some_list[:midpoint])
    elif some_list[midpoint] < element:
        return midpoint + 1 + binary_search(element, some_list[midpoint+1:])

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

#  내가 푼 풀이는 재귀로 들어가는 리스트 자체를 슬라이싱하고 인덱스 값을 더해주면서 반복시키는 것이고
#  풀이에서의 방법은, 스타트인덱스와 엔드인덱스를 직접 지정해주면서 따로 인덱스값은 저장하지 않는 풀이방법이다.

# 공식 정답

def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # start_index가 end_index보다 크면 some_list안에 element는 없다
    if start_index > end_index:
        return None

    # 범위의 중간 인덱스를 찾는다
    mid = (start_index + end_index) // 2

    # 이 인덱스의 값이 찾는 값인지 확인을 해준다
    if some_list[mid] == element:
        return mid

    # 찾는 항목이 중간 값보다 작으면 리스트 왼쪽을 탐색해준다
    if element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)

    # 찾는 항목이 중간 값보다 크면 리스트 오른쪽을 탐색해준다
    else:
        return binary_search(element, some_list, mid + 1, end_index)


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))