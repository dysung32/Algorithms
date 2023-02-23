A = int(input())
B = int(input())
C = int(input())

num = A * B * C
num_list = list(str(num))

for i in range(10):
    print(num_list.count(str(i)))