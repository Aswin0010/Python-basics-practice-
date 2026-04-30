s=input("Enter String : ")
s2=input("Enter String 2 : ")
freq={}
if len(s)!=len(s2):
    print("not anagrams")
for i in s:
    freq[i]=freq.get(i,0)+1
for j in s2:
    freq[j]=freq.get(j,0)-1
if all(v==0 for v in freq.values()):
    print(s,"and",s2,"are anagrams")
else:
    print("not anagrams")    