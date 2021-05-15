def isPalindrome (x):
    if type(x) != str:
        return 1
    elif x == x[::-1]:
        a = "is a palindrome"
        return a
    else:
        b ="is not a palindrome"
        return b
    