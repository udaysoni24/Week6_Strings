# Problem 1: Vowels vs Consonants
t = int(input().strip())
vowels = set("aeiouAEIOU")
for _ in range(t):
    s = input().strip()
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    print(v, c)
