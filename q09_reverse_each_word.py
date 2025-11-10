# Problem 9: Reverse each word in the string
A = input().rstrip("\n").split()
print(" ".join(w[::-1] for w in A))
