# Problem 3: Is it Palindrome?
t = int(input().strip())
for _ in range(t):
    s = input().strip()
    print(1 if s == s[::-1] else 0)
