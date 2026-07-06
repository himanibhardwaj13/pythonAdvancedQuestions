def fact(n):
    return 1 if n<=1 else n*fact(n-1)
    
print('Factorial of 5', fact(5))

def is_prime(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

is_prime(13)
def fibnosis(n):
    print(f"fibnosis series of {n}")
    a,b=0,1
    for _ in range(n):
        print(a, end = " ")
        a, b = b, a+b
        
fibnosis(5)

from collections import Counter
def anagram_check(s):
    return Counter(s.lower())
    
print("Is anagram ", anagram_check('abc')==anagram_check('bca'))

from itertools import permutations
def all_anagram(s):
    return [''.join(p) for p in permutations(s)]
    
print('All anagrams of abc', all_anagram('abc'))
