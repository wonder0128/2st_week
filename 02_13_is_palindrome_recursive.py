
input = "abcba"

# 재귀함수는 문제의 범위를 조금씩 좁혀 나가는 것
#  v   v
#   v v
#    v
#  abcba

def is_palindrome(string):
    if string[0] != string[-1]:
        return False

    if len(string) <= 1:
        return True
    
    return is_palindrome(string[1:-1])


print(is_palindrome(input))