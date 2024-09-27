def is_palindrome(s):
    s=s.replace('','').lower()
    return s==s[::-1]
s1="racecar"
s2="hello world"
print(f"{s1} is palindrome:{is_palindrome(s1)}")
print(f"{s2} is palindrome:{is_palindrome(s2)}")