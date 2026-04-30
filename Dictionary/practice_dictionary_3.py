s=input("Enter String : ").lower().split()
groups={}
for word in s:
    freq=[0]*26
    for ch in word:
        index=ord(ch)-ord('a')
        freq[index]+=1
    key=tuple(freq)
    if key in groups:
        groups[key].append(word)
    else:
        groups[key]=[word]
print("Grouped Anagrams : ")
print(list(groups.values()))             