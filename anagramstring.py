s1='abcdefghijklmnopqrstuvwxyz'
s='the quick brown fox jumps over lazy dog'
flag=True
for i in s1:
    if i not in s:
        flag=False
if flag==True:
    print("string is anagram")
else:
    print("string is not anagram")

