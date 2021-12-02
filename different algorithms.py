def stringMatch(text, pattern) -> bool:
    for i in range(len(text) - len(pattern) + 1):
        j = 0
        while j < len(pattern):
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == len(pattern):
            print("sting found at index ", i)

    return False


def binarySearch(arr, val):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + end // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            start = mid - 1
        else:
            end = mid + 1
    return -1


def maxLengthPlaindrom(text):
    dic = {i: text.count(i) for i in text}
    flag = False
    length = 0
    for key, val in dic.items():
        if val % 2 != 0:
            flag = True
        length += val // 2 * 2
    if flag:
        length += 1
    return length


def removeAtleastOnecharToMakePlaindrom(text):
    start = 0
    end = len(text) - 1
    while start < end:
        if text[start] == text[end]:
            start += 1
            end -= 1
        else:
            return text[start:end] == text[start:end][::-1] or text[start + 1:end + 1] == text[start + 1:end + 1][::-1]
    return True


def groupingAnagraam(listofwords):
    dic = {}
    for i in listofwords:
        key = "".join(sorted(list(i)))
        if key not in dic.keys():
            dic[key] = [i]
        else:
            dic[key].append(i)
    return dic.values()


def SumOfIndexToSpecificValue(arr, val):
    start = 0
    end = len(arr) - 1
    arr = sorted(arr)
    while start < end:
        if arr[start] + arr[end] == val:
            return start, end
        elif arr[start] + arr[end] < val:
            start += 1
        else:
            end -= 1

def findPalindrom(text):
    palindrom=""
    for i in range(len(text)):
        x=""
        for k in text[i:]:
            x+=k
            if x==x[::-1]:
                if len(palindrom)<len(x):
                    palindrom=x
    return palindrom

print(SumOfIndexToSpecificValue([1, 2, 3, 4, 5, 6, 7], 8))
print(groupingAnagraam(["eat", "tea", "ate", "bat", "sat"]))
print(removeAtleastOnecharToMakePlaindrom("abaey"))
print(maxLengthPlaindrom("abeba"))
print(binarySearch([1, 2, 3, 4, 5], 3))
print(stringMatch("jkbbskjabdkfjbkjbjasnavjjaksbfaonavojosodfnaaahssdnackjknkasdfnav", "nav"))
print(findPalindrom("utt"))

