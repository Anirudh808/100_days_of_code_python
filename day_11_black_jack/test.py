import re


def isPalindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    i = 0
    j = len(s) - 1

    print(s)

    while j > j / 2:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
