# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    # base case
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list

    # recursive case
    return some_list[-1:] + flip(some_list[:-1])
# some_list[-1:] 의 값은 마지막 원소부터 끝까지이므로, 마지막 원소 하나만을 뜻한다.
# some_list[:-1] 의 값은 첫번째 원소부터 -1원소 즉, 마지막 원소전까지를 뜻하므로, 끝원소 제외한 앞쪽 모두를 뜻한다.
# 고로, flip(some_list[:-1]) 를 반복할수록 리스트의 길이가 짧아지게 되는 것.


# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)