
input = "abcba"


#  v   v
#   v v
#    v
# "abcba"

def is_palindrome(string):
    n = len(string)
    for i in range(n): # i : 0 ~ n -1
        if string[i] != string[n - 1 - i] :
            return False

    return True


print(is_palindrome(input))