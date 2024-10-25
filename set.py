set_p={"delhi","vijayawada","tenali","guntur",True,1}

set_s=set(("jay","pr","kar","kar","la",False,0))

print(type(set_p))
print(type(set_s))

for x in set_p:
    print(x)

print("delhi" in set_p)
print(set_p)
print(set_s)


set_p.add("noida")
print(set_p)

set_p.update(set_s)
print(set_p)


set_p.remove("tenali")
x=set_s.pop()
print(x)

set_s.clear()
print(set_s)



ja_1=set(("ford","lambo","rolls","maruti"))

ka_2={"suzuki","maruti","kawasaki","royal"}


pq_3=ja_1.update(ka_2)

print(pq_3)


aq_4=ja_1&ka_2
print(aq_4)
