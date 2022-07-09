import collections
# x = ['bat', 'car', '8', 'track', 'game', 'car', 'people', 'country', 'game', 'road', 'dog', 'cat', 'track', "free", 'plane', 'pain', 'dog', 'robot']
# y = []
# z = set([])
# # for i in x:
# #     if len(y) == 0:
# #         y.append(i)
# #     elif not(i in y):
# #         y.append(i)
# # print(y)
#
# for i in x:
#     z.add(i)
# print(z)

# x = {89543454342: "Иванов", 89765456543: "Петров", 89075432167: "Сидоров", 89039740333: "Волков", 89262645378: "Иванов", 8765432123: "Сидоров"}
# z = set([])
# for i in x:
#     z.add(x[i])
# n = len(x) - len(z)
# print(n)

x = ['6', '5', '5']
c = collections.Counter()
for i in x:
    c[i] += 1
print(c)