def stringMatch(text,pattern):
    for i in range(len(text)-len(pattern)+1):
        j=0
        while j< len(pattern):
            if text[i+j]!=pattern[j]:
                break
            j+=1
        if j==len(pattern):
            print("string found at index",i)
    return
print(stringMatch("navnkjnkadnavjknkjnassdfiuhuihrtanavkjnakjdnfanvjkansfnav","nav"))