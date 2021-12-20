# s = "10[a2[c]]"
# s="n20[i]"
# # s = "3[a]2[bc]"
# # s = "2[abc]3[cd]ef"
# # s = "abc3[cd]xyz"
# # s="100[leetcode]"
alpha = "abcdefghijklmnopqrstuvwxyz"

number = "1234567890"
string = ""


result = 0
count = 0
num = 0
a = ""
d = []
c = 0

s="3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
for i, v in enumerate(s):
    if v in number and s[i + 1] == "[":
        o = s[c:i + 1]
        f=""
        for q in o:
            if q=="[":
                f=""
            if q in number:
              f+=q

        d += [[i, f]]
        c=i

        c=i
    elif v in alpha:
        c += 1
d = d[::-1]
print(d)
for i in range(0, len(d)):
    count = int(d[i][0])
    n = s[:count]
    t = ""
    string = ""
    while t != "]":
        t = s[count]
        string += s[count]
        m = ""
        count += 1
    p = s[count:]
    for a in string:
        if a in alpha:
            m += a
    string = int(d[i][1]) * m

    s = n + string + p
count2=0
finalstring=""
for i in s:
    if i not in number:
        finalstring+=i
print(finalstring)

# print(s[count2:])
# print(s)
# zzzpqjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkefjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkefjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkefjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkefpqjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkefjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkefjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkefjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkefef

print("zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"=="zzzpqjkjkefjkjkefjkjkefjkjkefpqjkjkefjkjkefjkjkefjkjkefef")