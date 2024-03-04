v1 = input("Write first vector: ")
split_v1 = v1.split()
v2 = input("Write first vector: ")
split_v2 = v2.split()
v1_v2 = 0

for i in range(len(split_v1)):
    v1_v2 += int(split_v1[i]) * int(split_v2[i])

print(v1_v2)
