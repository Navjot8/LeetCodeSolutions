sentence = "I speak Goat Latin"
vowel="aeiou"
count=0
wordList=[]
for word in sentence.split():
    count+=1
    if word[0].lower() in vowel:
        word+="ma"
    else:
        temp=word[1:]+word[0]+"ma"
        word=temp
    word+=count*"a"
    wordList.append(word)
    # count+=1
print(" ".join(wordList))