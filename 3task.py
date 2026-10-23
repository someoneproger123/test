man_num = int(input())
oves_num = int(input())
man=list()
oves=list()
for i in range(man_num):
    man.append(input())
for i in range(oves_num):
    oves.append(input())
s_man = set(man)
s_oves = set(oves)
result =s_man.intersection(s_oves)
if len(result) > 0:
    print(len(result))
else:
    print('Таких нет')
