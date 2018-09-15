class Solution:
    def isPalindrome(self, x):
        if x % 10 == 0 and x!=0 :
            return False
        return func(x,0)

def func(head,tail):
    if head > tail:
        return func(head//10,tail*10+head%10)
    if head == tail:
        return True
    if 0<=tail - head*10 <=9:
        return True
    return False
