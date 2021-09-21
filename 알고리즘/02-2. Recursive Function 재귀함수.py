def countdown(n):
    if n > 0:
        print(n)
        countdown(n-1)

countdown(4)


# 재귀함수를 활용해서 팩토리얼 문제 풀기
# 0! = 1, 1! = 1, 2! = 2, 3! = 6...

# base case => n=0인 경우 - n! = 1
# recursive case => n > 0 인 경우 - n! = (n-1)! * n

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

print(factorial(4))