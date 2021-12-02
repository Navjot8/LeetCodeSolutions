def matchString(txt, pattern):
    for i in range(len(txt) - len(pattern) + 1):
        j = 0
        while j < len(pattern):
            if txt[j + i] != pattern[j]:
                break
            j += 1
        if j == len(pattern):
            print("Index found at index, ", pattern)


wordDict =["cats","dog","sand","and","cat"]
text = "catsandog"
for i in wordDict:
    matchString(text,i)
