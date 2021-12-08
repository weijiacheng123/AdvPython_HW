import pandas as pd
from pandas.core.frame import DataFrame
f = pd.read_csv('Holiday Schedule Ranking 2019.csv')
names = []
date = []
dic = {}
num = 0
for i in f.Employee:
    names.append(i)
    dic[num] = 2
    num += 1
for i in f.columns[1:]:
    date.append(i)
names2 = [i for i in range(20)]
l1 = []
date.reverse()
it = 0
for i in date:
    count = 0
    # min = (index , number)
    min1 = ()
    min2 = ()
    min3 = ()
    for number in f[i]:
        if count in names2:
            if min1 ==() or min2 == () or min3 == ():
                if min1 == ():
                    min1 = (count, number)
                elif min2 == ():
                    min2 = (count, number)
                elif min3 == ():
                    min3 = (count, number)
            else:
                if number < min1[1]:
                    min1 = (count, number)
                elif number < min2[1]:
                    min2 = (count, number)
                elif number < min3[1]:
                    min3 = (count, number)
            if min1 != () and min2 != () and min3 != ():
                ll = [min1, min2, min3]
                ll = sorted(ll, key = lambda l : l[1] , reverse = True)
                min1 , min2 ,min3 = ll[0],ll[1],ll[2]
        count += 1
    l2 = [min1[0],min2[0],min3[0]]
    for k,v in dic.items():
        for index in l2:
            if k == index:
                dic[k] = v - 1
                if v - 1 == 0:
                    names2.remove(k)
    l1.append(l2)


for i in names2:
    index = 0
    for j in date:
        count = 0
        for number in f[j]:
            if number == 2 and count == i:
                l1[index].append(i)
            count += 1
        index += 1

l2 = []
num = 0
schedule = []
for i in date:
    schedule.append([i])
for i in l1:
    for j in i:
        n = names[j]
        schedule[num].append(n)
    num += 1
data = DataFrame(schedule)
data = data.rename(columns = {0:'Date' , 1:'name',2:'name',3:'name',4:'name'})
print(data)
data.to_csv("schedule.csv")

