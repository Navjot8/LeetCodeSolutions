mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

# mat = [[1, 1, 1, 1],
#        [1, 1, 1, 1],
#        [1, 1, 1, 1],
#        [1, 1, 1, 1]]
# [00,11,22,33
# 03,12,21,30
length = len(mat)
k = length // 2
flag = False
if k % 2 == 0:
    flag = True
matsum = []
print(k)
for i in range(len(mat)):
    if flag:
        matsum.append(mat[i][i])
    else:
        if i!=k:
            matsum.append(mat[i][i])

count = len(mat) - 1

for i in range(len(mat)):
    matsum.append(mat[i][count])
    count -= 1
print(sum(matsum))
