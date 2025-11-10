# Problem 16: Count occurrences of 'bob'
A = input().strip()
cnt = 0
for i in range(len(A) - 2):
    if A[i:i+3] == "bob":
        cnt += 1
print(cnt)
