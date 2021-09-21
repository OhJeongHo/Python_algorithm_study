#'선형 탐색(Linear Search)' 알고리즘을 사용해서 어떤 원소가 리스트 안에 포함되어 있는지 확인하려고 합니다.
# 선형 탐색이란, 리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘입니다.
#파라미터로 탐색할 값 element와 리스트 some_list를 받는 함수 linear_search를 작성하세요.
# 0번 인덱스부터 순서대로 하나씩 확인해서 만약 element를 some_list에서 발견할 시 그 위치(인덱스)를 리턴해 주면 됩니다.
#element가 some_list에 존재하지 않는 값이면 None을 리턴해주세요.

# 예시코드
#def linear_search(element, some_list):
    # 코드를 작성하세요.

#print(linear_search(2, [2, 3, 5, 7, 11]))
#print(linear_search(0, [2, 3, 5, 7, 11]))
#print(linear_search(5, [2, 3, 5, 7, 11]))
#print(linear_search(3, [2, 3, 5, 7, 11]))
#print(linear_search(11, [2, 3, 5, 7, 11]))


# 정답 코드 작성.
def linear_search(element, some_list):
    # 코드를 작성하세요.
    for i in range(len(some_list)):     # 리스트의 길이만큼 for문을 돌림
        if some_list[i] == element:     # 각 원소 숫자에 해당하는 값이 찾는 값과 일치하는 지?
            return i                    # 일치하면 그 원소번호를 리턴
    return None                         # 끝까지 없으면 None을 반환

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))