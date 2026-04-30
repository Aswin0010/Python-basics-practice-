s=input("Enter String : ")
freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
for i in s:
    if freq[i]==1:
        print(i,"is the first non repeating character")
        break
else:
    print("no non repeating character")           