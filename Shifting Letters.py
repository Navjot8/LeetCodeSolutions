s = "bad"
shifts = [500000, 20, 30]
alpha = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

count = 0
for i in range(1, len(s) + 1):
    string = ""
    for k in range(i):
        t = alpha.find(s[k])
        string += alpha[t + shifts[count]]

    s = string[:i] + s[i:]
    count += 1

print(string)
# "mkgfzkkuxownxvfvxasy"
#
# s = "baabb"
# t = ""
#
#
# def find(text, pattern):
#     for i in range(len(text) - len(pattern) + 1):
#         j = 0
#         while j < len(pattern):
#             if text[i + j] != pattern[j]:
#                 break
#             j += 1
#         if j == len(pattern):
#             return j
#     return -1
#
#
# def pal(s):
#     t = ""
#     for i in range(len(s)):
#         x = ""
#         for k in s[i:]:
#             x += k
#             if x == x[::-1]:
#                 if len(t) < len(x):
#                     t = x
#     return t
#
#
# string = "abbaaaab"
# count=0
# while string!="":
#     t1 = pal(string)
#     print(t1)
#     l = find(string, t1)
#     string=string[l:]
#     count+=1
# print(count)
# n number of element in the list
# nth element in the list ?
# what is the time complexity for this? o(1)
# o(n^2) n in the n number of list
