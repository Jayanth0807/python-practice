my_tuple=("delhi","amritsar","jaipur","udaipur","rajasthan")

print(type(my_tuple))
print(len(my_tuple))
print(my_tuple)


print(my_tuple[2:])
print(my_tuple[:4])

if "delhi" in my_tuple:
    print("delhi is there")



x=list(my_tuple)
x[1]="gujarat"

y=tuple(x)
print(y)

z=("kerala",)

y=y+z

print(y)


tuple_p=("orange","berry","apple","banana","dragon")

(red,*green,yellow)=tuple_p

print(red)
print(green)
print(yellow)

tuple_i=("jay","ud","deva","vara")

for x in range(len(tuple_i)):
    print(tuple_i[x])
x=tuple(tuple_i)

my_t=x*2

print(my_t)
