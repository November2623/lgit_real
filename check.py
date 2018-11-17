# n = 10
# list1 = []
# S = 0
# def len_number(n):
#     a = n
#     i = 0
#     while a != 0:
#         a = a // 10
#         i += 1
#     return i
# for i in range(1,n + 1):
#     list1.append(i)
# print(list1)
# list2 = list(reversed(list1))
# print(list2)
# len = len(list1)
# temp = 0
# for i in list2:
#     k = len_number(i)
#     print(i)
#     S= S+ i*pow(pow(10,k),temp)
#     temp = temp + 1
#     # print(i)
#     # k = len_number(i)
#     # # print(k)
#     # if k == 1:
#     #     S = S + i*pow(pow(10,k),len-1)
#     # elif k == 2:
#     #     S = S + i*pow(pow(10,k),len -1)
#     # len -= 1

n = 111
temp = 0
temp2 = n
count = 10
for i in range(n+1):
    if i % 10 == 0 and i // count == 1:
        count *= 10
    temp = temp*count + i
