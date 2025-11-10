# Problem 17: String operations
# Steps: Concatenate with itself -> remove uppercase -> replace vowels with '#'
A = input().strip()
A = A + A
A = ''.join(ch for ch in A if not ch.isupper())
vowels = set("aeiou")
A = ''.join('#' if ch in vowels else ch for ch in A)
print(A)
