# Deque is a double-ended queue
from collections import deque

def ispalindrome(word):
    """
    Check if the word is palindrome.
    Return True if the word can be read the same backward or forward. Otherwise, return False.
    """
    word_dq = deque(word)
    while len(word_dq) > 1:
        if word_dq.popleft() != word_dq.pop():
            return False
        return True


if __name__ == '__main__':
    print(ispalindrome("tanet"))
    print(ispalindrome("racecar"))
    print(ispalindrome("hello"))
    print(ispalindrome("madam im adam"))
