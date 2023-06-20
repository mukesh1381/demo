# l = [10,20,"Sai",30,40,"Durga",'A',23.4,50,60]
# print(l[1])
# print(l[3])
# print(l[-2])
# print(l[-4])
# #print(l[12])
#
# print(l[1:8])
# print(l[-1:-5])
# print(l[3:1])
# print(l[1:8:-1])
# print(l[::-1])

#insert,append,extend

#l = [2,3,4]
# l[1] = 23
# print(l)
#
# l.insert(1,23)
# print(l)
#
# l.append(18)
# print(l)
#
# l.extend([23,34,56,47,'Ali','Jafar'])
# print(l)

#remove,pop,clear,del
# l = [10,20,30,40,50,60]
# #l.remove(30)
# print((l))
# l.pop()
# print(l)
# #l.clear()
# print(l)
# del l
# print(l)

#List concatenation
# l1 = [10,20,30,40]
# l2 = [50,60,70,80]
# print(l1+l2)
# print(l1*3)

l3 = [10,8,7,3,2,21,16,71,24,54]
#l3 = ['sai','dev','Ram','john','akram','sai']
#l3.sort()
#print(l3)
for i in range(len(l3)):
    for j in range(i+1, len(l3)):
        if l3[i] > l3[j]:
            l3[i],l3[j] = l3[j],l3[i]

print(l3)


# l3.sort(reverse=True)
# #print(l3)
# l4 = []
# for i in l3:
#     if i not in l4:
#         l4.append(i)
# # print(l4)
#
# #List sort
# l = [2,6,9,4,3,5,7,1]
# print(l)
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
#
# #List copy
# l1 = [10,20,30,40,50]
# l2 = l1.copy()
# l1.append(10)
# print(l1)
# print(l2)
# print(id(l1))
# print(id(l2))