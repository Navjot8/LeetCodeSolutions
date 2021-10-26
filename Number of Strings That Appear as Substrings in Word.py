patterns = ["a","b","c"]
word = "aaaaabbbbb"
count=0
for i in patterns:
    if i in word:
        count+=1
print(count)