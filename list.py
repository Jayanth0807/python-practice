my_list=["apple","banana","jackfruit","apple","strawberry"]

print(my_list)
print(len(my_list))
print(type(my_list))

print(my_list[-2])

print(my_list[2:4])


print(my_list[1:])

print(my_list[:2])




my_list1=["delhi","pune","hyderabad","vizag","tenali","guntur"]

print(my_list1)
print(type(my_list1))

my_list1[0]="vijayawada"
print(my_list1)

my_list1[1:4]=["amritsar","jaipur","nagpur"]
print(my_list1)


my_list1.insert(3,"hyd")

print(my_list1)


my_list1.extend(my_list)

print(my_list1)

my_tuple=(86,19,8,1)

my_list1.extend(my_tuple)

print(my_list1)
