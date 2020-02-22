l = []
s = ['dog', 'cat', 'cat', 'mouse', 'dog']

for i in range(len(s)):
    if s[i] not in l:
        l.append(s[i])

print(l)