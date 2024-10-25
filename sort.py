list_1=["oragne","banana","apple","pineapple","cola","grape"]

list_1.sort()

print(list_1)


list_2=[25,40,5,78,98,65]

list_2.sort()
print(list_2)



def my_fun(n):
    return abs(n-35)

list_3=[100,75,50,35,85]
list_3.sort(key=my_fun)
list_3.reverse()
print(list_3)



for x in list_2:
    list_3.extend(x)

print(list_3)
