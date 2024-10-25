data=["zebra","lion","tiger","cheetah","fox"]

"""for i in range(len(data)):
    print(data[i])"""

"""i=0
while i<(len(data)):
    print(data[i])
    i=i+1"""


my_l=list(["jay","salaar","deva"])
new_list=[]

for x in my_l:
    if "a" in x:
        new_list.append(x)
    print(new_list)



l1=["smtp","i2c","spi","uart"]

new_l=[i.upper() if i!="smtp" else "uart"  for i in l1]
print(new_l[0])
