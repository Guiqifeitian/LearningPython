def is_palindrome(n):
    s=str(n)
    i=0
    while i<len(s):
        if s[i]!=s[-i-1]:#���������������������Ҽ�����
            return False
        i=i+1
    return True
        
output = filter(is_palindrome, range(1, 1000))
print(list(output))